from dagster import Definitions, define_asset_job, AssetSelection, AssetExecutionContext, with_resources, ScheduleDefinition
from dagster_dbt import DbtCliResource, dbt_assets
from dagster_airbyte import AirbyteResource, build_airbyte_assets

from .constants import dbt_manifest_path, dbt

##############################
#### ===>>>   dbt   <<<=== ###
##############################

@dbt_assets(manifest=dbt_manifest_path)
def dbt_visits_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

###############################
### ===>>>  airbyte  <<<=== ###
###############################

airbyte_resource = AirbyteResource(
    host="localhost",
    port="8000",
    username="airbyte",
    password="password",
)

# Use the airbyte_instance resource we define
airbyte_assets = with_resources(
    build_airbyte_assets(
        connection_id='5c4bb74c-3634-40d5-aaa5-bf3664868a10', #Copied from the url of the connection
        destination_tables=[
            'patient_language',
            'comprehensive_encounter',
            'comprehensive_encounter_map',
            'facility',
            'patient_diagnosis',
            'patient_disability',
            'patient_ethnicity',
            'patient_language',
            'patient_marital',
            'patient_race',
            'patient_visit',
            'patient_visit_details',
            'patient_visit_pds_care_provider',
            ],
        asset_key_prefix=['visits'], # must match the source name in dbt located in .yml file
        group_name='airbyte_group',
    ),
    {'airbyte':airbyte_resource}
)

##############################
#### ===>>>   job   <<<=== ###
##############################

everything_job = define_asset_job(
    name="everything_job",
    selection=AssetSelection.groups(
        'airbyte_group',
        'dbt_base_mysql', 
    )
)

####################################
#### ===>>>   schedules   <<<=== ###
####################################

daily_schedule = ScheduleDefinition(
    name="daily_schedule",
    cron_schedule="@daily",
    job=everything_job,
    execution_timezone="US/Mountain"
)

###############################################
#### ===>>>   putt it all together   <<<=== ###
###############################################

defs = Definitions(
    assets=airbyte_assets+[dbt_visits_dbt_assets],
    jobs=[everything_job],
    schedules=[daily_schedule],
    resources={
        "dbt": dbt,
    },
)