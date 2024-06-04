import pymysql
import os
import dotenv

# Load environment variables from the .env file
dotenv.load_dotenv('.env')

# Establish a connection to the database
connection = pymysql.connect(
    host=os.environ.get("DATABASE_HOST"),
    user=os.environ.get("DATABASE_USER"),
    password=os.environ.get("DATABASE_PASS"),
    database=os.environ.get("DATABASE_NAME"),
    port=int(os.environ.get("DATABASE_PORT")),
)
