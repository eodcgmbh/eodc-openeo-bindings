import os


def map_udf(process, root_folder, process_id):
    """
    
    """

    params = {
        "udf": process['arguments']['udf'],
        "runtime": process['arguments']['runtime'],
        "output_folder": os.path.join(root_folder, process_id)
    }
    
    return params
