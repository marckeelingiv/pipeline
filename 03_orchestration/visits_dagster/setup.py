from setuptools import find_packages, setup

setup(
    name="visits_dagster",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "dagster==1.6.11",
        "dagster-dbt==0.22.11",
        "dagster-airbyte==0.22.11",
        "dbt-clickhouse==1.7.3",
        "pyyaml==6.0.1",
    ],
    extras_require={
        "dev": [
            "dagster-webserver==1.6.11",
        ]
    },
)