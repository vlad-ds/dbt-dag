import json

import networkx as nx


class DbtNode:
    def __init__(self,
                 full_name: str,
                 node_dict: dict):

        self.full_name = full_name
        parts = full_name.split(".")
        self.node_type = parts[0]
        self.dbt_project = parts[1]
        self.node_name = parts[2]
        self.run_id = parts[3] if len(parts) > 3 else None

        self.node_dict = node_dict

    def __hash__(self):
        return hash(self.full_name)

    def __str__(self):
        return self.full_name


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

    def populate(self):

        # add nodes
        for node_name, node_dict in self.manifest["nodes"].items():
            node_object = DbtNode(node_name, node_dict)
            self.graph.add_node(node_name, node_object=node_object)

        # add edges
        for node_name, children in self.manifest["child_map"].items():
            for child in children:
                self.graph.add_edge(node_name, child)


ddag = DbtDag(manifest_path="examples/jaffle_shop/manifest.json")
ddag.populate()