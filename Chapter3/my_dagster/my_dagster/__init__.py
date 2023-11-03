from typing import Any, Mapping
from pathlib import Path
from dagster import Definitions, load_assets_from_modules
from dagster_airbyte import load_assets_from_airbyte_instance, AirbyteResource
from dagster import (
    ScheduleDefinition,
    Definitions,
    define_asset_job,
    AssetExecutionContext,
    AssetKey
)
from dagster_dbt import dbt_assets, DbtCliResource, build_schedule_from_dbt_selection, DagsterDbtTranslator

##############################
#### ===>>>   AirByte   <<<=== ###
##############################

airbyte_resource = AirbyteResource(
    host="localhost",
    port="8000",
    username="airbyte",
    password="password",
)

# Use the airbyte_instance resource we define
airbyte_assets = load_assets_from_airbyte_instance(airbyte_resource)

# materialize all assets
run_everything_job = define_asset_job("run_everything", selection="*")

airbyte_schedule = ScheduleDefinition(
    job=run_everything_job,
    cron_schedule="@daily"
)



##############################
#### ===>>>   dbt   <<<=== ###
##############################

# https://github.com/dagster-io/dagster/blob/master/examples/assets_dbt_python/assets_dbt_python/assets/dbt/__init__.py
DBT_PROJECT_DIR='C:\\Users\\keelim\\dev\\sandbox\\pipeline\\Chapter2\\dbt_visits'
dbt_resource = DbtCliResource(
    project_dir=DBT_PROJECT_DIR,
    profiles_dir=DBT_PROJECT_DIR
    )
dbt_parse_invocation = dbt_resource.cli(["parse"]).wait()
# dbt_manifest_path = dbt_parse_invocation.target_path.joinpath("manifest.json")

class CustomDagsterDbtTranslator(DagsterDbtTranslator):
    @classmethod
    def get_asset_key(cls, dbt_resource_props: Mapping[str, Any]) -> AssetKey:
        asset_key = super().get_asset_key(dbt_resource_props)
        return asset_key

@dbt_assets(
    manifest=Path(DBT_PROJECT_DIR)/'target'/'manifest.json',
    # dagster_dbt_translator=CustomDagsterDbtTranslator()
)
def dbt_project_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(['build'], context=context).stream()

daily_dbt_assets_schedule = build_schedule_from_dbt_selection(
    [dbt_project_assets],
    job_name="daily_dbt_models",
    cron_schedule="@daily",
)

all_assets = load_assets_from_modules([airbyte_assets])

defs = Definitions(
    assets=[
        airbyte_assets,
        dbt_project_assets
    ],
    jobs=[
        run_everything_job
    ],
    schedules=[
        airbyte_schedule,
        daily_dbt_assets_schedule
    ],
    resources={"dbt": dbt_resource,}
)