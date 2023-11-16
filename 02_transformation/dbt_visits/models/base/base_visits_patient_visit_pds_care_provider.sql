SELECT 
    deleted_on,
    created_on,
    care_provider_id,
    patient_visit_id,
    deleted_by,
    id,
    created_by,
    data_source,
    `_airbyte_ab_id`,
    `_airbyte_emitted_at`,
    `_airbyte_normalized_at`,
    `_airbyte_patient_vis___care_provider_hashid`
FROM {{ source('visits', 'patient_visit_pds_care_provider') }}