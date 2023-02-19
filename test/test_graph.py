import unittest

from dbt_dag.DbtDag import DbtNode, DbtDag
from fixtures.jaffle_shop.lineage_maps import ancestors, descendants


class TestGraphBuild(unittest.TestCase):
    def setUp(self) -> None:
        self.dag = DbtDag(manifest_path="fixtures/jaffle_shop/manifest.json")

    def test_graph_build(self):
        self.assertEqual(len(self.dag.graph.nodes), 28)
        self.assertEqual(len(self.dag.graph.edges), 29)


class TestGraphMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.dag = DbtDag(manifest_path="fixtures/jaffle_shop/manifest.json")

    def test_build_node_id(self):
        self.assertEqual(self.dag.build_node_id("customers"), "model.jaffle_shop.customers")
        self.assertEqual(self.dag.build_node_id("orders"), "model.jaffle_shop.orders")
        self.assertEqual(self.dag.build_node_id("raw_customers", "seed"), "seed.jaffle_shop.raw_customers")
        self.assertEqual(self.dag.build_node_id("customers", "seed"), "seed.jaffle_shop.customers")

    def test_get_node_from_id(self):
        ids = ["model.jaffle_shop.customers",
               "seed.jaffle_shop.raw_customers"]

        for id_ in ids:
            node = self.dag.get_node_from_id(id_)
            self.assertIsInstance(node, DbtNode)
            self.assertEqual(node.node_id, id_)

    def test_get_ancestors(self):
        for ancestor in ancestors:
            for depth, result in ancestors[ancestor].items():
                self.assertEqual(dict(self.dag.get_ancestors(ancestor, max_depth=depth)), result)
            max_depth = max(ancestors[ancestor].keys())
            max_depth_result = ancestors[ancestor][max_depth]
            self.assertEqual(dict(self.dag.get_ancestors(ancestor, max_depth=None)), max_depth_result)

    def test_get_descendants(self):
        for descendant in descendants:
            for depth, result in descendants[descendant].items():
                self.assertEqual(dict(self.dag.get_descendants(descendant, max_depth=depth)), result)
            max_depth = max(descendants[descendant].keys())
            max_depth_result = descendants[descendant][max_depth]
            self.assertEqual(dict(self.dag.get_descendants(descendant, max_depth=None)), max_depth_result)

