SELECT 
    admit_date,
    deleted_on,
    matching_method_identifier,
    created_on,
    matching_method,
    patient_id, 
    discharge_date,
    facility_id, 
    id,
    `type`,
    `_airbyte_ab_id`,
    `_airbyte_emitted_at`,
    `_airbyte_normalized_at`,
    `_airbyte_comprehensive_encounter_hashid`
FROM {{ source('visits','comprehensive_encounter') }}