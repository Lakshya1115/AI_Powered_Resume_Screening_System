from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import pdfplumber
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load AI model for skill extraction
skill_extractor = pipeline("ner", model="dslim/bert-base-NER")

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload_resume", methods=["POST"])
def upload_resume():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Extract text from PDF
    with pdfplumber.open(filepath) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

    # Extract skills
    skills = [ent["word"] for ent in skill_extractor(text) if ent["entity"] == "B-SKILL"]
    
    return jsonify({"skills": list(set(skills))})

if __name__ == "__main__":
    app.run(debug=True)
 
