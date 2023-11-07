SELECT 
    code,
    insert_id,
    last_seen,
    created_on AS create_datetime,
    patient_id,
    facility_id,
    id,
    created_by,
    data_source_id,
    `_airbyte_ab_id`,
    `_airbyte_emitted_at`,
    `_airbyte_normalized_at`,
    `_airbyte_patient_disability_hashid`
FROM {{ source('visits', 'patient_disability') }}