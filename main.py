from src.DbtDag import DbtNode, DbtDag
from networkx.algorithms.traversal.depth_first_search import dfs_successors, dfs_predecessors

ddag = DbtDag(manifest_path="examples/jaffle_shop/manifest.json")
ddag.populate()
node_id = ddag.build_node_id("customers")
pred = ddag.get_predecessors(node_id)
suc = ddag.get_successors(node_id)