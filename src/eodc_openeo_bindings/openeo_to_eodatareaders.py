"""

"""
from copy import deepcopy
from typing import Union, List, Tuple, Optional

from eodc_openeo_bindings.map_processes import map_process
from eodc_openeo_bindings.map_udf import map_udf
from openeo_pg_parser_python.graph import Graph
from openeo_pg_parser_python.translate import translate_process_graph


def openeo_to_eodatareaders(process_graph_json_in: Union[dict, str], job_data: str, 
                            process_defs: Union[dict, list, str], vrt_only: bool = False,
                            existing_node_ids: List[Tuple] = None) \
        -> Tuple[List[Tuple[str, List[str], Optional[str], List[str], str]], Graph]:
    """
    This function translates an OpenEO process graph into a sequence of calls to eoDataReaders, 
    one for each node of the process graph.
    Each openEO process is wrapped into an apply/reduce call using eoDataReaders methods.

    """
    
    # TODO make process_defs and job_data env variables

    if isinstance(process_graph_json_in, dict):
        process_graph_json = deepcopy(process_graph_json_in)
    else:
        process_graph_json = process_graph_json_in
    # TODO process_defs must be defined from the outer functions using openeo_to_eodatareaders
    # this way an application can send a url, list or foldername
    graph = translate_process_graph(process_graph_json, process_defs=process_defs).sort(by='dependency')
    
    wrapper_processes = get_wrapper_processes()
    
    nodes = []
    for node_id in graph.ids:
        cur_node = graph[node_id]
        wrapper_name = None
        wrapper_dimension = None
        node_dependencies = None            
        
        if cur_node.is_reducer:
            # Current process is classified as "reducer" in its process definition
            if cur_node.parent_process:
                # Current process has parent, must be an embedded process graph
                wrapper_name = cur_node.parent_process.process_id
                wrapper_dimension = cur_node.parent_process.dimension
            else:
                # Current process is of type "reducer" but has no parent, must be one of these processes:
                # "reduce_dimension", "reduce_dimension_binary"
                wrapper_name = cur_node.process_id
                wrapper_dimension = cur_node.dimension
        else:
            wrapper_name = cur_node.process_id
            recuder_dimension = None # for clarity, this will be needed when also 'apply_dimension' is supported by eoDataReaders
        
        # Workaround for process "array_element" until it has the category "reducer" set
        # TODO remove when the process definition is updated
        if (not cur_node.is_reducer) and (cur_node.parent_process):
            # Current process has parent, must be an embedded process graph
            wrapper_name = cur_node.parent_process.process_id
            wrapper_dimension = cur_node.parent_process.dimension
        
        
        # NB find better solution
        if wrapper_dimension:
            if wrapper_dimension in ('spectral', 'spectral_bands', 'bands'):
                wrapper_dimension = 'band'
            if wrapper_dimension in ('temporal', 'time'):
                wrapper_dimension = 'time'
            
        if cur_node.content['process_id'] == 'run_udf':
            operator = "UdfExec"
            params = map_udf(cur_node.content, job_data, cur_node.id)
            filepaths = None
        else:
            operator = "eoDataReader"
            params, filepaths = map_process(
                cur_node.content,
                cur_node.id,
                job_data,
                wrapper_name=wrapper_name,
                wrapper_dimension=wrapper_dimension,
                vrt_only=vrt_only,
            )
        
        # Get dependencies
        if cur_node.result_process and (cur_node.process_id in wrapper_processes):
            # The current process is a wrapper process, which embeds a process graph
            # Its only dependency is the node in the embedded process graph with 'result' set to True.
            node_dependencies = [cur_node.result_process.id]
        else:
            node_dependencies = list(cur_node.dependencies.ids)
        
        # Add to nodes list
        nodes.append((cur_node.id, params, filepaths, node_dependencies, operator))
        
    # Update the out_dirpath of the last node, to save data in a default "result" folder
    # NB: this will need to be changed with the newer version of the v1.0 parser
    nodes[-1][1][0]['out_dirpath'] = nodes[-1][1][0]['out_dirpath'].replace(nodes[-1][0], 'result')
    
    return nodes, graph
    

def get_wrapper_processes():
    """
    Return openEO processes which are wrappers around other processes.
    Their dependencies are handles differently than for common processes.
    """
    
    
    return ('apply', 'reduce_dimension')
    
