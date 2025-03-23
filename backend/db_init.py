from models import db
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://username:password@localhost:5432/resume_db"
db.init_app(app)

with app.app_context():
    db.create_all()
    print("Database initialized successfully.")
 
