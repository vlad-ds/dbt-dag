import json

import networkx as nx


class DbtDag:
    def __init__(self,
                 manifest_path: str = None,
                 manifest_dict: dict = None):

        self.manifest = None
        self.graph = nx.DiGraph()

        if manifest_dict:
            self.manifest = manifest_dict
        elif manifest_path:
            with open(manifest_path) as file:
                self.manifest = json.load(file)
        else:
            raise Exception("No manifest provided.")

    @property
    def dbt_schema_version(self):
        return self.manifest["metadata"]["dbt_schema_version"]


ddag = DbtDag(manifest_path="examples/jaffle_shop/manifest.json")
