import os
import time
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

config = {
    "host": os.getenv("DB_HOST", "db"),
    "user": os.getenv("DB_USER", "student_user"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME", "student_db"),
    "port": int(os.getenv("DB_PORT", "3306")),
}

connection = None
cursor = None

for attempt in range(30):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor(dictionary=True)
        print("Database Connected Successfully")
        break
    except mysql.connector.Error:
        print(f"Waiting for MySQL... attempt {attempt + 1}/30")
        time.sleep(2)
else:
    raise RuntimeError("Could not connect to MySQL after 60 seconds")
