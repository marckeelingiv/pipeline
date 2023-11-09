from collections import OrderedDict
from faker import Faker
from dataclasses import dataclass, field
from datetime import datetime
import pandas as pd

'''
The code provided defines several data classes that can be used to generate fake 
data for different entities such as facilities, patient visits, patient diagnoses, 
etc. These data classes are defined using the dataclass decorator from the dataclasses 
module. Each data class has attributes that represent the fields of the entity it 
represents, and these attributes have default values that generate random fake 
data using the faker library.
'''

faker = Faker()

def _company():
    return faker.company()
def _phone():
    return faker.phone()
def _uuid4():
    return faker.uuid4()
def _name():
    return faker.name()
def _base_location():
    return faker.local_latlng(country_code='US')
def _address():
    return faker.address()
def _phone():
    return faker.phone_number()
def _name():
    return faker.name()
def _past_date():
    return faker.past_date()
def _company_email():
    return faker.company_email()
def _city():
    return faker.city()
def _zip():
    return faker.zipcode()
def _url():
    return faker.url()
def _bban():
    return faker.bban()
def _int():
    return faker.pyint()

class DataClassDF():
    '''The `DataClassDF` class is a base class that provides a method `return_df()` 
    which returns a Pandas DataFrame representation of the data class object. 
    It uses the `__dict__` attribute to retrieve the attribute-value pairs of 
    the object and creates a DataFrame from them.  '''
    def return_df(self)->pd.DataFrame:
        df:pd.DataFrame = pd.DataFrame.from_dict(self.__dict__.items()).set_index(0).transpose()
        return df

@dataclass()
class FacilityDataClass(DataClassDF):
    '''The `FacilityDataClass` is a data class that inherits from `DataClassDF`. 
    It defines attributes representing the fields of a facility, such as id, 
    name, address, phone, etc. It also defines default factory functions 
    for generating random values for these attributes using the `faker` library.  
   
   The `__post_init__()` method in the `FacilityDataClass` is a special method 
   that is called automatically after the initialization of the object. 
   It extracts the latitude, longitude, county, country, and state from 
   the `location` attribute and assigns them to separate attributes. 
   Finally, it deletes the `location` attribute.

   Used to create instances of facilities and convert them to DataFrame objects using the `return_df()` method.'''
    def _participating():
        return faker.random_element(elements=OrderedDict([(0,0.8),(1,0.2)]))

    def _type():
        _types = [
            ("?", 0.725985594722553),
            ("snf", 0.100029169564925),
            ("h", 0.0650256916552606),
            ("c", 0.0445845580810914),
            ("f", 0.00792065878340476),
            ("x", 0.00740458186550587),
            ("v", 0.00617048488792156),
            ("s", 0.00583391298494402),
            ("hha", 0.00543002670137097),
            ("p", 0.00385935782080912),
            ("m", 0.00370229093275293),
            ("o", 0.00325352839544955),
            ("u", 0.00296183274620235),
            ("fq", 0.00278232773128099),
            ("z", 0.00242331770143828),
            ("alf", 0.00237844144770795),
            ("g", 0.00159310700742702),
            ("ssa", 0.00143604011937084),
            ("msbh", 0.00134628761191016),
            ("y", 0.00123409697758431),
            ("sat", 0.00096483945520228),
            ("hr", 0.000785334440280925),
            ("hp", 0.000471200664168555),
            ("ems", 0.000448762537303386),
            ("hie", 0.000403886283573047),
            ("l", 0.000359010029842709),
            ("d", 0.000291695649247201),
            ("t", 0.000269257522382032),
            ("ob", 0.000224381268651693),
            ("i", 0.000179505014921354),
            ("a", 0.000112190634325846),
            ("b", 0.00008975250746),
            ("rh", 0.0000044876254),
        ]
        return faker.random_element(elements=OrderedDict(_types))

    id:str = field(default_factory=_uuid4)
    name:str = field(default_factory=_company)
    address:str = field(default_factory=_address)
    address2:str = field(default_factory=_address)
    phone:str = field(default_factory=_phone)
    contact_name:str = field(default_factory=_name)
    participating:int = field(default_factory=_participating)
    join_date:datetime = field(default_factory=_past_date)
    email:str = field(default_factory=_company_email)
    city:str = field(default_factory=_city)
    state:str = field(init=False)
    zip:str = field(default_factory=_zip)
    country:str = field(init=False)
    parent_facility_id:str = field(default_factory=_uuid4)
    type:str = field(default_factory=_type)
    latitude:str = field(init=False)
    longitude:str = field(init=False)
    url:str = field(default_factory=_url)
    created_by:datetime = field(default_factory=_past_date)
    created_on:datetime = field(default_factory=_past_date)
    last_update:datetime = field(default_factory=_past_date)
    location:str = field(default_factory=_base_location)

    def __post_init__(self):
        self.latitude = self.location[0]
        self.longitude = self.location[1]
        self.county = self.location[2]
        self.country = self.location[3]
        self.state = self.location[4].split("/")[1]
        del self.location

@dataclass
class ComprehensiveEncounterDataClass(DataClassDF):
    '''A template for generating synthetic data for comprehensive encounter mapping. 
    The ComprehensiveEncounterMapDataClass class contains attributes related to the 
    mapping of comprehensive encounters, such as the IDs of the encounter, visit, 
    and patient, as well as information about the deletion status and sensitivity 
    of the mapping. It creates keeps track of groups of visits'''
    def _type():
        types_frequency = [
            ("BEHAVIORAL_HEALTH",0.0005),
            ("EMERGENCY",0.183),
            ("INPATIENT",0.071),
            ("NULL",0.0005),
            ("POST_ACUTE_CARE",0.0105),
            ("UNKNOWN",0.7345),
        ]
        return faker.random_element(elements=OrderedDict(types_frequency))

    def _matching_method():
        return faker.random_element(elements=OrderedDict([("ACCOUNT_NUMBER",0.64),("BILLING_ACCOUNT_NUMBER",0.36)]))


    id:str = field(default_factory=_uuid4)
    facility_id:str = field(default_factory=_uuid4)
    created_on:datetime = field(default_factory=_past_date)
    deleted_on:datetime = field(default_factory=_past_date)
    matching_method:str = field(default_factory=_matching_method)
    matching_method_identifier:str = field(default_factory=_uuid4)
    admit_date:datetime = field(default_factory=_past_date)
    discharge_date:datetime = field(default_factory=_past_date)
    type:str = field(default_factory=_type)
    patient_id:str = field(default_factory=_uuid4)

