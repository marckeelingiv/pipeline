# pipeline

# Introduction
- What is Data Engineering?
- Why is it needed?
- Two types of data engineers (A & B)

# Chapter 1 (Data Generation and Transfer)
1. Set up Environment 
    - `python -m venv ./env`
    - `.\env\Scripts\Activate.ps1`
    - `python.exe -m pip install --upgrade pip`
    - `python -m pip install -r .\requirements.txt`
2. Turn on MySQL (3306), ClickHouse (8123), Airbyte (8000) (start generating data)
    - docker compose -f .\00_infrastructure\DockerCompose.yaml up -d
    - go into data generation folder `cd .\01_data_generation`
    - run the python script to seed the data `python -m data_gen_and_seed` (then wait for 5 min)
    - docker compose -f .\00_infrastructure\airbyte\DockerCompose_airbyte.yaml up -d
3. Show [Relational Diagram](./Table%20Structure.drawio)
4. Show how the data is generated 
    - [01_data_generation/DataGenClasses.py](./01_data_generation/DataGenClasses.py)
    - [01_data_generation/data_gen_and_seed.py](./01_data_generation/data_gen_and_seed.py)
5. Show data in source (connect to mysql using dbeaver)
6. Create connection from Mysql to ClickHouse through Airbyte
    1. login to airbyte localhost:800 username: airbyte password: password
        - create database on clickhouse: `CREATE DATABASE mysql_extracts;`
        - make sure to land data in new schema called `mysql_extracts` in clickhouse
    2. Talk About Enable binary logging on mysql
    3. describe what airbyte is
    4. describe what ClickHouse is

# Chapter 2 (Organizing the Data)
1. create the dbt repo shown in [02_transformation](./02_transformation/)
    - `dbt --version`
    - `dbt init dbt_visits`
    - create profiles.yaml file
    - create sources.yml file
    - dbt debug
    - create base and intermediate folders
2. dbt models
    - create models
    - show documentation
    - patient attributes model (v1 & v2)
    - visits joined (v1 & v2)
3. dbt tests
    - what are they
    - quick demo


# Chapter 3 (Orchestration)
1. Create Dagster environment
    - `dagster project scaffold-code-location --name my_dagster`
1. Connect Airbyte to Dagster
    - `pip install -e ".[dev]"`
    - run dagster `$env:DAGSTER_DBT_PARSE_PROJECT_ON_LOAD = "1"; dagster dev`
    - Create an airbyte resource (https://docs.dagster.io/concepts/resources & https://docs.dagster.io/integrations/airbyte#using-airbyte-with-dagster)
4. Set up report delivery schedules
5. Set up Alerting


# Things not shown here
- Working with people you have no control over to communicate the vision and convince to give you the permissions needed to execute 
- Working with Data Science to figure out what data is important to them
- How to Secure your connections and data
- How to deploy to production

# Possible Changes/Improvements
- Swap out ClickHouse for DuckDB
- Improve dates in fake data
- Set up notifications of failure

# Link To Video Demo
[Data Pipeline Implementation at Big Mountain Data and Dev Conference](https://youtu.be/coycGADJ5CQ)