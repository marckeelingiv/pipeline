from dagster import Definitions, load_assets_from_modules
from dagster_airbyte import load_assets_from_airbyte_instance, AirbyteResource
from dagster import (
    ScheduleDefinition,
    Definitions,
    define_asset_job,
)

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


all_assets = load_assets_from_modules([airbyte_assets])

defs = Definitions(
    assets=[
        airbyte_assets
    ],
    jobs=[
        run_everything_job
    ],
    schedules=[
        airbyte_schedule
    ],
)
