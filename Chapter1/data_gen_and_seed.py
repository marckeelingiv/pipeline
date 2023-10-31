from DataGenClasses import (
    FacilityDataClass, ComprehensiveEncounterDataClass, 
    PatientVisitDataClass, ComprehensiveEncounterMapDataClass, 
    PatientDiagnosisDataClass, PatientVisitPDSCareProviderDataClass, 
    PatientVisitDetailsDataClass, PatientLanguageDataClass, 
    PatientDisabilityDataClass, PatientMaritalDataClass, 
    PatientRaceDataClass, PatientEthnicityDataClass
    )
from mysql_connection import engine
from pandas import DataFrame
  
facility_list = []
comprehensive_encounter_list = []
patient_visit_list = []
comprehensive_encounter_map_list = []
patient_diagnosis_list = []
patient_visit_pds_care_provider_list = []
patient_visit_details_list = []
PatientLanguage_list = []
PatientDisability_list = []
PatientMarital_list = []
PatientRace_list = []
PatientEthnicity_list = []

# Data Generation
for facility_id_num in range(20):
    facility = FacilityDataClass(
        id=facility_id_num).__dict__
    facility_list.append(facility)

    # Comprehensive Encounter Generation
    for comprehensive_encounter_id in range(4000):
        comprehensive_encounter = ComprehensiveEncounterDataClass(
            facility_id=facility_id_num)
        comprehensive_encounter_list.append(comprehensive_encounter.__dict__)

        patient_visit = PatientVisitDataClass(
            patient_id=comprehensive_encounter.patient_id, 
            facility_id=facility_id_num)
        patient_visit_list.append(patient_visit.__dict__)

        comprehensive_encounter_map = ComprehensiveEncounterMapDataClass(
            comprehensive_encounter_id=comprehensive_encounter.id, 
            patient_visit_id=patient_visit.id)
        comprehensive_encounter_map_list.append(comprehensive_encounter_map.__dict__)

        patient_diagnosis = PatientDiagnosisDataClass(
            patient_visit_id=patient_visit.id)
        patient_diagnosis_list.append(patient_diagnosis.__dict__)

        patient_visit_pds_care_provider = PatientVisitPDSCareProviderDataClass(
            patient_visit_id=patient_visit.id)
        patient_visit_pds_care_provider_list.append(patient_visit_pds_care_provider.__dict__)

        patient_visit_details = PatientVisitDetailsDataClass(
            id=patient_visit.id)
        patient_visit_details_list.append(patient_visit_details.__dict__)

        PatientLanguage = PatientLanguageDataClass(
            patient_id=patient_visit.patient_id,
            facility_id=patient_visit.facility_id)
        PatientLanguage_list.append(PatientLanguage.__dict__)

        PatientDisability = PatientDisabilityDataClass(
            patient_id=patient_visit.patient_id,
            facility_id=patient_visit.facility_id)
        PatientDisability_list.append(PatientDisability.__dict__)

        PatientMarital = PatientMaritalDataClass(
            patient_id=patient_visit.patient_id,
            facility_id=patient_visit.facility_id)
        PatientMarital_list.append(PatientMarital.__dict__)

        PatientRace = PatientRaceDataClass(
            patient_id=patient_visit.patient_id,
            facility_id=patient_visit.facility_id)
        PatientRace_list.append(PatientRace.__dict__)

        PatientEthnicity = PatientEthnicityDataClass(
            patient_id=patient_visit.patient_id,
            facility_id=patient_visit.facility_id)
        PatientEthnicity_list.append(PatientEthnicity.__dict__)

# Upload to MySQL
DataFrame.from_records(facility_list).to_sql(
    'facility',
    con=engine, 
    if_exists='replace',
    index=False)
DataFrame.from_records(comprehensive_encounter_list).to_sql(
    'comprehensive_encounter',
    con=engine, 
    if_exists='replace',
    index=False)
DataFrame.from_records(patient_visit_list).to_sql(
    'patient_visit',
    con=engine, 
    if_exists='replace',
    index=False)
DataFrame.from_records(comprehensive_encounter_map_list).to_sql(
    'comprehensive_encounter_map',
    con=engine, 
    if_exists='replace',
    index=False)
DataFrame.from_records(patient_diagnosis_list).to_sql(
    'patient_diagnosis',
    con=engine, 
    if_exists='replace',
    index=False)
DataFrame.from_records(patient_visit_pds_care_provider_list).to_sql(
    'patient_visit_pds_care_provider',
    con=engine, 
    if_exists='replace',
    index=False)
DataFrame.from_records(patient_visit_details_list).to_sql(
    'patient_visit_details',
    con=engine, 
    if_exists='replace',
    index=False)
DataFrame.from_records(PatientLanguage_list).to_sql(
    'PatientLanguage',
    con=engine, 
    if_exists='replace',
    index=False)
DataFrame.from_records(PatientDisability_list).to_sql(
    'PatientDisability',
    con=engine, 
    if_exists='replace',
    index=False)
DataFrame.from_records(PatientMarital_list).to_sql(
    'PatientMarital',
    con=engine, 
    if_exists='replace',
    index=False)
DataFrame.from_records(PatientRace_list).to_sql(
    'PatientRace',
    con=engine, 
    if_exists='replace',
    index=False)
DataFrame.from_records(PatientEthnicity_list).to_sql(
    'PatientEthnicity',
    con=engine, 
    if_exists='replace',
    index=False)