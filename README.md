# dbt-dag

This library addresses a current limitation of dbt: the inability to expose the workflow DAG for analysis and testing. Accessing the DBT dag would provide several advantages such as:

* Visualizing the DAG with any tool, not just `dbt docs`. 
* Generating Airflow DAGs from the dbt DAG. 
* Running tests on the workflow graph. 
* Integrating the information with other lineage tools. 

The DBT dag is reconstructed from the `manifest.json` file and exposed as a [NetworkX DiGraph](https://networkx.org/documentation/stable/reference/classes/digraph.html). Thus, we don't need to interfere with dbt's internals to get the graph. NetworkX provides a rich and convenient library for dealing with graphs. We also provide some high-level methods on top of the NetworkX library. 

The `manifest.json` file can be created and updated by running `dbt compile`, which does not run any models or incur any expense. The user has the responsibility of ensuring that `manifest.json` is up to date. 
