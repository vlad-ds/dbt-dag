# dbt-dag

This library addresses a current limitation of dbt: the inability to expose the workflow DAG for analysis and testing. Accessing the DBT dag provides several advantages:

* Visualize the dbt DAG with any tool, not just `dbt docs`. 
* Generate Airflow DAGs matchig the structure of the dbt DAG. 
* Run tests on the dbt graph logic e.g. "every model has at least 3 tests" or "no staging model can reference a mart model" 
* Integrate the dbt DAG with other metadata and lineage tools. 

The DBT dag is reconstructed from the `manifest.json` file and exposed as a [NetworkX DiGraph](https://networkx.org/documentation/stable/reference/classes/digraph.html). We don't interfere with dbt internals to get the graph. NetworkX provides a rich and intuitive interface for dealing with graphs. We also provide some high-level methods on top of the NetworkX library. 

The `manifest.json` file can be created and updated by running `dbt compile`, which does not run any models or incur any expense. 

The user has the responsibility of ensuring that `manifest.json` is up to date. 
