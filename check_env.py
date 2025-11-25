import os
from dotenv import load_dotenv

print("Directorio actual:", os.getcwd())

load_dotenv()

print("DATABASE_URL:", os.getenv("DATABASE_URL"))

print("Archivos en este directorio:", os.listdir())
