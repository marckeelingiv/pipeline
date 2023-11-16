{%- macro visits_joined_column_macro(target_table, prefix) -%}
   {#- prefixes all columns in target_table -#}
  {%- set cols = adapter.get_columns_in_relation(ref(target_table)) -%}
  SELECT
  {%- for col in cols %}
    {%- if col not in ['_airbyte_ab_id','_airbyte_emitted_at','_airbyte_normalized_at'] %}
      {{target_table}}_temp.{{ col.name }} AS {{prefix}}_{{col.name}}{% if not loop.last %},{% endif %}
      
    {%- endif -%}
  {%- endfor %}
  FROM {{ ref(target_table) }} AS {{target_table}}_temp
{%- endmacro -%}