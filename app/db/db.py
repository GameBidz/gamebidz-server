import pymysql
import os
import dotenv

# Load environment variables from the .env file
dotenv.load_dotenv('app/.env')

# Establish a connection to the database
connection = pymysql.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASS"),
    database=os.environ.get("DB_NAME"),
)
