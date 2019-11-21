import json
from typing import List, Dict
from uuid import uuid4

import numpy as np
import osr
import requests
from eodatareaders.eo_data_reader import eoDataReader


class UdfExec:

    def __init__(self, input_paths: List[str], params: Dict[str, str]):
        self.url = "http://localhost:5000/udf"  # TODO should come from environment variable
        self.input_paths = input_paths
        self.input_params = params
        self.output_folder = self.input_params["output_folder"]

        self.json_params: dict = None
        self.input_json: dict = None
        self.return_json: dict = None

        self.execute()

    def execute(self):
        self.create_json_param()
        self.create_json()
        worked, response = self.send_request()
        if not worked:
            return Exception(response)
        self.return_json = json.loads(response)
        self.write_to_disk()

    def create_json_param(self):
        self.json_params = {
            "general_id": uuid4(),
            "hypercube_id": uuid4(),  # potentially multiple ones
            "source": self.input_params["udf"],
            "language": self.input_params["runtime"]
        }
        eo_deck = eoDataReader(self.input_paths)
        # TODO save information from eoDataReaders: proj, time, band, x- y-coord
        
        # NB assumes the projection is already the same for all rasters
        proj = osr.SpatialReference(wkt=eo_deck.eo_mdc.iloc[0].raster.projection)
        self.json_params["proj"] = "EPSG:" + proj.GetAttrValue('AUTHORITY', 1)
        
        self.json_params["bands"] = list(eo_deck.eo_mdc.band)
        self.json_params["time"] = list(eo_deck.eo_mdc.time.astype(str))
        
        x = np.arange(0, eo_deck.eo_mdc.iloc[0].raster.size_raster[0])
        y = np.arange(0, eo_deck.eo_mdc.iloc[0].raster.size_raster[1])
        data = np.meshgrid(x, y)
        x = list(data[0].flatten())
        y = list(data[1].flatten())
        (self.json_params["x"], self.json_params["y"]) = eo_deck.eo_mdc.iloc[0].raster.pix2coords((x, y))
        
        # Get data
        data = []
        eo_mdc_groups = eo_deck.eo_mdc.groupby(['band', 'time'])
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
        
        # self.json_params["data"] = []
        # for k in len(eo_deck.eo_mdc.bands):
        #     self.json_params["data"].append(
        #         eo_deck.eo_mdc.iloc[k].raster.load_raster()
        #     )
        #array = xarray.DataArray(numpy.zeros(shape=(2, 3)), coords={'x': [1, 2], 'y': [1, 2, 3]}, dims=('x', 'y'))

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
                "id": self.json_params["data_id"],
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
                            }, {
                                "name": "y",
                                "coordinates": self.json_params["y"],
                            }, {
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
        # TODO write response json to disk
        pass
