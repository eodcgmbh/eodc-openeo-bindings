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

    if isinstance(process_graph_json_in, dict):
        process_graph_json = deepcopy(process_graph_json_in)
    else:
        process_graph_json = process_graph_json_in
    graph = translate_process_graph(process_graph_json).sort(by='dependency')

    nodes = []
    for cur_node in graph.nodes:
        # Check if this node contains a callback
        reducer_name = None
        reducer_dimension = None
        node_dependencies = None

        if 'reducer' in cur_node.content['arguments'].keys():
            cur_reducer = cur_node.content['arguments']['reducer']

            # Callback is using an existing process
            if 'callback' in cur_reducer.keys() and 'process_id' in cur_reducer['callback']:
                # NB This block of code seems unused, also 'callback' is not supported an more by API v1.0
                reducer_name = graph[cur_reducer['from_node']].content['process_id']
                reducer_dimension = cur_node.content['arguments']['dimension']

            # Callback is itself a process graph
            elif 'from_node' in cur_reducer.keys():
                node_dependencies = [cur_reducer['from_node']]
                if cur_node.content['process_id'] == "reduce":
                    reducer_name = graph[cur_reducer['from_node']].content['process_id']
                    reducer_dimension = cur_node.content['arguments']['dimension']

            if cur_node.content['process_id'] == "reduce":
                if 'from_node' in cur_reducer.keys():
                    reducer_name = graph[cur_reducer['from_node']].content['process_id']
                    reducer_dimension = cur_node.content['arguments']['dimension']
                else:
                    # NB This is needed for UDFs, currently usable only from within a reduce call
                    reducer_name = cur_reducer['callback']['udf']['process_id']
                    reducer_dimension = cur_node.content['arguments']['dimension']

        # Convert OpenEO process to eoDataReaders syntax
        # Check if this node comes from a reduce node
        else:
            for node_edge in cur_node.edges:
                # Pass dimension parameter to children of callback
                if node_edge.node_ids[0] == cur_node.id and node_edge.name == 'callback':
                    parent_node_graph = graph[node_edge.node_ids[1]].content
                    if 'dimension' in parent_node_graph['arguments'].keys():
                        reducer_dimension = parent_node_graph['arguments']['dimension']
                        reducer_name = cur_node.content['process_id']

        # TODO: dimension names should be available to users via dube metadata
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
                cur_node.name,
                cur_node.id,
                job_data,
                reducer_name=reducer_name,
                reducer_dimension=reducer_dimension,
                vrt_only=vrt_only,
            )
        # Get node dependencies
        if not node_dependencies and cur_node.dependencies:
            node_dependencies = []
            for dependency_node in cur_node.dependencies.nodes:
                if 'callback' not in dependency_node.id:
                    node_dependencies.append(dependency_node.id)

        # Add to nodes list
        nodes.append((cur_node.id, params, filepaths, node_dependencies, operator))
    
    # Update the out_dirpath of the last node, to save data in a default "result" folder
    # NB: this will need to be changed with the newer version of the v1.0 parser
    nodes[-1][1][0]['out_dirpath'] = nodes[-1][1][0]['out_dirpath'].replace(nodes[-1][0], 'result')

    return nodes, graph
