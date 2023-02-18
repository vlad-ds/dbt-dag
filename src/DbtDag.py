import json

import networkx as nx


class DbtDag:
    def __init__(self,
                manifest_path: str = None,
                manifest_dict: dict = None):

        self.manifest = None

        if manifest_dict:
            self.manifest = manifest_dict
        elif manifest_path:
            with open(manifest_path) as file:
                self.manifest = json.load(file)
        else:
            raise Exception("No manifest provided.")


ddag = DbtDag(manifest_path="examples/jaffle_shop/manifest.json")

