from dotenv import load_dotenv

load_dotenv()

from sqlalchemy import create_engine
import sqlalchemy
import pandas as pd
import os


MYSQL_HOSTNAME = '35.188.202.5' # you probably don't need to change this

MYSQL_USER = os.getenv('MYSQL_USER')

MYSQL_PASSWORD = os.getenv('MYSQL_password')

MYSQL_DATABASE = 'db1'

# creating a concatenated string of variables that sql alchemy can use to connect to a db
connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'

db = create_engine(connection_string)

query = 'SELECT * FROM db1.patients;'

patients_df = pd.read_sql(query, con=db)
patients_df

real_df = pd.read_csv('/Users/brittanykusi-gyabaah/Desktop/AHI/HHA-507-2022-main/ingestion/example_files/csv/synthetic/allergies.csv')
real_df

real_df.to_sql('patients', con=db, if_exists='replace')