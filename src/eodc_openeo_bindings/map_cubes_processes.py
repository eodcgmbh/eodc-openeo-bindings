"""

"""

from os import environ
from owslib.csw import CatalogueServiceWeb
from owslib.fes import PropertyIsLike, BBox, PropertyIsLessThan, PropertyIsGreaterThan


def map_load_collection(process):
    """
    Retrieves a file list and maps bbox and band filters to eoDataReaders.
    """

    # Get list of filepaths fro csw server
    filepaths = csw_query(collection=process['arguments']["id"],
                          spatial_extent=(
                              process['arguments']['spatial_extent']['south'],
                              process['arguments']['spatial_extent']['west'],
                              process['arguments']['spatial_extent']['north'],
                              process['arguments']['spatial_extent']['east']
                              ),
                          temporal_extent=process['arguments']["temporal_extent"]
                         )

    dict_item_list = []

    # Map band filter
    if 'bands' in process['arguments'].keys():
        dict_item = map_filter_bands(process)[0]
        dict_item_list.append(dict_item)

    # Map bbox filter
    if 'spatial_extent' in process['arguments'].keys():
        dict_item = map_filter_bbox(process)[0]
        dict_item_list.append(dict_item)

    return dict_item_list, filepaths
    

def map_filter_bands(process):
    """

    """

    dict_item_list = []

    if 'bands' in process['arguments'].keys():
        load_bands = process['arguments']['bands']
    elif 'names' in process['arguments'].keys():
        load_bands = process['arguments']['names']
    # elif 'wavelenghts' in process['args'].keys():
    #     # add this option
    else:
        load_bands = 'all'
    
    dict_item = {'name': 'filter_bands', 'bands': load_bands}
    dict_item_list.append(dict_item)

    return dict_item_list


def map_filter_bbox(process):
    """

    """

    # TODO support fields 'base' and 'height'

    dict_item_list = []

    if 'spatial_extent' in process['arguments'].keys():
        bbox = (process['arguments']['spatial_extent']['west'], process['arguments']['spatial_extent']['south'],\
                process['arguments']['spatial_extent']['east'], process['arguments']['spatial_extent']['north'])
        if 'crs' in process['arguments']['spatial_extent'].keys():
            crs_value = process['arguments']['spatial_extent']['crs']
        else:
            crs_value = 'EPSG:4326'
        dict_item = {'name': 'crop', 'bbox': bbox, 'crs': crs_value}
        dict_item_list.append(dict_item)

    return dict_item_list
    

#def map_reduce(process, reducer_name, reducer_dimension):
def map_reduce(process):
    """
    Reduce(self, f_input, dimension='time', per_file=False, in_memory=False):
    """
    
    if 'f_input' in process.keys():
        per_file = None
        if 'per_file' in process['f_input']:
            per_file = process['f_input'].pop('per_file')
        dict_item = {
            'name': 'reduce',
            'dimension': process['reducer_dimension'],
            'f_input': process['f_input']
            }
        if per_file:
            dict_item['per_file'] = per_file
    else:
        # Add saving to vrt, else no vrt file is generated
        dict_item = map_save_result(process, delete_vrt=False, format_type='vrt')[0]

    return [dict_item]
    

def map_apply(process):
    """
    Reduce(self, f_input, dimension='time', per_file=False, in_memory=False):
    """    
    
    dict_item_list = [
                {'name': 'apply',
                'f_input': {'f_name': 'eo_' + process['reducer_name']} # TODO change name, reducer is confusing here
                }
                ]

    return dict_item_list
    
    
def map_save_result(process, delete_vrt=False, format_type = None, band_label=None):
    """

    """
    
    dict_item = {
        'name': 'save_raster',
        }
    #
    if delete_vrt:
        dict_item['delete_vrt'] = 'True;bool'
    # Add format type
    if 'format_type' in process.keys():
        dict_item['format_type'] = process['arguments']['format']
    elif format_type:
        dict_item['format_type'] = format_type
    # Add band_label of band(s) to save
    if band_label:
        dict_item['band_label'] = band_label

    return [dict_item]


def csw_query(collection, spatial_extent, temporal_extent):
    """
    Retrieves a file list from the EODC CSW server according to the specified parameters.

    """

    csw = CatalogueServiceWeb(environ.get('CSW_SERVER'), timeout=300)
    constraints = []

    # Collection filter
    constraints.append(PropertyIsLike('apiso:ParentIdentifier', collection))
    # Spatial filter
    constraints.append(BBox(spatial_extent))
    # Temporal filter
    constraints.append(PropertyIsGreaterThan('apiso:TempExtent_begin', temporal_extent[0]))
    constraints.append(PropertyIsLessThan('apiso:TempExtent_end', temporal_extent[1]))

    # Run the query
    constraints = [constraints]
    csw.getrecords2(constraints=constraints, maxrecords=100)

    # Put found records in a variable (dictionary)
    records0 = csw.records

    # Put statistics about results in a variable
    #results = csw.results

    # Sort records
    records = []
    for record in records0:
        records.append(records0[record].references[0]['url'])
    records = sorted(records)

    return records
