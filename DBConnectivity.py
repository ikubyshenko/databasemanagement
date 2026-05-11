import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="DBMSEvent",
    user="postgres",
    password="00000000"
)

cursor = conn.cursor()