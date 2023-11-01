# pipeline

## Introduction
- What is Data Engineering?
- Why is it needed?
- Two types of data engineers (A & B)

## Chapter 1 (Data Generation and Transfer)
1. Turn on MySQL, ClickHouse, Airbyte (start generating data)
    - airbyte on 8000
2. Show Relational Diagram
3. Show how the data is generated
4. Show data in source
5. Create connection from Mysql to ClickHouse through Airbyte
    1. Enable binary logging on mysql
    1. describe aht airbyte is
    2. describe what ClickHouse is 

## Chapter 2 (Organizing the Data)
1. dbt models
    - dbt --version
    - dbt init dbt_visits
    - create models
    - add profiles.yaml
    - dbt debug
    - patient attributes model (v1 & v2)
    - visits joined (v1 & v2)
2. dbt tests
    - what are they
    - quick demo


## Chapter 3 (Orchestration)
1. Connect Airbyte to Dagster
    - Create an airbyte resource (https://docs.dagster.io/concepts/resources)
    - `pip install -e ".[dev]"` `dagster dev`
2. Connect DBT to Dagster
3. Set up report delivery schedules
4. Set up Alerting


## Things not shown here
- Working with people you have no control over to communicate the vision and convince to give you the permissions needed to execute 
- Working with Data Science to figure out what data is important to them
- How to Secure your connections and data
- How to deploy to production

## possible changes/improvements
- Swap out ClickHouse for DuckDB