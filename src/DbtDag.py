import json
from typing import Optional, List

import networkx as nx
from networkx.algorithms.traversal.depth_first_search import dfs_successors, dfs_predecessors


class DbtNode:
    def __init__(self,
                 node_id: str,
                 node_dict: dict):

        self.node_id = node_id
        parts = node_id.split(".")
        self.node_type = parts[0]
        self.dbt_project = parts[1]
        self.node_name = parts[2]
        self.run_id = parts[3] if len(parts) > 3 else None

        self.node_dict = node_dict

    def __hash__(self):
        return hash(self.node_id)

    def __str__(self):
        return self.node_id


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
    def dbt_schema_version(self) -> str:
        return self.manifest["metadata"]["dbt_schema_version"]

    @property
    def dbt_project(self) -> str:
        node = list(self.manifest["nodes"])[0]
        return node.split(".")[1]

    def get_node_from_id(self, node_id: str):
        if not node_id in self.graph.nodes:
            raise Exception("node_id not found")
        return self.graph.nodes[node_id]["node_object"]

    def build_node_id(self, node_name: str, node_type="model") -> str:
        return f"{node_type}.{self.dbt_project}.{node_name}"

    def get_predecessors(self, node_id: str) -> List[str]:
        if node_id not in self.graph.nodes:
            raise Exception("Node doesn't exist.")
        return list(self.graph.predecessors(node_id))

    def get_successors(self, node_id: str) -> List[str]:
        if node_id not in self.graph.nodes:
            raise Exception("Node doesn't exist.")
        return list(self.graph.successors(node_id))

    def populate(self):

        # add nodes
        for node_id, node_dict in self.manifest["nodes"].items():
            node_object = DbtNode(node_id, node_dict)
            self.graph.add_node(node_id, node_object=node_object)

        # add edges
        for node_id, children in self.manifest["child_map"].items():
            for child in children:
                self.graph.add_edge(node_id, child)