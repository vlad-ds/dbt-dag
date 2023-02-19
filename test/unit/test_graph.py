import unittest

from dbt_dag import DbtNode, DbtDag

dag = DbtDag(manifest_path="test/fixtures/jaffle_shop/manifest.json")

class TestGraphBuild(unittest.TestCase):
    def test_graph(self):
        pass

        self.assertEqual()



# assert len(dag.graph.nodes) == 28