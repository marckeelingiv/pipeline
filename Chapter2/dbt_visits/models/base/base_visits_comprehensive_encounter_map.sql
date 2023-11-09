SELECT 
    deleted_on,
    created_on,
    patient_visit_id,
    comprehensive_encounter_id,
    patient_id,
    is_sensitive,
    id,
    `_airbyte_ab_id`,
    `_airbyte_emitted_at`,
    `_airbyte_normalized_at`,
    `_airbyte_comprehensive_encounter_map_hashid`
FROM {{ source('visits','comprehensive_encounter_map') }}