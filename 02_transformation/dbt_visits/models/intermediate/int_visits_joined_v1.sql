SELECT
    pd.code AS `pvd_code`,
    pd.created_on AS `pvd_created_on`,
    pd.patient_visit_id AS `pvd_patient_visit_id`,
    pd.patient_id AS `pvd_patient_id`,
    pd.diagnosis_date AS `pvd_diagnosis_date`,
    pd.description AS `pvd_description`,
    pd.id AS `pvd_id`,
    pd.`type` AS `pvd_type`,
    pd.priority AS `pvd_priority`,
    pd.created_by AS `pvd_created_by`,
    pd.data_source AS `pvd_data_source`,
    pv.admit_date AS `pv_admit_date`,
    pv.account_number AS `pv_account_number`,
    pv.major_class AS `pv_major_class`,
    pv.discharge_date AS `pv_discharge_date`,
    pv.sensitive_categories AS `pv_sensitive_categories`,
    pv.visit_type AS `pv_visit_type`,
    pv.discharge_disposition AS `pv_discharge_disposition`,
    pv.transfer_date AS `pv_transfer_date`,
    pv.data_source AS `pv_data_source`,
    pv.created_on AS `pv_created_on`,
    pv.patient_id AS `pv_patient_id`,
    pv.facility_id AS `pv_facility_id`,
    pv.id AS `pv_id`,
    pv.billing_account_number AS `pv_billing_account_number`,
    pvd.discharge_disposition_raw AS `pvd_discharge_disposition_raw`,
    pvd.note AS `pvd_note`,
    pvd.presumed_discharge_date AS `pvd_presumed_discharge_date`,
    pvd.last_seen AS `pvd_last_seen`,
    pvd.location_label AS `pvd_location_label`,
    pvd.prior_patient_location AS `pvd_prior_patient_location`,
    pvd.admit_source_type AS `pvd_admit_source_type`,
    pvd.presumed_discharge_reason AS `pvd_presumed_discharge_reason`,
    pvd.attending_physician AS `pvd_attending_physician`,
    pvd.added_by AS `pvd_added_by`,
    pvd.location_raw AS `pvd_location_raw`,
    pvd.chief_complaint AS `pvd_chief_complaint`,
    pvd.note_privacy_level AS `pvd_note_privacy_level`,
    pvd.location AS `pvd_location`,
    pvd.discharge_diagnosis AS `pvd_discharge_diagnosis`,
    cem.deleted_on AS `cem_deleted_on`,
    cem.created_on AS `cem_created_on`,
    cem.patient_visit_id AS `cem_patient_visit_id`,
    cem.comprehensive_encounter_id AS `cem_comprehensive_encounter_id`,
    cem.patient_id AS `cem_patient_id`,
    cem.is_sensitive AS `cem_is_sensitive`,
    ce.admit_date AS `ce_admit_date`,
    ce.deleted_on AS `ce_deleted_on`,
    ce.matching_method_identifier AS `ce_matching_method_identifier`,
    ce.created_on AS `ce_created_on`,
    ce.matching_method AS `ce_matching_method`,
    ce.discharge_date AS `ce_discharge_date`,
    ce.id AS `ce_id`
FROM {{ ref('base_visits_patient_diagnosis') }} AS pd
LEFT JOIN {{ ref('base_visits_patient_visit') }} AS pv ON pv.id = pd.patient_visit_id
LEFT JOIN {{ ref('base_visits_patient_visit_details') }} AS pvd ON pvd.id = pv.id
LEFT JOIN {{ ref('base_visits_comprehensive_encounter_map') }} AS cem ON cem.patient_visit_id = pv.id
LEFT JOIN {{ ref('base_visits_comprehensive_encounter') }} AS ce ON ce.id = cem.comprehensive_encounter_id