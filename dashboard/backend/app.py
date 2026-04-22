from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import json

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

# -------------------------
# GET JOBS
# -------------------------
@app.route("/jobs", methods=["GET"])
def get_jobs():
    try:
        with open("../../outputs/hot_jobs.json") as f:
            jobs = json.load(f)
        return jsonify(jobs)
    except Exception as e:
        return jsonify({"error": str(e)})


# -------------------------
# 🤖 GENERATE RESUME
# -------------------------
@app.route("/generate", methods=["POST"])
def generate():
    job = request.json.get("job", {})

    prompt = f"""
Create a strong 1-page resume:

Title: {job.get("title")}
Company: {job.get("company")}
Description: {job.get("description", "")}

Candidate:
- DevOps / Cloud Support
- Linux, AWS EC2, SSH
- Python automation, APIs
- Docker, CI/CD

Make it ATS optimized.
"""

    try:
        res = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return jsonify({
            "success": True,
            "output": res.choices[0].message.content
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


# -------------------------
# 💬 GENERATE ANSWERS
# -------------------------
@app.route("/answers", methods=["POST"])
def answers():
    job = request.json.get("job", {})

    prompt = f"""
Generate answers:

Job: {job.get("title")} at {job.get("company")}

1. Why do you want this role?
2. Why are you a good fit?
3. Relevant experience?
"""

    try:
        res = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return jsonify({
            "success": True,
            "output": res.choices[0].message.content
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


# -------------------------
# RUN
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
