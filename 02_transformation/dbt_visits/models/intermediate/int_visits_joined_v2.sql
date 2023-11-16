WITH
pd AS (
    {{ visits_joined_column_macro('base_visits_patient_diagnosis','pd') }}
),
pv AS (
    {{ visits_joined_column_macro('base_visits_patient_visit','pv') }}
),
pvd AS (
    {{ visits_joined_column_macro('base_visits_patient_visit_details','pvd') }}
),
cem AS (
    {{ visits_joined_column_macro('base_visits_comprehensive_encounter_map','cem') }}
),
ce AS (
    {{ visits_joined_column_macro('base_visits_comprehensive_encounter','ce') }}
),
joined AS (
    SELECT
        *
    FROM pd
    LEFT JOIN pv ON pv_id = pd_patient_visit_id
    LEFT JOIN pvd ON pvd_id = pv_id
    LEFT JOIN cem ON cem_patient_visit_id = pv_id
    LEFT JOIN ce ON ce_id = cem_comprehensive_encounter_id
)
SELECT * FROM joined