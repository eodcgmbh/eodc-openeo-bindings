"""

"""

from openeo_pg_parser_python.translate_process_graph import translate_graph
from eodc_openeo_bindings.map_processes import map_process
from eodc_openeo_bindings.map_udf import map_udf
from copy import deepcopy


def openeo_to_eodatareaders(process_graph_json_in, job_data, vrt_only=False, existing_node_ids=None):
    """
    
    """
    
    if isinstance(process_graph_json_in, dict):
        process_graph_json = deepcopy(process_graph_json_in)
    else:
        process_graph_json = process_graph_json_in
    graph = translate_graph(process_graph_json)
    nodes = []
    for node_id in graph.nodes:            
        # Check if this node contains a callback
        reducer_name = None
        reducer_dimension = None
        node_dependencies = None
        if 'reducer' in graph.nodes[node_id].graph['arguments'].keys():
            if 'callback'in graph.nodes[node_id].graph['arguments']['reducer'].keys():
                callback_pg = graph.nodes[node_id].graph['arguments']['reducer']['callback']
                if 'process_id' in callback_pg:
                    # Callback is using an existing process
                    reducer_name = graph.nodes[graph.nodes[node_id].graph['arguments']['reducer']['from_node']].graph['process_id']
                    reducer_dimension = graph.nodes[node_id].graph['arguments']['dimension']
            elif 'from_node' in graph.nodes[node_id].graph['arguments']['reducer'].keys():
                # Callback is itself a process graph
                node_dependencies = [graph.nodes[node_id].graph['arguments']['reducer']['from_node']]
        
        if graph.nodes[node_id].graph['process_id'] == "reduce":
            reducer_name = graph.nodes[graph.nodes[node_id].graph['arguments']['reducer']['from_node']].graph['process_id']
            reducer_dimension = graph.nodes[node_id].graph['arguments']['dimension']
        
        # Convert openeo process to eoDataReaders syntax
        # Check if this node comes from a reduce node
        else:
            for node_edge in graph.nodes[node_id].edges:
                # Pass dimension paramer to children of callback
                if node_edge.node_ids[0] == node_id and node_edge.name == 'callback':
                    parent_node_graph = graph.nodes[node_edge.node_ids[1]].graph
                    if 'dimension' in parent_node_graph['arguments'].keys():
                        reducer_dimension = parent_node_graph['arguments']['dimension']
                        reducer_name = graph.nodes[node_id].graph['process_id']
        
        # TODO: dimension names should be available to users via dube metadata
        if reducer_dimension:
            if reducer_dimension in ('spectral', 'spectral_bands', 'bands'):
                reducer_dimension = 'band'
            if reducer_dimension in ('temporal', 'time'):
                reducer_dimension = 'time'
        
        operator = "eoDataReader"
        udf_exists = False
        if graph.nodes[node_id].graph['process_id'] == 'run_udf':
            udf_exists = True
            operator = "UdfExec"
            params = map_udf(graph.nodes[node_id].graph, job_data, node_id)
            filepaths = None
        else:
            params, filepaths = map_process(
                                            graph.nodes[node_id].graph,
                                            graph.nodes[node_id].name,
                                            graph.nodes[node_id].id,
                                            job_data,
                                            reducer_name=reducer_name,
                                            reducer_dimension=reducer_dimension,
                                            vrt_only=vrt_only
                                            )
        # Get node dependencies
        if not node_dependencies and graph.nodes[node_id].dependencies:
            node_dependencies = []
            for dependency in graph.nodes[node_id].dependencies:
                if 'callback' not in dependency.id:
                    node_dependencies.append(dependency.id)
        
        # Add to nodes list
        final_node_id = graph.nodes[node_id].id
        if existing_node_ids:
            for existing_node_id in existing_node_ids:
                if graph.nodes[node_id].id.split('_')[0] == existing_node_id.split('_')[0]:
                    final_node_id = existing_node_id
        nodes.append((final_node_id, params, filepaths, node_dependencies, operator))
        
    return nodes, graph