@dataclass
class PatientVisitDataClass(DataClassDF):
    '''The PatientVisitDataClass has several attributes such as id, patient_id, admit_date, 
    created_on, etc. These attributes have default values defined using factory functions.
    Has three private methods _discharge_disposition, _major_class, and _sensitive_categories. 
    These methods generate random values based on predefined frequencies for the corresponding attributes.
    Overall it is a template for generating synthetic patient visit data with random values for various attributes.'''
    def _discharge_disposition():
        discharge_disposition_frequency = [
            (1, 0.4135),
            (2, 0.0015),
            (3, 0.0025),
            (4, 0.0005),
            (5, 0.002),
            (6, 0.0065),
            (7, 0.004),
            (8, 0.0015),
            (9, 0.0035),
            (20, 0.002),
            (30, 0.005),
            (68, 0.0005),
            (70, 0.009),
            (76, 0.0005),
            (118, 0.001),
            (119, 0.0015),
            (120, 0.0015),
            (126, 0.0005),
            (127, 0.002),
            (None, 0.541),
        ]
        return faker.random_element(elements=OrderedDict(discharge_disposition_frequency))
    
    def _major_class():
        major_class_frequency = [
            ("A", 0.004),
            ("C", 0.0095),
            ("E", 0.2445),
            ("I", 0.0595),
            ("L", 0.0085),
            ("NULL", 0.001),
            ("O", 0.6145),
            ("P", 0.037),
            ("R", 0.001),
            ("U", 0.0075),
            ("V", 0.013),
        ]
        return faker.random_element(elements=OrderedDict(major_class_frequency))
        
    def _sensitive_categories():
        sensitive_categories_frequency = [
            (0, 0.995),
            (4, 0.0015),
            (6, 0.0035),
        ]
        return faker.random_element(elements=OrderedDict(sensitive_categories_frequency))

    id:str = field(default_factory=_uuid4)
    patient_id:str = field(default_factory=_uuid4)
    admit_date:datetime = field(default_factory=_past_date)
    created_on:datetime = field(default_factory=_past_date)
    account_number:str = field(default_factory=_bban)
    discharge_date:datetime = field(default_factory=_past_date)
    data_source:str = field(default_factory=_uuid4)
    facility_id:str = field(default_factory=_uuid4)
    discharge_disposition:int = field(default_factory=_discharge_disposition)
    visit_type:int = field(default_factory=_int)
    transfer_date:datetime = field(default_factory=_past_date)
    major_class:str = field(default_factory=_major_class)
    billing_account_number:str = field(default_factory=_bban)
    sensitive_categories:int = field(default_factory=_sensitive_categories)

@dataclass
class ComprehensiveEncounterMapDataClass(DataClassDF):
    '''The ComprehensiveEncounterMapDataClass class also has a private method _deleted_on 
    which generates a random value for the deleted_on attribute based on a predefined frequency. 
    The deleted_on attribute represents the date when the mapping was deleted, and it can 
    have a value of None (80% probability) or a random past date (20% probability).

    Additionally, the class has attributes for created_on, patient_id, and is_sensitive. 
    The created_on attribute represents the date when the mapping was created, the patient_id 
    attribute stores the ID of the patient, and the is_sensitive attribute indicates whether 
    the mapping is sensitive or not, with a default value of 0 (not sensitive).

    Overall, this code defines a data class for generating synthetic data related to 
    comprehensive encounter mapping, with various attributes representing different 
    aspects of the mapping.'''
    def _deleted_on():
        deleted_on_frequency = [
            (None, 0.8),
            (faker.past_date(), 0.2)
        ]
        return faker.random_element(elements=OrderedDict(deleted_on_frequency))

    id:str = field(default_factory=_uuid4)
    comprehensive_encounter_id:str = field(default_factory=_uuid4)
    patient_visit_id:str = field(default_factory=_uuid4)
    deleted_on:datetime = field(default_factory=_deleted_on)
    created_on:datetime = field(default_factory=_past_date)
    patient_id:str = field(default_factory=_uuid4)
    is_sensitive:int = field(default=0)

@dataclass
class PatientLanguageDataClass(DataClassDF):
    '''The PatientLanguageDataClass class represents patient language data. 
    It has several attributes such as id, created_on, created_by, etc. 
    These attributes have default values defined using factory functions or static values.
    
    The PatientLanguageDataClass class includes attributes related to 
    the language of the patient. For example, the code attribute stores 
    the language code, with a default value of "ENG" (English). Other 
    attributes such as patient_id, facility_id, and data_source_id store 
    the IDs of the patient, facility, and data source respectively.
    
    Overall, this code defines a data class for generating synthetic 
    data related to patient language information. It provides attributes 
    to store various details such as language code, creation information, 
    patient and facility IDs, and data source ID.'''
    id:str = field(default_factory=_uuid4)
    created_on:datetime = field(default_factory=_past_date)
    created_by:str = field(default="1")
    last_seen:datetime = field(default_factory=_past_date)
    patient_id:str = field(default_factory=_uuid4)
    facility_id:str = field(default_factory=_uuid4)
    data_source_id:str = field(default_factory=_uuid4)
    code:str = field(default="ENG")
    insert_id:str = field(default_factory=_uuid4)

@dataclass
class PatientDisabilityDataClass(DataClassDF):
    '''The PatientDisabilityDataClass class represents patient disability data. 
    It has several attributes such as id, created_on, created_by, etc. 
    These attributes have default values defined using factory functions or static values.

    The PatientDisabilityDataClass class also has a private method _code_frequency 
    which generates a random value for the code attribute based on a predefined frequency. 
    The code attribute represents the disability code, and it can have values 
    like "UK", "DREM", "DEYE", etc., with different probabilities.

    Other attributes such as patient_id, facility_id, and data_source_id 
    store the IDs of the patient, facility, and data source respectively.

    Overall, this code defines a data class for generating synthetic data 
    related to patient disability information. It provides attributes to store 
    various details such as disability code, creation information, patient and 
    facility IDs, and data source ID.
    '''
    def _code_frequency():
        code_frequency = [
            ("UK", 0.99),
            ("DREM", 0.006),
            ("DEYE", 0.0014),
            ("DPHY", 0.0014),
            ("DEAR", 0.0012),
        ]
        return faker.random_element(elements=OrderedDict(code_frequency))

    id:str = field(default_factory=_uuid4)
    created_on:datetime = field(default_factory=_past_date)
    created_by:str = field(default="1")
    last_seen:datetime = field(default_factory=_past_date)
    patient_id:str = field(default_factory=_uuid4)
    facility_id:str = field(default_factory=_uuid4)
    data_source_id:str = field(default_factory=_uuid4)
    code:str = field(default_factory=_code_frequency)
    insert_id:str = field(default_factory=_uuid4)

@dataclass
class PatientMaritalDataClass(DataClassDF):
    '''The PatientMaritalDataClass class represents patient marital status data. 
    It has several attributes such as id, created_on, created_by, etc. 
    These attributes have default values defined using factory functions or static values.

    The PatientMaritalDataClass class also has a private method _code_frequency 
    which generates a random value for the code attribute based on a predefined frequency. 
    The code attribute represents the marital status code, and it can have values like 
    "S" (single), "M" (married), "D" (divorced), "W" (widowed), etc., with different probabilities.

    Other attributes such as patient_id, facility_id, and data_source_id store the IDs 
    of the patient, facility, and data source respectively.

    Overall, this code defines a data class for generating synthetic data related 
    to patient marital status information. It provides attributes to store various 
    details such as marital status code, creation information, patient and 
    facility IDs, and data source ID.'''
    def _code_frequency():
        code_frequency = [
            ("S", 0.5838),
            ("M", 0.2452),
            ("D", 0.073),
            ("W", 0.0572),
            ("SP", 0.024),
            ("O", 0.0132),
            ("LP", 0.0036),
        ]
        return faker.random_element(elements=OrderedDict(code_frequency))

    id:str = field(default_factory=_uuid4)
    created_on:datetime = field(default_factory=_past_date)
    created_by:str = field(default="1")
    last_seen:datetime = field(default_factory=_past_date)
    patient_id:str = field(default_factory=_uuid4)
    facility_id:str = field(default_factory=_uuid4)
    data_source_id:str = field(default_factory=_uuid4)
    code:str = field(default_factory=_code_frequency)
    insert_id:str = field(default_factory=_uuid4)

