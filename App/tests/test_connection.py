from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
print("Usando DATABASE_URL:", DATABASE_URL)

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute("SELECT current_database();")
        print("Conectado a la base de datos:", result.fetchone()[0])
except Exception as e:
    print("Error:", e)
