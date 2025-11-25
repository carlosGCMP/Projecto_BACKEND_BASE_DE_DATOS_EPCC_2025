import psycopg2
from psycopg2 import sql

try:
    conn = psycopg2.connect(
        dbname="plastitex_db",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    print("Conexión exitosa!")
except Exception as e:
    print("Error:", e)
