"""

"""
from copy import deepcopy
from typing import Union, List, Tuple, Optional

from eodc_openeo_bindings.map_processes import map_process
from eodc_openeo_bindings.map_udf import map_udf
from openeo_pg_parser_python.graph import Graph
from openeo_pg_parser_python.translate import translate_process_graph


def openeo_to_eodatareaders(process_graph_json_in: Union[dict, str], job_data: str, vrt_only: bool = False,
                            existing_node_ids: List[Tuple] = None) \
        -> Tuple[List[Tuple[str, List[str], Optional[str], List[str], str]], Graph]:
    """
    This method translates an OpenEO process graph into a list of nodes and a graph.

    """
    
    # TODO make process_defs and job_data env variables

    if isinstance(process_graph_json_in, dict):
        process_graph_json = deepcopy(process_graph_json_in)
    else:
        process_graph_json = process_graph_json_in
    # TODO process_defs must be defined from the outer functions using openeo_to_eodatareaders
    # this way an application can send a url, list or foldername
    graph = translate_process_graph(process_graph_json, process_defs="http://localhost:3000/v1.0/processes").sort(by='dependency')
    
    empty_processes = ('apply', 'apply_dimension', 'reduce_dimension', 'reduce_dimension_binary')
    
    nodes = []
    for node_id in graph.ids:
        cur_node = graph[node_id]
        reducer_name = None
        reducer_dimension = None
        node_dependencies = None
        
        # This approach will work if also array_element is flagged as a reducer
        if cur_node.is_reducer:
            # Current process is classified as "reducer" in process definition
            if cur_node.parent_process:
                # Current process has parent, must be an embedded process graph
                reducer_name = cur_node.parent_process.process_id
                reducer_dimension = cur_node.parent_process.dimension
            else:
                # Current process is of type "reducer" but has no parent, must be one of these processes:
                # "reduce_dimension", "reduce_dimension_binary"
                reducer_name = cur_node.process_id
                reducer_dimension = cur_node.dimension
        # TODO -> if not a reduce call, the process should be embedded into an "apply" call
        
        # Workaround for process "array_element" until it has the category "reducer" set
        # TODO remove when the process definition is updated
        if (not cur_node.is_reducer) and (cur_node.parent_process):
            # Current process has parent, must be an embedded process graph
            reducer_name = cur_node.parent_process.process_id
            reducer_dimension = cur_node.parent_process.dimension
        
        
        # NB find better solution
        if reducer_dimension:
            if reducer_dimension in ('spectral', 'spectral_bands', 'bands'):
                reducer_dimension = 'band'
            if reducer_dimension in ('temporal', 'time'):
                reducer_dimension = 'time'
            
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
                reducer_name=reducer_name,
                reducer_dimension=reducer_dimension,
                vrt_only=vrt_only,
            )
        
        # Get dependencies
        if cur_node.result_process and (cur_node.process_id in empty_processes):
            # The current process is a shell/empty process, which embeds a process graph
            # It only dependency is the node in the embedded process graph, where 'result' is set to True.
            node_dependencies = [cur_node.result_process.id]
        else:
            node_dependencies = list(cur_node.dependencies.ids)
        
        # Add to nodes list
        nodes.append((cur_node.id, params, filepaths, node_dependencies, operator))
        
    # Update the out_dirpath of the last node, to save data in a default "result" folder
    # NB: this will need to be changed with the newer version of the v1.0 parser
    nodes[-1][1][0]['out_dirpath'] = nodes[-1][1][0]['out_dirpath'].replace(nodes[-1][0], 'result')
    
    return nodes, graph
