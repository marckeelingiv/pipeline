{% set my_tables = [
  "base_visits_patient_disability",
  "base_visits_patient_ethnicity",
  "base_visits_patient_language",
  "base_visits_patient_marital",
  "base_visits_patient_race",
]%}
WITH 
{% for table in my_tables %}
cte_{{table}} AS (SELECT * FROM (SELECT
    patient_id,
    code,
    ROW_NUMBER() OVER (PARTITION BY patient_id ORDER BY create_datetime DESC) AS row_num
FROM {{ ref(table) }}
) AS temp_{{table}}
WHERE row_num = 1),
{%- endfor -%}
all_pids AS (
  SELECT DISTINCT patient_id FROM (
    {% for table in my_tables %}
      SELECT patient_id FROM cte_{{table}}
      {% if not loop.last %} UNION ALL{% endif -%}
    {% endfor %}
  )
),
all_attributes AS (
  SELECT
    all_pids.patient_id,
    {%- for table in my_tables -%}
      {% set last_underscore_index = table.rfind("_")+1 -%}
      {% set column_name = table[last_underscore_index:] %}
      cte_{{table}}.code AS {{column_name}}
      {%- if not loop.last %},{% endif -%}
    {%- endfor %}
  FROM all_pids
  {% for table in my_tables -%}
    LEFT JOIN cte_{{table}} ON cte_{{table}}.patient_id = all_pids.patient_id
  {% endfor -%}
)
SELECT * FROM all_attributes