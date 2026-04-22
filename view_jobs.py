import json

try:
    with open("outputs/hot_jobs.json") as f:
        jobs = json.load(f)
except FileNotFoundError:
    print("❌ No hot_jobs.json found. Run main.py first.")
    exit()

print("\n🔥 YOUR DAILY JOB LIST\n")

if not jobs:
    print("⚠️ No jobs found.")
    exit()

for i, job in enumerate(jobs[:20], 1):
    print(f"{i}. [{job.get('score', 0)}] {job.get('title', 'N/A')}")
    print(f"   🏢 {job.get('company', 'N/A')}")
    print(f"   📍 {job.get('location', 'N/A')}")
    print()
