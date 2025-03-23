from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from config import DB_CONFIG

# PostgreSQL
db = SQLAlchemy()

def init_postgres(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{DB_CONFIG["POSTGRES"]["user"]}:{DB_CONFIG["POSTGRES"]["password"]}@{DB_CONFIG["POSTGRES"]["host"]}/{DB_CONFIG["POSTGRES"]["dbname"]}'
    db.init_app(app)

# MongoDB
mongo_client = MongoClient(DB_CONFIG["MONGO_URI"])
mongo_db = mongo_client["resume_screening"]
resume_collection = mongo_db["resumes"]
 
