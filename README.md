# pipeline

# Introduction
- What is Data Engineering?
- Why is it needed?
- Two types of data engineers (A & B)

# Chapter 1 (Data Generation and Transfer)
1. Set up Environment 
    - python -m venv ./env
    - .\env\Scripts\Activate.ps1
    - python -m pip install -r .\requirements.txt
2. Turn on MySQL (3306), ClickHouse (8123), Airbyte (8000) (start generating data)
    - python .\01_data_generation\data_gen_and_seed.py (then wait for 5 min)
    - docker compose -f .\00_infrastructure\DockerCompose.yaml up -d
    - docker compose -f .\00_infrastructure\airbyte\DockerCompose_airbyte.yaml up -d
3. Show [Relational Diagram](./Table%20Structure.drawio)
4. Show how the data is generated 
    - [01_data_generation/DataGenClasses.py](./01_data_generation/DataGenClasses.py)
    - [01_data_generation/data_gen_and_seed.py](./01_data_generation/data_gen_and_seed.py)
5. Show data in source (connect to mysql using dbeaver)
6. Create connection from Mysql to ClickHouse through Airbyte
    1. Talk About Enable binary logging on mysql
    2. describe what airbyte is
    2. describe what ClickHouse is

# Chapter 2 (Organizing the Data)
1. create the dbt repo shown in [02_transformation](./02_transformation/)
    - dbt --version
    - dbt init dbt_visits
    - create sources.yml file
    - create profiles.yaml file
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
    - dagster project scaffold-code-location --name my_dagster
1. Connect Airbyte to Dagster
    - Create an airbyte resource (https://docs.dagster.io/concepts/resources)
    - `pip install -e ".[dev]"` `dagster dev`
    - run dagster `dagster dev`
2. Connect DBT to Dagster
3. Set up report delivery schedules
4. Set up Alerting


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