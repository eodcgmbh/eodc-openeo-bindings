import json
from typing import List, Dict
from uuid import uuid4

import requests
from eodatareaders.eo_data_reader import eoDataReader


class UdfExec:

    def __init__(self, input_paths: List[str], params: Dict[str]):
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
            "data_id": uuid4(),
            "source": self.input_params["udf"],
            "language": self.input_params["runtime"]
        }
        reader = eoDataReader(self.input_paths)
        # TODO save information from eoDataReaders: proj, time, band, x- y-coord

    def create_json(self):
        # TODO distinction between different types
        self.input_json = self.create_hypercube()

    def create_hypercube(self):
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
                        "dimensions": [
                            {
                                "name": "time",
                                "coordinates": self.json_params["time"],
                            }, {
                                "name": "band",
                                "coordinates": self.json_params["bands"]
                            }, {
                                "name": "x",
                                "coordinates": self.json_params["x"],
                            }, {
                                "name": "y",
                                "coordinates": self.json_params["y"],
                            }
                        ],
                        "array": [1],
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
