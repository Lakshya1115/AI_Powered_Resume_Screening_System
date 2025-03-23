import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "POSTGRES": {
        "dbname": os.getenv("POSTGRES_DB"),
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "host": os.getenv("POSTGRES_HOST"),
    },
    "MONGO_URI": os.getenv("MONGO_URI"),
}

