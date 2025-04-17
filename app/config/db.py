""" import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData

# Loading environment variables from the .env file
load_dotenv()

# Get database credentials from environment variables
DB_USERNAME = os.getenv('MYSQL_ADDON_USER')
DB_PASSWORD = os.getenv('MYSQL_ADDON_PASSWORD')
DB_HOST = os.getenv('MYSQL_ADDON_HOST')
DB_PORT = os.getenv('MYSQL_ADDON_PORT')
DB_NAME = os.getenv('MYSQL_ADDON_DB')

print(f'DB_USERNAME: {DB_USERNAME}')
print(f'DB_PASSWORD: {DB_PASSWORD}')
print(f'DB_HOST: {DB_HOST}')
print(f'DB_PORT: {DB_PORT}')
print(f'DB_NAME: {DB_NAME}')

# Create a connection string
# connect to local base
engine = create_engine('mysql+pymysql://root:@localhost:3306/storedb')

# connect to cloud base
# engine = create_engine(f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

meta = MetaData()

conn = engine.connect() """