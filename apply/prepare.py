import os
import json
from datetime import datetime

from ai.resume_tailor import tailor_resume
from ai.qa_generator import generate_answers
from ai.cover_letter import generate_cover_letter
from ai.pdf_resume import generate_pdf_resume


OUTPUT_DIR = "outputs/applications"
BASE_RESUME_PATH = "resume.txt"


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def save_file(path, content):
    with open(path, "w") as f:
        f.write(content)


def prepare_application(job):
    company = job.get("company", "unknown").replace(" ", "_")
    title = job.get("title", "role").replace(" ", "_")

    folder_name = f"{company}_{title}"
    folder_path = os.path.join(OUTPUT_DIR, folder_name)

    ensure_dir(folder_path)

    # Save raw job data
    save_file(
        os.path.join(folder_path, "job.json"),
        json.dumps(job, indent=2)
    )

    # Save apply link
    save_file(
        os.path.join(folder_path, "link.txt"),
        job.get("apply_url", "")
    )

    return folder_path


def run():
    # Check required files
    if not os.path.exists("outputs/hot_jobs.json"):
        print("❌ Missing outputs/hot_jobs.json — run main.py first")
        return

    if not os.path.exists(BASE_RESUME_PATH):
        print("❌ Missing resume.txt — create your base resume file")
        return

    with open("outputs/hot_jobs.json") as f:
        jobs = json.load(f)

    with open(BASE_RESUME_PATH) as f:
        base_resume = f.read()

    print(f"🚀 Preparing applications for {len(jobs)} jobs...")

    created = []

    for job in jobs[:5]:  # 🔥 LIMIT TO TOP 5 (HIGH QUALITY)
        path = prepare_application(job)

        # =========================
        # 🧠 AI GENERATED CONTENT
        # =========================

        # Answers
        answers = generate_answers(job)
        save_file(os.path.join(path, "answers.txt"), answers)

        # Cover Letter
        cover = generate_cover_letter(job)
        save_file(os.path.join(path, "cover_letter.txt"), cover)

        # Tailored Resume
        tailored = tailor_resume(job, base_resume)

        # Save TXT version (optional)
        save_file(os.path.join(path, "resume.txt"), tailored)

        # Save PDF version (MAIN)
        pdf_path = os.path.join(path, "resume.pdf")
        generate_pdf_resume(tailored, pdf_path)

        created.append(path)

    print("\n✅ Applications prepared:\n")

    for p in created:
        print(f"📂 {p}")

    print("\n🎯 DONE — Ready to apply!")


if __name__ == "__main__":
    run()
