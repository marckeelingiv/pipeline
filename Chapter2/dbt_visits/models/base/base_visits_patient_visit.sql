SELECT 
    admit_date,
    account_number,
    major_class,
    discharge_date,
    sensitive_categories,
    visit_type,
    discharge_disposition,
    transfer_date,
    data_source,
    created_on,
    patient_id,
    facility_id,
    id,
    billing_account_number,
    `_airbyte_ab_id`,
    `_airbyte_emitted_at`,
    `_airbyte_normalized_at`,
    `_airbyte_patient_visit_hashid`
FROM {{ source('visits', 'patient_visit') }}