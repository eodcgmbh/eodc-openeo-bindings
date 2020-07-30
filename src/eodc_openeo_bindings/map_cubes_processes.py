"""

"""

from os import environ
from owslib.csw import CatalogueServiceWeb
from owslib.fes import PropertyIsLike, BBox, PropertyIsLessThan, PropertyIsGreaterThan, PropertyIsEqualTo


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
        process['arguments']['extent'] = process['arguments']['spatial_extent']
        dict_item = map_filter_bbox(process)[0]
        dict_item_list.append(dict_item)

    return dict_item_list, filepaths
    

def map_filter_bands(process):
    """

    """

    dict_item_list = []

    if 'bands' in process['arguments'].keys():
        load_bands = process['arguments']['bands']
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

    if 'extent' in process['arguments'].keys():
        bbox = (process['arguments']['extent']['west'], process['arguments']['extent']['south'],\
                process['arguments']['extent']['east'], process['arguments']['extent']['north'])
        if 'crs' in process['arguments']['extent'].keys():
            crs_value = process['arguments']['extent']['crs']
        else:
            crs_value = 'EPSG:4326'
        dict_item = {'name': 'crop', 'extent': bbox, 'crs': crs_value}
        dict_item_list.append(dict_item)

    return dict_item_list
    

def map_reduce_dimension(process):
    """
    Reduce(self, f_input, dimension='time'):
    """
    
    if 'f_input' in process:
        dict_item = {
            'name': 'reduce',
            'dimension': process['wrapper_dimension'],
            'f_input': process['f_input']
            }
    else:
        if process['wrapper_name'] == 'run_udf':
            format_type = 'Gtiff'
        else:
            format_type = 'VRT'
        # Add saving to vrt, else no vrt file is generated
        dict_item = map_save_result(process, in_place=False, format_type=format_type)[0]

    return [dict_item]
    

def map_apply(process):
    """
    Reduce(self, f_input, dimension='time'):
    """    
    
    if 'f_input' in process:
        dict_item = {
            'name': 'apply', 
            'f_input': process['f_input']
            }
    else:
        # Add saving to vrt, else no vrt file is generated
        dict_item = map_save_result(process, in_place=False, format_type='VRT')[0]

    return [dict_item]
    
    
def map_save_result(process, in_place=False, format_type = None, band_label=None):
    """

    """
    
    if 'options' in process['arguments']:
        bands = []
        for item in process['arguments']['options']:
            bands.append(process['arguments']['options'][item])
        dict_item = {
            'name': 'create_composite',
            'bands': bands,
            'format_type': process['arguments']['format']
        }
    else:
        dict_item = {
            'name': 'save_raster'
            }
        #
        if in_place:
            dict_item['in_place'] = 'True;bool'
        # Add format type
        if 'format_type' in process.keys():
            dict_item['format_type'] = process['arguments']['format']
        elif format_type:
            dict_item['format_type'] = format_type

    return [dict_item]


def map_merge_cubes(process):
    """
    
    """
    
    # intentionally empty, just for clarity
    # the only thing needed for this process is to create a new pickled object from the input ones, already mapped by other functions in map_processes.py
    
    return []


def map_rename_labels(process):
    """
    
    """
    
    # TODO this should be done once in openeo_to_eodatareaders for all processes dealing with dimensions 
    process['arguments']['dimension'] = check_dim_name(process['arguments']['dimension'])
        
    dict_item_list = [
        {
            'name': 'rename_labels', 
            'dim_name': process['arguments']['dimension'] + ';str', 
            'new_labels': str(process['arguments']['target']) + ';list',
            'old_labels': str(process['arguments']['source']) + ';list' if 'source' in process['arguments'] else '[];list'
        },
        map_save_result(process, in_place=True, format_type='VRT')[0]  # add saving to vrt, else no vrt file is generated
    ]
    
    return dict_item_list


def map_add_dimension(process):
    """
    
    """
    
    process['arguments']['name'] = check_dim_name(process['arguments']['name'])
    
    # Check if label is str or float
    if isinstance(process['arguments']['label'], str):
        label = process['arguments']['label'] + ';str'
    elif isinstance(process['arguments']['label'], int):
        label = str(process['arguments']['label']) + ';int'
    elif isinstance(process['arguments']['label'], float):
        label = str(process['arguments']['label']) + ';float'
    else:
        raise f"Data type for variable {process['arguments']['label']} not understood."
    
    dict_item_list = [
        {
            'name': 'add_dimension', 
            'dim_name': process['arguments']['name'] + ';str',
            'label':  label,
            'dim_type': process['arguments']['type'] + ';str' if 'type' in process['arguments'] else 'other;str',
        }
    ]
    
    return dict_item_list


def csw_query(collection, spatial_extent, temporal_extent):
    """
    Retrieves a file list from the EODC CSW server according to the specified parameters.

    """

    if collection == 'SIG0':
        csw = CatalogueServiceWeb(environ.get('ACUBE_CSW_SERVER'), timeout=300)
    else:
        csw = CatalogueServiceWeb(environ.get('CSW_SERVER'), timeout=300)
    constraints = []

    # Collection filter
    if collection == 'SIG0':
        constraints.append(PropertyIsEqualTo('eodc:variable_name', collection))
    else:
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


def check_dim_name(dimension_name):
    """
    Map common dimension names for spectral and time to fieladnames used in eodatareaders.
    """
    
    if dimension_name in ('spectral', 'spectral_bands', 'bands'):
        dimension_out_name = 'band'
    elif dimension_name in ('temporal', 'time', 't'):
        dimension_out_name = 'time'
    else:
        dimension_out_name = dimension_name
        
    return dimension_out_name
