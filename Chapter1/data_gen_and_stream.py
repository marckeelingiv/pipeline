from pandas import read_sql
from mysql_connection import engine
import random

def pick_random_value(my_list):
    return random.choice(my_list)

# query to get list of facility ids
query='Select id FROM facility'

# convert query to list
id_list = read_sql(sql=query, con=engine)['id'].tolist()

print(id_list)

# use list to set default values when generating more data
# use facility ids, and patient ids
# TODO: get dates to look better