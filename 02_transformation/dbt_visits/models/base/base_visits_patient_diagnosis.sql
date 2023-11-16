SELECT 
    code,
    created_on,
    patient_visit_id,
    patient_id,
    diagnosis_date,
    description,
    id,
    `type`,
    priority,
    created_by,
    data_source,
    `_airbyte_ab_id`,
    `_airbyte_emitted_at`,
    `_airbyte_normalized_at`,
    `_airbyte_patient_diagnosis_hashid`
FROM {{ source('visits', 'patient_diagnosis') }}