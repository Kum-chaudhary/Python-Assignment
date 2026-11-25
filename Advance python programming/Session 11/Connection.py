import psycopg2
import os

from dotenv import load_dotenv

load_dotenv()
def get_connection():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        return conn
    except Exception as e:
        print(f"something went wrong while connecting to the database : {e}")
        return None
get_connection()