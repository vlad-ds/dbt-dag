from src.DbtDag import DbtNode, DbtDag

ddag = DbtDag(manifest_path="examples/jaffle_shop/manifest.json")
node_id = ddag.build_node_id("customers")
pred = ddag.get_predecessors(node_id)
suc = ddag.get_successors(node_id)