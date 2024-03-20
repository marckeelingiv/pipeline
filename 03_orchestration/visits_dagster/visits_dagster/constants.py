# This code was created from the below link
# https://docs.dagster.io/integrations/dbt/using-dbt-with-dagster/load-dbt-models#step-1-create-a-dagster-project-that-wraps-your-dbt-project
import os
from pathlib import Path

from dagster_dbt import DbtCliResource

dbt_project_dir = Path('..','..','dbt_visits').resolve()
dbt = DbtCliResource(project_dir=os.fspath(dbt_project_dir))

# If DAGSTER_DBT_PARSE_PROJECT_ON_LOAD is set, a manifest will be created at run time.
# Otherwise, we expect a manifest to be present in the project's target directory.
if os.getenv("DAGSTER_DBT_PARSE_PROJECT_ON_LOAD"):
    dbt_manifest_path = (
        dbt.cli(
            ["--quiet", "parse"],
            target_path=Path("target"),
        )
        .wait()
        .target_path.joinpath("manifest.json")
    )
else:
    dbt_manifest_path = dbt_project_dir.joinpath("target", "manifest.json")