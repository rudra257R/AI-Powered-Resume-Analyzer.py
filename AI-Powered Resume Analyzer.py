from flask import Flask,render_template,request
from flask import Flask
import pdfplumber
import os

print("Current File:", __file__)
print("Current Directory:", os.path.dirname(os.path.abspath(__file__)))

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print("BASE_DIR =", BASE_DIR)

app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))
print("BASE_DIR =", BASE_DIR)
print("TEMPLATE_FOLDER =", app.template_folder)
print("TEMPLATE EXISTS =", os.path.exists(app.template_folder))
print("FILES =", os.listdir(app.template_folder))
print("TEMPLATE_FOLDER =", os.path.join(BASE_DIR, "templates"))

UPLOAD_FOLDER="upload"
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER

skills_list=[
    "pythin","java","html","c","c++",
    "MongoDB","MySQL","css","javaScript",
    "Flask","git","PHP",
]

def extract_text(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    return text
         
def analyze_resume(text):
    found_skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    score = int((len(found_skills) / len(skills_list)) * 100)

    missing_skills = list(set(skills_list) - set(found_skills))

    return found_skills, missing_skills, score

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze",methods=["post"])
def analyze():
    file = request.files["resume"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    text = extract_text(filepath)

    found_skills, missing_skills, score = analyze_resume(text)

    return render_template(
        "result.html",
        score=score,
        skills=found_skills,
        missing=missing_skills
    )

if __name__ == "__main__":
    app.run(debug=True)
                    