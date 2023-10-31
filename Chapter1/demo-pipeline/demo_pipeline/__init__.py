from dagster import Definitions, load_assets_from_modules
from .sensors import gen_records_sensor

from . import assets

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    sensors= [gen_records_sensor]
)
