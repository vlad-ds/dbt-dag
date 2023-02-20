# dbt-dag

This library addresses a current limitation of dbt: the inability to expose the workflow DAG for analysis and testing. Accessing the DBT dag would provide several advantages such as:

* Visualizing the DAG with any tool, not just `dbt docs`. 
* Generating Airflow DAGs from the dbt DAG. 
* Running tests on the workflow graph. 
* Integrating the information with other lineage tools. 