@dataclass
class PatientRaceDataClass(DataClassDF):
    '''The PatientRaceDataClass class represents patient race data. 
    It has several attributes such as id, created_on, created_by, etc. 
    These attributes have default values defined using factory functions or static values.

    The PatientRaceDataClass class also has a private method _code_frequency 
    which generates a random value for the code attribute based on a 
    predefined frequency. The code attribute represents the race code, 
    and it can have values like "W" (White), "OR" (Other), "B" (Black), 
    "AI" (American Indian), "AS" (Asian), etc., with different probabilities.

    Other attributes such as patient_id, facility_id, and data_source_id 
    store the IDs of the patient, facility, and data source respectively.

    Overall, this code defines a data class for generating synthetic 
    data related to patient race information. It provides attributes 
    to store various details such as race code, creation information, 
    patient and facility IDs, and data source ID.'''
    def _code_frequency():
        code_frequency = [
            ("W", 0.6526),
            ("B", 0.1546),
            ("HI", 0.1022),
            ("OR", 0.074),
            ("AI", 0.0056),
            ("AS", 0.0032),
            ("ASI", 0.0028),
            ("UK", 0.0018),
            ("AIAN", 0.001),
            ("CH", 0.0006),
            ("FL", 0.0006),
            ("D", 0.0004),
            ("KR", 0.0002),
            ("NH", 0.0002),
            ("VT", 0.0002),
        ]
        return faker.random_element(elements=OrderedDict(code_frequency))

    id:str = field(default_factory=_uuid4)
    created_on:datetime = field(default_factory=_past_date)
    created_by:str = field(default="1")
    last_seen:datetime = field(default_factory=_past_date)
    patient_id:str = field(default_factory=_uuid4)
    facility_id:str = field(default_factory=_uuid4)
    data_source_id:str = field(default_factory=_uuid4)
    code:str = field(default_factory=_code_frequency)
    insert_id:str = field(default_factory=_uuid4)

@dataclass
class PatientEthnicityDataClass(DataClassDF):
    '''The PatientEthnicityDataClass class represents patient ethnicity data. 
    It has several attributes such as id, created_on, created_by, etc. 
    These attributes have default values defined using factory functions or static values.

    The PatientEthnicityDataClass class also has a private method _code_frequency 
    which generates a random value for the code attribute based on a predefined 
    frequency. The code attribute represents the ethnicity code, and it can have 
    values like "NHL" (Non-Hispanic/Latino), "CA" (Caucasian), "UK" (Unknown), 
    "HO" (Hispanic/Latino), "HL" (Hispanic or Latino), etc., with different probabilities.

    Other attributes such as patient_id, facility_id, and data_source_id 
    store the IDs of the patient, facility, and data source respectively.

    Overall, this code defines a data class for generating synthetic 
    data related to patient ethnicity information. It provides attributes 
    to store various details such as ethnicity code, creation information, 
    patient and facility IDs, and data source ID.'''
    def _code_frequency():
        code_frequency = [
            ("NHL", 0.7812),
            ("CA", 0.075),
            ("UK", 0.0364),
            ("HO", 0.0356),
            ("HL", 0.0272),
            ("DO", 0.0136),
            ("ME", 0.0114),
            ("GU", 0.0098),
            ("PR", 0.0072),
            ("CH", 0.0016),
            ("D", 0.0008),
            ("CU", 0.0002),
        ]
        return faker.random_element(elements=OrderedDict(code_frequency))

    id:str = field(default_factory=_uuid4)
    created_on:datetime = field(default_factory=_past_date)
    created_by:str = field(default="1")
    last_seen:datetime = field(default_factory=_past_date)
    patient_id:str = field(default_factory=_uuid4)
    facility_id:str = field(default_factory=_uuid4)
    data_source_id:str = field(default_factory=_uuid4)
    code:str = field(default_factory=_code_frequency)
    insert_id:str = field(default_factory=_uuid4)

@dataclass
class PatientDiagnosisDataClass(DataClassDF):
    '''The PatientDiagnosisDataClass class represents patient diagnosis data. 
    It has several attributes such as id, patient_id, description, diagnosis_date, 
    created_on, etc. These attributes have default values defined using factory 
    functions or static values.

    The PatientDiagnosisDataClass class also has two private methods: 
    _priority_frequency and _type_frequency. These methods generate random values 
    for the priority and type attributes respectively, based on predefined frequencies. 
    The priority attribute represents the priority of the diagnosis, and the type 
    attribute represents the type of diagnosis.

    Other attributes such as data_source, code, and patient_visit_id store 
    the data source ID, diagnosis code, and patient visit ID respectively.

    Overall, this code defines a data class for generating synthetic data 
    related to patient diagnosis information. It provides attributes to 
    store various details such as diagnosis code, description, diagnosis date, 
    creation information, patient and data source IDs, priority, and type of diagnosis.'''
    def _priority_frequency():
        priority_frequency = [
            ("NULL", 0.7034),
            ("1", 0.076),
            ("2", 0.053),
            ("0", 0.034),
            ("3", 0.022),
            ("4", 0.0196),
            ("5", 0.0152),
            ("6", 0.0102),
            ("8", 0.0096),
            ("7", 0.009),
            ("9", 0.0064),
            ("11", 0.0044),
            ("12", 0.0044),
            ("10", 0.0032),
            ("13", 0.0026),
            ("99", 0.0024),
            ("18400", 0.002),
            ("14", 0.0018),
            ("15", 0.0018),
            ("16", 0.0018),
            ("17", 0.0018),
            ("19", 0.0016),
            ("18", 0.0014),
            ("-1", 0.0012),
            ("20", 0.0012),
            ("21", 0.0012),
            ("25", 0.0008),
            ("22", 0.0006),
            ("23", 0.0006),
            ("27", 0.0006),
            ("24", 0.0004),
            ("26", 0.0004),
            ("28", 0.0004),
            ("40", 0.0004),
            ("10800", 0.0004),
            ("29", 0.0002),
            ("30", 0.0002),
            ("31", 0.0002),
            ("32", 0.0002),
            ("34", 0.0002),
            ("36", 0.0002),
            ("38", 0.0002),
            ("39", 0.0002),
            ("41", 0.0002),
            ("42", 0.0002),
            ("43", 0.0002),
            ("52", 0.0002),
            ("57", 0.0002),
            ("58", 0.0002),
            ("59", 0.0002),
            ("60", 0.0002),
            ("83", 0.0002),
            ("101", 0.0002),
            ("113", 0.0002),
            ("10150", 0.0002),
            ("10151", 0.0002),
        ]
        return faker.random_element(elements=OrderedDict(priority_frequency))
    
    def _type_frequency():
        type_frequency = [
            ("NULL", 0.394),
            ("F", 0.16),
            ("A", 0.1216),
            ("W", 0.1154),
            ("S", 0.0716),
            ("U", 0.0586),
            ("P", 0.0502),
            ("R", 0.028),
            ("D", 0.0006),
        ]
        return faker.random_element(elements=OrderedDict(type_frequency))
    
    id:str = field(default_factory=_uuid4)
    patient_id:str = field(default_factory=_uuid4)
    description:str = field(default_factory=faker.sentence)
    diagnosis_date:datetime = field(default_factory=_past_date)
    created_on:datetime = field(default_factory=_past_date)
    created_by:str = field(default="1")
    data_source:str = field(default_factory=_uuid4)
    code:str = field(default_factory=_uuid4)
    patient_visit_id:str = field(default_factory=_uuid4)
    priority:str = field(default_factory=_priority_frequency)
    type:str = field(default_factory=_type_frequency)

