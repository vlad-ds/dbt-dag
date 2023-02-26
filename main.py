from dbt_dag.DbtDag import DbtNode, DbtDag

dag = DbtDag(manifest_path="examples/jaffle_shop/manifest.json")
node_id = dag.build_node_id("customers")
#
# pred = ddag.get_predecessors(node_id, max_depth=999)