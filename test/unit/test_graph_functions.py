from DbtDag import DbtNode, DbtDag

ddag = DbtDag(manifest_path="test/fixtures/jaffle_shop/manifest.json")

assert len(ddag.graph.nodes) == 28