@dataclass
class PatientVisitPDSCareProviderDataClass(DataClassDF):
    '''Defines a data class for generating synthetic data related 
    to care provider data associated with a patient visit in a Patient 
    Data Source (PDS) system. It provides attributes to store various 
    details such as identifiers for the care provider, patient visit, 
    and data source, creation and deletion information, and user identifiers.'''
    id:str = field(default_factory=_uuid4)
    patient_visit_id:str = field(default_factory=_uuid4)
    care_provider_id:str = field(default_factory=_uuid4)
    data_source:str = field(default_factory=_uuid4)
    created_on:datetime = field(default_factory=_past_date)
    created_by:str = field(default="Null")
    deleted_on:str = field(default="Null")
    deleted_by:str = field(default="Null")
    
@dataclass
class PatientIdentDataClass(DataClassDF):
    '''The created_on attribute stores the timestamp when the patient identification 
    data was created. The data_source attribute stores the unique identifier 
    for the data source of the patient identification data. The last_seen attribute 
    stores the datetime when the patient identification data was last seen.

    The ssn_salted and ssn_last4_salted attributes store the salted values of the 
    Social Security Number (SSN) and last 4 digits of the SSN respectively. 
    The ssn_hash and ssn_last4_hash attributes store the hashed values of the 
    SSN and last 4 digits of the SSN respectively.

    The hash_key_id attribute represents the identifier for the hash key used 
    for hashing the SSN and last 4 digits of the SSN. It is set to "NULL" by default.

    Overall, this code defines a data class for generating synthetic data related 
    to patient identification information. It provides attributes to store various 
    details such as identifiers, date of birth, type, creation information, data source, 
    last seen datetime, salted and hashed values of the SSN and last 
    4 digits of the SSN, and hash key identifier.'''
    id:str = field(default_factory=_uuid4) # varchar(36) PK 
    patient_id:str = field(default_factory=_uuid4) # varchar(36) 
    date_of_birth:datetime = field(default_factory=_past_date) # date 
    type:str = field(default="NULL") # int(10) UN 
    created_on:datetime = field(default_factory=_past_date) # timestamp 
    data_source:str = field(default_factory=_uuid4) # varchar(36) 
    last_seen:datetime = field(default_factory=_past_date) # datetime 
    ssn_salted:str = field(default_factory=faker.sha256) # varchar(48) 
    ssn_last4_salted:str = field(default_factory=faker.sha256) # varchar(48) 
    ssn_hash:str = field(default_factory=_uuid4) # binary(20) 
    ssn_last4_hash:str = field(default_factory=_uuid4) # binary(16) 
    hash_key_id:str = field(default="NULL") # int(11)

@dataclass
class PatientVisitDetailsDataClass(DataClassDF):
    '''Defines a data class for generating synthetic data related to the details 
    of a patient visit. It provides attributes to store various details such as 
    identifiers, notes, privacy level, attending physician, chief complaint, 
    discharge diagnosis, discharge disposition, user who added the details, 
    location, last seen datetime, presumed discharge date and reason, 
    prior patient location, and admit source type.
    '''
    def _type_frequency():
        type_frequency = [
            ("NULL", 0.948853615520282),
            ("(blank)", 0.0141093474426808),
            ("lab", 0.00377928949357521),
            ("CHEST PAIN", 0.00251952632905014),
            ("Back Pain", 0.00201562106324011),
            ("Abd Pain", 0.0017636684303351),
            ("screening", 0.0017636684303351),
            ("Abdominal pain", 0.00151171579743008),
            ("LOW BACK PAIN", 0.00125976316452507),
            ("CLINIC", 0.00100781053162006),
            ("COUGH", 0.00100781053162006),
            ("FEVER", 0.00100781053162006),
            ("headache", 0.00100781053162006),
            ("OSA", 0.00100781053162006),
            ("Priv", 0.00100781053162006),
            ("SCREENING MAMMOGRAM", 0.00100781053162006),
            ("xray", 0.00100781053162006),
            ("Allscripts Order", 0.000755857898715042),
            ("CONSULT", 0.000755857898715042),
            ("COVID", 0.000755857898715042),
            ("CP", 0.000755857898715042),
            ("DYSPHAGIA", 0.000755857898715042),
            ("Fall", 0.000755857898715042),
            ("I10", 0.000755857898715042),
            ("labs", 0.000755857898715042),
            ("MVA", 0.000755857898715042),
            ("MVC", 0.000755857898715042),
            ("NEWBORN", 0.000755857898715042),
            ("Newborn Delivery", 0.000755857898715042),
            ("OP LAB", 0.000755857898715042),
            ("Patient Questions", 0.000755857898715042),
            ("PELVIC PAIN", 0.000755857898715042),
            ("R53.1", 0.000755857898715042),
            ("SKIN PROBLEM", 0.000755857898715042),
            ("Weakness", 0.000755857898715042),
            ("Z12.31", 0.000755857898715042),
        ]
        return faker.random_element(elements=OrderedDict(type_frequency))
    
    def _admit_source_type():
        admit_source_type_frequency = [
            ("NULL", 0.4938),
            ("9", 0.151),
            ("10", 0.1116),
            ("12", 0.0632),
            ("1", 0.0626),
            ("8", 0.0524),
            ("2", 0.0246),
            ("3", 0.0142),
            ("31", 0.0074),
            ("13", 0.0064),
            ("0", 0.005),
            ("7", 0.0018),
            ("17", 0.0014),
            ("4", 0.001),
            ("11", 0.001),
            ("25", 0.001),
            ("16", 0.0006),
            ("5", 0.0004),
            ("21", 0.0002),
            ("26", 0.0002),
            ("30", 0.0002),
        ]
        return faker.random_element(elements=OrderedDict(admit_source_type_frequency))

    id:str = field(default_factory=_uuid4) # varchar(36) PK 
    note:str = field(default="") # text 
    note_privacy_level:int = field(default=0) # int(10) UN 
    attending_physician:str = field(default_factory=_name) # varchar(255) 
    chief_complaint:str = field(default_factory=_uuid4) # text 
    discharge_diagnosis:str = field(default_factory=_uuid4) # varchar(255) 
    discharge_disposition_raw:str = field(default_factory=_uuid4) # varchar(45) 
    added_by:str = field(default_factory=_uuid4) # varchar(36) 
    location:str = field(default_factory=_uuid4) # varchar(255) 
    location_label:str = field(default_factory=_uuid4) # varchar(255) 
    location_raw:str = field(default_factory=_uuid4) # varchar(255) 
    last_seen:str = field(default_factory=_uuid4) # datetime 
    presumed_discharge_date:str = field(default_factory=_uuid4) # datetime 
    presumed_discharge_reason:str = field(default_factory=_uuid4) # varchar(255) 
    prior_patient_location:str = field(default_factory=_uuid4) # varchar(255) 
    admit_source_type:str = field(default_factory=_admit_source_type) # smallint(6)

