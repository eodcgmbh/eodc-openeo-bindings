import itertools
import json
import os
from typing import List, Dict
from uuid import uuid4

import numpy as np
import osr
import requests
from eodatareaders.eo_data_reader import eoDataReader
from geopathfinder.naming_conventions.eodr_naming import eoDRFilename
from osgeo import gdal


def array_to_raster(array, out_folder, out_filename, wkt_projection, raster_size, geotransform):
    """Array > Raster
    Save a raster from a C order array.

    :param array: ndarray
    """
    
    os.makedirs(out_folder, exist_ok=True)
    out_filepath = os.path.join(out_folder, out_filename)

    driver = gdal.GetDriverByName('GTiff')
    dataset = driver.Create(
        out_filepath,
        raster_size[0],
        raster_size[1],
        1,
        gdal.GDT_Float32, )

    dataset.SetGeoTransform(geotransform)

    dataset.SetProjection(wkt_projection)
    dataset.GetRasterBand(1).WriteArray(array)
    dataset.FlushCache()  # Write to disk.


class UdfExec:

    def __init__(self, input_paths: List[str], params: Dict[str, str]):
        self.input_paths = input_paths
        self.input_params = params
        self.output_folder = self.input_params["output_folder"]
        self.url = self.get_url()

        self.json_params: dict = None
        self.input_json: dict = None
        self.return_json: dict = None
        self.input_json_extra: dict = None

        self.execute()

    def execute(self):
        self.create_json_param()
        self.create_json()
        worked, response = self.send_request()
        if not worked:
            return Exception(response)
        self.return_json = json.loads(response)
        self.write_to_disk()

    def get_url(self):
        runtime = self.input_params["runtime"]
        if runtime == "python":
            return os.environ.get("OPENEO_PYTHON_UDF_URL")
        if runtime == "r":
            return os.environ.get("OPENEO_R_UDF_URL")
        raise Exception(f"Runtime {runtime} is currently not supported")

    def create_json_param(self):
        self.json_params = {
            "general_id": str(uuid4()),
            "hypercube_id": str(uuid4()),  # potentially multiple ones
            "source": self.input_params["udf"],
            "language": self.input_params["runtime"]
        }
        self.input_json_extra = {}
        eo_deck = eoDataReader(self.input_paths)
        
        # NB assumes the projection is already the same for all rasters
        proj = osr.SpatialReference(wkt=eo_deck.eo_mdc.iloc[0].raster.projection)
        self.json_params["proj"] = "EPSG:" + proj.GetAttrValue('AUTHORITY', 1)
        
        self.json_params["bands"] = sorted(list(set(eo_deck.eo_mdc.band)))
        self.json_params["time"] = sorted(list(set(eo_deck.eo_mdc.time.astype(str))))
        
        self.input_json_extra["proj_full"] = eo_deck.eo_mdc.iloc[0].raster.projection
        self.input_json_extra["geotransform"] = eo_deck.eo_mdc.iloc[0].raster.geotransform
        self.input_json_extra["size_pixel"] = eo_deck.eo_mdc.iloc[0].raster.size_pixel[0]
        self.input_json_extra["size_raster"] = eo_deck.eo_mdc.iloc[0].raster.size_raster
        
        x_size = self.input_json_extra["size_raster"][0]
        y_size = self.input_json_extra["size_raster"][1]
        x = np.arange(0, x_size)
        y = np.arange(0, y_size)
        data = np.meshgrid(x, y)
        x = list(data[0].flatten())
        y = list(data[1].flatten())
        x2, y2 = eo_deck.eo_mdc.iloc[0].raster.pix2coords((x, y))
        self.json_params["x"] = x2[0:x_size]
        self.json_params["y"] = y2[0::x_size]
        
        # Get data
        data = []
        eo_mdc_groups = eo_deck.eo_mdc.groupby(['band'])
        for idx, eo_mdc_group in eo_mdc_groups:
            band_data = []
            for counter in np.arange(0, len(eo_mdc_group)):
                current_data = eo_mdc_group.iloc[counter].raster.load_raster()
                band_data.append(current_data.tolist())
                del current_data
            data.append(band_data)
            del band_data
        self.json_params["data"] = data
        del data

    def create_json(self):
        # TODO distinction between different types
        self.input_json = self.create_hypercube()

    def create_hypercube(self):
        # TODO multiple hypercubes
        return {
            "code": {
                "source": self.json_params["source"],
                "language": self.json_params["language"]
            },
            "data": {
                "id": self.json_params["general_id"],
                "proj": self.json_params["proj"],
                "hypercubes": [
                    {
                        "id": self.json_params["hypercube_id"],
                        # order of dimensions have to match data structure
                        "dimensions": [
                            {
                                "name": "band",
                                "coordinates": self.json_params["bands"]
                            },
                            {
                                "name": "time",
                                "coordinates": self.json_params["time"],
                            },
                            {
                                "name": "y",
                                "coordinates": self.json_params["y"],
                            }, 
                            {
                                "name": "x",
                                "coordinates": self.json_params["x"],
                            }
                        ],
                        "data": self.json_params["data"],
                    },
                ],
            },
        }

    def send_request(self):
        response = requests.post(url=self.url, json=self.input_json, headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            return True, response.text
        return False, response.text

    def write_to_disk(self):
        # TODO extent to other data types
        def set_filename_param(filename_field, dim_name):
            if dim_name in dim_idx:
                dim_param_idx = dim_idx[dim_name]
                filename_fields[filename_field] = cube["dimensions"][dim_param_idx]["coordinates"][indices[dim_param_idx]]
            if dim_name == "time":
                filename_fields[filename_field] = self.convert_datetime_fmt(filename_fields[filename_field])

        for cube in self.return_json['hypercubes']:
            # create dict of {dim_name: dim_index}
            dim_idx = {}
            for idx, dim in enumerate(cube['dimensions']):
                dim_idx[dim["name"]] = idx

            num_dims = len(cube['dimensions']) - 2
            dim_elems = []
            for k in np.arange(num_dims):
                dim = cube['dimensions'][k]
                dim_elems.append(list(np.arange(0, len(dim['coordinates']))))

            indices_list = list(itertools.product(*dim_elems))
            for indices in indices_list:
                raster = cube['data']            
                for k, index in enumerate(indices):
                    raster = raster[index]
                raster2 = np.array(raster)
                
                # Create filename, set needed params if given in dimensions
                filename_fields = {}
                set_filename_param(filename_field="band", dim_name="band")
                set_filename_param(filename_field="dt_1", dim_name="time")
                eodr_filename = str(eoDRFilename(filename_fields, ext='.tif'))
                # Save array to disk
                array_to_raster(raster2, self.output_folder, eodr_filename, 
                                self.input_json_extra["proj_full"], self.input_json_extra["size_raster"],
                                self.input_json_extra["geotransform"]
                                )

    @staticmethod
    def convert_datetime_fmt(time_str: str):
        return time_str.replace('-', '').replace(' ', 'T').replace(':', '').split('+')[0]
