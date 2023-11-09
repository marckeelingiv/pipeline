from sqlalchemy import create_engine

# Define the database connection details 
host = '127.0.0.1'
username='your_username'
password='your_password'
database='visit'

# Create a connection string  
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')  