@dataclass
class FacilityIdentifierDataClass(DataClassDF):
    '''Defines a data class for generating synthetic data related to facility 
    identifier information. It provides attributes to store various details 
    such as identifiers, types, facility and source facility IDs, 
    and last update timestamp.'''
    def _type():
        _type_frequency = [
            ("NPI", 0.5056),
            ("hl7", 0.316),
            ("report", 0.0902),
            ("pcc-facId", 0.028),
            ("UHC_NPI", 0.0046),
            ("UHC_TIN", 0.0044),
            ("BCI_2021_ADDRESS_IDN", 0.0036),
            ("BCI_2021_PRV_EXTERNAL_ID", 0.0036),
            ("BCI_ADDRESS_IDN", 0.0036),
            ("DHC_NPI", 0.0036),
            ("BCI_PRV_NPIN", 0.0034),
            ("BCI_PRV_EXTERNAL_ID", 0.0032),
            ("direct-address", 0.0032),
            ("NAT_UHC_NPI", 0.003),
            ("pcc-orgId", 0.0028),
            ("molina", 0.0024),
            ("molina-hh", 0.0018),
            ("pmg_clinic_id", 0.0014),
            ("addus_homecare_pcs", 0.001),
            ("providence_clinic_id", 0.001),
            ("Regence _PRPR", 0.001),
            ("tuality_id", 0.001),
            ("BCBSMA_NPI", 0.0008),
            ("H_SID", 0.0008),
            ("MMIS_IDNTFR", 0.0008),
            ("ProvID", 0.0008),
            ("providence_clinic", 0.0006),
            ("anthem_ca_HealthHome", 0.0004),
            ("compass", 0.0004),
            ("f_idents", 0.0004),
            ("FLC Care Coordinator", 0.0004),
            ("international_community_ichs", 0.0004),
            ("molina_provider_clinic", 0.0004),
            ("nh_healthy_families_npi2", 0.0004),
            ("odds", 0.0004),
            ("providence_clinic_region", 0.0004),
            ("trillium_npi", 0.0004),
            ("western_sky_tin", 0.0004),
            ("amerigroup", 0.0002),
            ("CCO", 0.0002),
            ("centene_npi", 0.0002),
            ("centene_tin", 0.0002),
            ("cigna_pnw_cac_attribution", 0.0002),
            ("GOBHI", 0.0002),
            ("Healthpoint_Ochin", 0.0002),
            ("King County BH Recovery NA", 0.0002),
            ("la_clinica_child_portal", 0.0002),
            ("mcinnis_facility", 0.0002),
            ("MultCo Clinic", 0.0002),
            ("ochin_pat_facility_relationship", 0.0002),
            ("Parent Organization", 0.0002),
            ("php_pod", 0.0002),
            ("steward_child", 0.0002),
            ("trillium_tin", 0.0002),
            ("WVP_referral", 0.0002),
        ]
        return faker.random_element(elements=OrderedDict(_type_frequency))
    def _source_facility():
        _source_facility_frequency = [
            ("1", 0.969033856317093),
            ("10", 0.00350949628406276),
            ("78", 0.000412881915772089),
            ("104", 0.00474814203137903),
            ("697", 0.000412881915772089),
            (_uuid4, 0.021882742),
        ]
        return faker.random_element(elements=OrderedDict(_source_facility_frequency))

    deleted_on_frequency = [
            (None, 0.8),
            (faker.past_date(), 0.2)
        ]
    id:str = field(default_factory=_uuid4) # varchar(36) PK
    identifier:str = field(default_factory=_company) # varchar(255)
    type:str = field(default_factory=_type) # varchar(45)
    facility_id:str = field(default_factory=_uuid4) # varchar(36)
    source_facility_id:str = field(default_factory=_source_facility) # char(36)
    last_update:datetime = field(default=datetime(2000,1,1)) # timestamp

