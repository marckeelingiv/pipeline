WITH 
p_dis AS (
SELECT * FROM (SELECT
    patient_id,
    code,
    ROW_NUMBER() OVER (PARTITION BY patient_id ORDER BY create_datetime DESC) AS row_num
FROM {{ ref('base_visits_patient_disability') }}
)
WHERE row_num = 1
), 
p_eth AS (
SELECT * FROM (SELECT
    patient_id,
    code,
    ROW_NUMBER() OVER (PARTITION BY patient_id ORDER BY create_datetime DESC) AS row_num
FROM {{ ref('base_visits_patient_ethnicity') }}
) WHERE row_num = 1
),
p_lang AS (
SELECT * FROM (SELECT
    patient_id,
    code,
    ROW_NUMBER() OVER (PARTITION BY patient_id ORDER BY create_datetime DESC) AS row_num
FROM {{ ref('base_visits_patient_language') }}
) WHERE row_num = 1
),
p_mar AS (
SELECT * FROM (SELECT
    patient_id,
    code,
    ROW_NUMBER() OVER (PARTITION BY patient_id ORDER BY create_datetime DESC) AS row_num
FROM {{ ref('base_visits_patient_marital') }}
) WHERE row_num = 1
),
p_rac AS (
SELECT * FROM (SELECT
    patient_id,
    code,
    ROW_NUMBER() OVER (PARTITION BY patient_id ORDER BY create_datetime DESC) AS row_num
FROM {{ ref('base_visits_patient_race') }}
) WHERE row_num = 1
),
all_pids AS (
    SELECT DISTINCT patient_id FROM (
    SELECT patient_id FROM p_dis
    UNION ALL
    SELECT patient_id FROM p_eth
    UNION ALL
    SELECT patient_id FROM p_lang
    UNION ALL
    SELECT patient_id FROM p_mar
    UNION ALL
    SELECT patient_id FROM p_rac)
),
all_attributes AS (
    SELECT 
        all_pids.patient_id,
        p_dis.code AS disability_code,
        p_eth.code AS ethnicity_code,
        p_lang.code AS language_code,
        p_mar.code AS marital_code,
        p_rac.code AS race_code
    FROM all_pids
    LEFT JOIN p_dis ON p_dis.patient_id = all_pids.patient_id
    LEFT JOIN p_eth ON p_eth.patient_id = all_pids.patient_id
    LEFT JOIN p_lang ON p_lang.patient_id = all_pids.patient_id
    LEFT JOIN p_mar ON p_mar.patient_id = all_pids.patient_id
    LEFT JOIN p_rac ON p_rac.patient_id = all_pids.patient_id )
SELECT * FROM all_attributes