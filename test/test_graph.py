import unittest

from dbt_dag.DbtDag import DbtNode, DbtDag

dag = DbtDag(manifest_path="fixtures/jaffle_shop/manifest.json")


class TestGraphBuild(unittest.TestCase):
    def test_graph_structure(self):
        self.assertEqual(len(dag.graph.nodes), 28)