@dataclass
class Hl7MappingDataClass(DataClassDF):
    '''Defines a data class for generating synthetic data related to 
    HL7 mapping information. It provides attributes to store various details 
    such as identifiers, facility ID, name, segment, segment iteration, field, 
    field iteration, component, subcomponent, creation and deletion information, 
    translation, default value, mapping configurations, and group association.'''
    def _name_():
        _name_frequency = [
            ("ENCOUNTER_FACILITY", 0.151866450266636),
            ("ENCOUNTER_SERVICE", 0.118247159749594),
            ("ENCOUNTER_CLASS", 0.0890331555761651),
            ("ENCOUNTER_DISCHARGE_DISPOSITION", 0.0709482958497566),
            ("ENCOUNTER_LOCATION_LABEL", 0.05170415024345),
            ("ENCOUNTER_LOCATION", 0.0468351495478785),
            ("ENCOUNTER_ADMIT_SOURCE", 0.0452121493160213),
            ("ENCOUNTER_PATIENT_TYPE", 0.0347785763969395),
            ("IGNORE_ENCOUNTER", 0.0250405750057964),
            ("ENCOUNTER_DELETE", 0.0231857175979597),
            ("PATIENT_MRN", 0.0217945745420821),
            ("ALLERGY_SEVERITY", 0.0206352886621841),
            ("CARE_PROVIDER_FILTER", 0.0201715743102249),
            ("ENCOUNTER_CANCEL_DISCHARGE", 0.0169255738465105),
            ("DIAGNOSIS_CODE_METHOD", 0.0162300023185718),
            ("PATIENT_MRN_AUTHORITY_TO_USE", 0.0153025736146534),
            ("ENCOUNTER_ACCOUNT", 0.0146070020867146),
            ("CARE_PROVIDER_LAST_NAME", 0.014375144910735),
            ("ENCOUNTER_REASON", 0.0141432877347554),
            ("PATIENT_PHONE_TYPE", 0.0141432877347554),
            ("DIAGNOSIS_NAME", 0.0139114305587758),
            ("PATIENT_SEX", 0.0134477162068166),
            ("CARE_PROVIDER_FIRST_NAME", 0.0129840018548574),
            ("DIAGNOSIS_TYPE", 0.0125202875028982),
            ("PATIENT_DEMOGRAPHIC_MARITAL_STATUS_CODE", 0.0118247159749594),
            ("PATIENT_DEMOGRAPHIC_LANGUAGE_CODE", 0.0115928587989798),
            ("PATIENT_DEMOGRAPHIC_ETHNICITY_CODE", 0.0111291444470206),
            ("PROVIDER_SHOULD_NOTIFY_DEFAULT", 0.0106654300950614),
            ("CARE_PROVIDER_NPI_IDENTIFIER", 0.00996985856712265),
            ("CARE_PROVIDER_MIDDLE_NAME", 0.00973800139114306),
            ("ENCOUNTER_ATTEND_PHYSICIAN_IDENTIFIER_TYPE", 0.00950614421516346),
            ("PATIENT_DEMOGRAPHIC_RACE_CODE", 0.00950614421516346),
            ("PROVIDER_NOTIFIED_BY_FACILITY_DEFAULT", 0.00834685833526548),
            ("ALLERGY_TYPE", 0.00811500115928588),
            ("ENCOUNTER_ATTEND_PHYSICIAN_ASSIGN_AUTH", 0.00741942963134709),
            ("ENCOUNTER_CONSULT_PHYSICIAN_IDENTIFIER_TYPE", 0.00718757245536749),
            ("ENCOUNTER_REFER_PHYSICIAN_IDENTIFIER_TYPE", 0.0069557152793879),
        ]
        return faker.random_element(elements=OrderedDict(_name_frequency))
    def _segment():
        _segment_frequency = [
            ("PV1", 0.514629258517034),
            ("PID", 0.109218436873747),
            ("---", 0.103406813627255),
            ("MSH", 0.0847695390781563),
            ("PD1", 0.0525050100200401),
            ("DG1", 0.0408817635270541),
            ("AL1", 0.0270541082164329),
            ("ROL", 0.0208416833667335),
            ("NK1", 0.0130260521042084),
            ("PV2", 0.012625250501002),
            ("OBX", 0.00440881763527054),
            ("IN1", 0.00340681362725451),
            ("OBR", 0.0030060120240481),
            ("ZPD", 0.00260521042084168),
            ("NTE", 0.00240480961923848),
            ("EVN", 0.00120240480961924),
            ("ZP1", 0.00100200400801603),
            ("CON", 0.000601202404809619),
            ("DRG", 0.000601202404809619),
            ("ZFA", 0.000601202404809619),
            ("ZRV", 0.000601202404809619),
            ("ZSD", 0.000601202404809619),

        ]
        return faker.random_element(elements=OrderedDict(_segment_frequency))
    def _segment_iteration():
        _segment_iteration_frequency = [
            (None, 0.9794),
            (0, 0.0182),
            (1, 0.0008),
            (2, 0.0006),
            (10, 0.0004),
            (14, 0.0004),
            (3, 0.0002),
        ]
        return faker.random_element(elements=OrderedDict(_segment_iteration_frequency))
    def _field_():
        _field_frequency = [
            (3, 0.275),
            (None, 0.2954),
            (4, 0.1204),
            (2, 0.1028),
            (10, 0.0878),
            (36, 0.0624),
            (8, 0.0562),
        ]
        return faker.random_element(elements=OrderedDict(_field_frequency))
    def _field_iteration():
        _field_iteration_frequency = [
            (0, 0.8224),
            (None, 0.171),
            (1, 0.0044),
            (2, 0.0012),
            (7, 0.0006),
            (3, 0.0002),
            (10, 0.0002),
        ]
        return faker.random_element(elements=OrderedDict(_field_iteration_frequency))
    def _component():
        _component_frequency = [
			(0, 0.6742),
			(None, 0.1198),
			(1, 0.085),
			(2, 0.0398),
			(3, 0.0296),
			(12, 0.0248),
			(8, 0.0148),
			(4, 0.0046),
			(6, 0.0042),
			(13, 0.0012),
			(5, 0.0008),
			(7, 0.0006),
			(9, 0.0002),
			(10, 0.0002),
			(14, 0.0002),
		]
        return faker.random_element(elements=OrderedDict(_component_frequency))
    def _subcomponent():
        _subcomponent_frequency = [
			(None, 0.8762),
			(1, 0.0772),
			(0, 0.0462),
			(5, 0.0002),
			(7, 0.0002),
		]
        return faker.random_element(elements=OrderedDict(_subcomponent_frequency))
    def _deleted_by():
        _deleted_by_frequency = [
			(None, 0.64),
			(_uuid4, .2586),
			(1, 0.0126),
		]
        return faker.random_element(elements=OrderedDict(_deleted_by_frequency))
    def _translation():
        _translation_frequency = [
			('NULL', 0.448986602542082),
			('{1":"1"', 0.0436276193747853),
			('{I":"2"', 0.0398488491927173),
			('{(?i).*ABORTION.*": "247"', 0.0364136035726554),
			('{(?i)^EMER$": "0"', 0.0364136035726554),
			('{A11":"true"}"', 0.0322913088285812),
			('{(?i).*OUTPT.*": "3"', 0.0312607351425627),
			('{SEVERE":"4"', 0.0285125386465132),
			('{A13":"true"}"', 0.0261078667124699),
			('TRUE', 0.0199244245963586),
			('{M":"1"', 0.0192373754723463),
			('FALSE', 0.0192373754723463),
			('{H":"PRN"', 0.0188938509103401),
			('{9": "I9"', 0.0185503263483339),
			('{DA":"A"', 0.0140845070422535),
			('{*":"false"}"', 0.0120233596702164),
			('{1":"10"', 0.0116798351082102),
			('{DA":"DA"', 0.0116798351082102),
			('{1":"2"', 0.0113363105462041),
			('{(?i).*CARDIOLOGY.*": "40"', 0.0109927859841979),
			('MRN', 0.00961868773617314),
			('{20":"20"', 0.00927516317416695),
			('{(?i)^WEV((?!BY).)*":"wa_prmce"', 0.00858811405015459),
			('{D":"D"', 0.00858811405015459),
			('{(?i).*EMERGENCY.*": "0"', 0.00755754036413604),
			('{PSY":"true"}"', 0.00755754036413604),
			('{A":"AS"', 0.00652696667811749),
			('{40002005":"VGH DENTAL INTEGRATION"', 0.0061834421161113),
			('{*":"4"}"', 0.00583991755410512),
			('{HOME":"1"', 0.00549639299209894),
			('{CLI":"260"', 0.00515286843009275),
			('{1":"0"', 0.00480934386808657),
			('{9":"I9"', 0.00480934386808657),
			('{AIP":"9"', 0.00480934386808657),
			('{AMA":"7"', 0.00480934386808657),
			('a', 0.00480934386808657),
			('{CLI":"12"', 0.00446581930608038),
		]
        return faker.random_element(elements=OrderedDict(_translation_frequency))
    def _default_value():
        _default_value_frequency = [
			('NULL', 0.617338487023744),
			(' "(?i).*EMERGENCY.*": "0"', 0.0369961347321922),
			('2:"2"', 0.0323025952512424),
			('O:"3"', 0.0311982330204307),
			(' "(?i).*ACUPUNCTURE.*": "360"', 0.0292655991165102),
			(' "(?i).*EXAM.*": "3"', 0.0251242407509663),
			('MODERATE:"3"', 0.02263942573164),
			('FALSE', 0.0212589729431253),
			(' "10": "I10"', 0.015184980673661),
			('C:"CEL"', 0.015184980673661),
			('MALE:"1"', 0.0146327995582551),
			('NF:"W"', 0.0110436223081171),
			('2:"12"', 0.0102153506350083),
			('FA:"FA"', 0.0093870789618995),
			('2:"3"', 0.00773053561568194),
			('21:"126"', 0.00717835450027609),
			('(?i)^WMC.*:"mch"', 0.00690226394257316),
			('AMA:"7"', 0.00690226394257316),
			('M:"M"', 0.00690226394257316),
			('ER:"0"', 0.00635008282716731),
			('50006001:"Tillamook Mobile Clinic"', 0.00469353948094975),
			('B:"B"', 0.00469353948094975),
			('10:"I10"', 0.00386526780784097),
			('I:"2"', 0.00358917725013805),
			('102:"wa_30401"', 0.00331308669243512),
			('2:"9"', 0.00331308669243512),
			('ER:"1"', 0.00331308669243512),
			('(blank)', 0.00331308669243512),
			('2:"4"', 0.00276090557702927),
			('SHORT TERM:"2"', 0.00276090557702927),
			('ACC:"330"', 0.00248481501932634),
			('CAR:"40"', 0.00248481501932634),
			('EMERGENCY:"0"', 0.00248481501932634),
			('N:"NHL"', 0.00248481501932634),
			('801EASTHLTH:"dc_1861686776"', 0.00220872446162341),
			('ANES:"218"', 0.00220872446162341),
			('BURN:"266"', 0.00220872446162341),
			('CCPHD:"or_1669777470"', 0.00220872446162341),
			('ED:"0"', 0.00220872446162341),
			(' "(?i).*CARDIOLOGY.*": "40"', 0.00193263390392049),
			('2:"5"', 0.00193263390392049),
			('AMH:"amh"', 0.00193263390392049),
			('HOME:"8"', 0.00193263390392049),
			('IP:"2"', 0.00193263390392049),
		]
        return faker.random_element(elements=OrderedDict(_default_value_frequency))
    def _map_all_field_iterations():
        _map_all_field_iterations_frequency = [
			('0', 0.600890620651266),
			('1', 0.0553854717506262),
			('3:"3"', 0.0370164208182577),
			(' "(?i).*ACUTE CARE.*": "215"', 0.0295018090731979),
			(' "(?i)^ER$": "0"', 0.0295018090731979),
			('P:"1"', 0.0295018090731979),
			(' "(?i).*IMMEDIATE CARE.*": "3"', 0.0253270247703869),
			('MILD:"1"', 0.0217088783746173),
			('NULL', 0.0217088783746173),
			('W:"WPN"', 0.0153075424436404),
			(' "I9": "I9"', 0.0150292234901197),
			('F:"2"', 0.0147509045365989),
			('FN:"F"', 0.0111327581408294),
			('EA:"EA"', 0.00946284441970498),
			('3:"0"', 0.00918452546618425),
			('4:"13"', 0.00834956860562204),
			('(?i)^WSJ.*:"sjh"', 0.00695797383801837),
			('ICU:"24"', 0.0064013359309769),
			('30:"30"', 0.00612301697745616),
			('EMERGENCY:"0"', 0.00528806011689396),
			('60110136:"Mult-Co SOUTHEAST PAC"', 0.00473142220985249),
			('SNF:"3"', 0.00473142220985249),
			('IN:"2"', 0.00445310325633176),
			(' "(?i).*EMERGENCY.*": "0"', 0.00417478430281102),
			('I9:"I9"', 0.00389646534929029),
			('P:"LP"', 0.00361814639576955),
			('103:"wa_30148"', 0.00333982744224882),
			('D:"D"', 0.00333982744224882),
			('LAW:"14"', 0.00333982744224882),
			('AMA:"7"', 0.00306150848872808),
			('CAR:"40"', 0.00278318953520735),
		]
        return faker.random_element(elements=OrderedDict(_map_all_field_iterations_frequency))
    def _use_regex():
        _use_regex_frequency = [
			('0', 0.674625208217657),
			('4:"4"', 0.0330372015546918),
			('E:"0"', 0.0327595780122154),
			(' "(?i).*ACCESS SERVICES.*": "301"', 0.0294280955024986),
			(' "(?i)^ED$": "0"', 0.0294280955024986),
			(' "(?i).*URGENT CARE.*": "3"', 0.0252637423653526),
			('SV:"4"', 0.0224875069405886),
			('NULL', 0.0208217656857301),
			('HOME:"PRN"', 0.0152692948362021),
			('FEMALE:"2"', 0.0147140477512493),
			(' "IA": "I10"', 0.0127706829539145),
			('DF:"F"', 0.0111049416990561),
			('MA:"MA"', 0.00943920044419767),
			('5:"7"', 0.00805108273181566),
			('(?i)^WHF.*:"hfh"', 0.00694058856191005),
			('S:"S"', 0.00527484730705164),
			('97006004:"King County Public Health"', 0.00471960022209883),
			('40:"40"', 0.00444197667962243),
			('IA:"I10"', 0.00388672959466963),
			('1', 0.00360910605219323),
			('INO:"11"', 0.00360910605219323),
			('105:"wa_30348"', 0.00333148250971682),
			('4:"13"', 0.00305385896724042),
			('4:"85"', 0.00277623542476402),
			('4:"3"', 0.00249861188228762),
			('ACF:"348"', 0.00249861188228762),
			('ASC:"65"', 0.00249861188228762),
			('CARDIOLOGY:"40"', 0.00249861188228762),
			('OBSERVATION:"11"', 0.00249861188228762),
			(' "(?i).*SURGERY.*": "33"', 0.00222098833981122),
			(' "I10": "I10"', 0.00222098833981122),
			('AAGASTRO:"MD_1154311017"', 0.00222098833981122),
		]
        return faker.random_element(elements=OrderedDict(_use_regex_frequency))
    def _hl7_groovy_script_id():
        _hl7_groovy_script_id_frequency = [
			('NULL', 0.66993006993007),
			('0', 0.0422377622377622),
			(' "(?i).*ADVANCED WOUND CARE.*": "38"', 0.0296503496503497),
			(' "(?i)^ED .*": "0"', 0.0296503496503497),
			('I/P:"2"', 0.0293706293706294),
			('5:"5"', 0.0257342657342657),
			(' "(?i).* PSY.*": "237"', 0.0251748251748252),
			('MO:"3"', 0.0226573426573427),
			('CELL:"CEL"', 0.0153846153846154),
			(' "I10": "I10"', 0.0125874125874126),
			('A:"A"', 0.0111888111888112),
			('U:"0"}"', 0.0109090909090909),
			('MISC:"MA"', 0.00951048951048951),
			('(?i)^WSH.*:"shm"', 0.00699300699300699),
			('5:"73"', 0.00587412587412587),
			('U:"UN"', 0.00531468531468531),
			('41:"41"', 0.00447552447552448),
			('6:"13"', 0.0041958041958042),
			('EMERGENCY:"0"', 0.00391608391608392),
			('I10:"I10"', 0.00391608391608392),
			('1', 0.00363636363636364),
			('113:"wa_11301"', 0.00335664335664336),
			('137005001:"Desert AIDS Project"', 0.0027972027972028),
			('5:"243"', 0.0027972027972028),
			('5:"7"', 0.0027972027972028),
			('ACH:"40"', 0.00251748251748252),
			(' "SNM": "SNM"', 0.00223776223776224),
			('AAMC:"MD_1043554967"', 0.00223776223776224),
			('CAR:"40"', 0.00223776223776224),
			('E:"20"', 0.00223776223776224),
			('ICU:"24"', 0.00223776223776224),
			('LCHC:"or_1114978582"', 0.00223776223776224),
		]
        return faker.random_element(elements=OrderedDict(_hl7_groovy_script_id_frequency))
    def _group_name():
        _group_name_frequency = [
			('NULL', 0.630748299319728),
			('CARE_PROVIDER_LIST', 0.0571428571428571),
			('0', 0.0348299319727891),
			('6:"6"', 0.0318367346938776),
			(' "(?i).*ALLERGY.*": "206"', 0.028843537414966),
			(' "(?i)^ER .*": "0"', 0.028843537414966),
			('IP:"2"', 0.0285714285714286),
			(' "(?i).*PSY .*": "237"', 0.0244897959183673),
			('MI:"2"', 0.0220408163265306),
			('W:"W"', 0.0168707482993197),
			('WORK:"WPN"', 0.0149659863945578),
			(' "SNM": "SNM"', 0.0122448979591837),
			('DRUG ALLERGY:"DA"', 0.00925170068027211),
			('8:"14"', 0.00789115646258503),
			('(?i)^WCH.*:"c"', 0.00680272108843537),
			('42:"42"', 0.00435374149659864),
			('1', 0.00380952380952381),
			('SNM:"SNM"', 0.00380952380952381),
			('301:"wa_30148"', 0.00326530612244898),
			('HOME-HEALTH:"6"', 0.00299319727891156),
			('146002002:"CAS GARLINGTON CAM"', 0.00272108843537415),
			('ACS:"7"', 0.00244897959183673),
			('U:"UN"', 0.00244897959183673),
			(' "ICD9": "I9"', 0.00217687074829932),
			('ABH_ES:"md_1912039017"', 0.00217687074829932),
			('CFHC:"1366790008"', 0.00217687074829932),
			('GENERAL MED:"285"', 0.00217687074829932),
			('I:"2"', 0.00217687074829932),
			('LAW:"14"', 0.00217687074829932),
			('6:"13"', 0.0019047619047619),
			('7:"1"', 0.0019047619047619),
			('9:"-1"', 0.0019047619047619),
		]
        return faker.random_element(elements=OrderedDict(_group_name_frequency))
    def _ignore_unmapped():
        _ignore_unmapped_frequency = [
			('0', 0.67956698240866),
			('NULL', 0.0600811907983762),
			('7:"7"', 0.0313937753721245),
			(' "(?i).* ED .*": "0"', 0.0286874154262517),
			(' "(?i).*ALZHEIMERS.*": "216"', 0.0286874154262517),
			('O/P:"3"', 0.0284167794316644),
			(' "(?i).*PSYCH.*": "237"', 0.0243572395128552),
			('LOW:"2"', 0.0219215155615697),
			(' "ICD9": "I9"', 0.0121786197564276),
			('D:"F"', 0.0102841677943166),
			('FOOD ALLERGY:"FA"', 0.00920162381596752),
			('9:"0"', 0.00622462787550744),
			('43:"75"', 0.00487144790257104),
			('(?i)^WSP((?!COMCNTR).)*:"o"', 0.00433017591339648),
			('ICD9:"I9"', 0.00378890392422192),
			('8:"14"', 0.00351826792963464),
			('303:"wa_30348"', 0.00324763193504736),
			('E:"0"', 0.00324763193504736),
			('TEL:"PRN"}"', 0.00324763193504736),
			('1', 0.00297699594046008),
			('LEFT AGAINST:"7"', 0.00297699594046008),
			('PH:"PRN"', 0.00297699594046008),
			('PH:"PRN"}"', 0.00297699594046008),
			('NEW:"85"', 0.0027063599458728),
			('(?i)^WSP.*:"o"', 0.00243572395128552),
			('AFB:"40"', 0.00243572395128552),
			('GERIATRICS:"310"', 0.00243572395128552),
			(' "ICD-9": "I9"', 0.00216508795669824),
			('ABH_R:"MD_1497751135"', 0.00216508795669824),
			('AMA:"7"', 0.00216508795669824),
			('CARE_PROVIDER_LIST', 0.00216508795669824),
			('OHSUR:"OHSU RICHMOND FM"', 0.00216508795669824),
		]
        return faker.random_element(elements=OrderedDict(_ignore_unmapped_frequency))

    id:str = field(default_factory=_uuid4) # char(36) PK 
    facility_id:str = field(default_factory=_uuid4) # char(36) 
    name:str = field(default_factory=_name_) # varchar(45) 
    segment:str = field(default_factory=_segment) # char(3) 
    segment_iteration:int = field(default_factory=_segment_iteration) # tinyint(4) 
    _field:int = field(default_factory=_field_) # tinyint(4) 
    field_iteration:str = field(default_factory=_field_iteration) # tinyint(4) 
    component:str = field(default_factory=_component) # tinyint(4) 
    subcomponent:str = field(default_factory=_subcomponent) # tinyint(4) 
    created_on:str = field(default_factory=_past_date) # datetime 
    created_by:str = field(default_factory=_uuid4) # char(36) 
    deleted_on:str = field(default_factory=_past_date) # datetime 
    deleted_by:str = field(default_factory=_deleted_by) # char(36) 
    translation:str = field(default_factory=_translation) # mediumtext 
    default_value:str = field(default_factory=_default_value) # char(36) 
    map_all_field_iterations:str = field(default_factory=_map_all_field_iterations) # tinyint(4) 
    use_regex:str = field(default_factory=_use_regex) # tinyint(1) 
    hl7_groovy_script_id:str = field(default_factory=_hl7_groovy_script_id) # char(36) 
    group_name:str = field(default_factory=_group_name) # varchar(45) 
    ignore_unmapped:str = field(default_factory=_ignore_unmapped) # tinyint(1)

@dataclass
class DxCodeDataClass(DataClassDF):
    '''Defines a data class for generating synthetic data related to 
    diagnosis code information. It provides attributes to store various 
    details such as identifiers, code value, method, description, 
    non-emergent status, classification, version, creation and modification 
    timestamps, and billability of the diagnosis code.'''
    def _method():
        _method_frequency = [
			('I10', 0.814),
			('SNM', 0.186),
		]
        return faker.random_element(elements=OrderedDict(_method_frequency))
    def _is_billable():
        _is_billable_frequency = [
			('1', 0.6542),
			(None, 0.186),
			('0', 0.1598),
		]
        return faker.random_element(elements=OrderedDict(_is_billable_frequency))

    id:str = field(default_factory=_uuid4) # varchar(36) PK
    code:str = field(default_factory=_int) # varchar(45)
    method:str = field(default_factory=_method) # varchar(12)
    description:str = field(default_factory=faker.sentence(nb_words=15)) # varchar(255)
    wa_non_emergent:str = field(default=0) # tinyint(1)
    status:str = field(default=None) # varchar(255)
    version:str = field(default=None) # varchar(255)
    created_on:str = field(default_factory=_past_date) # timestamp
    modified_on:str = field(default_factory=_past_date) # timestamp
    is_billable:str = field(default_factory=_is_billable) # bit(1)