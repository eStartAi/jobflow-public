from pipeline.normalize import normalize_jobs
from pipeline.fast_filter import fast_filter
from pipeline.devops_filter import is_devops_job
from pipeline.score import score_job


def run_pipeline(jobs):
    print(f"\n📊 Total Jobs Collected (before filter): {len(jobs)}")

    if not jobs:
        print("⚠️ No jobs found — check sources or company list")
        return

    # ================================
    # 1. Normalize
    # ================================
    jobs = normalize_jobs(jobs)

    # ================================
    # 2. FAST FILTER
    # ================================
    jobs = [job for job in jobs if fast_filter(job)]
    print(f"⚡ After FAST filter: {len(jobs)}")

    if not jobs:
        return

    # ================================
    # 3. DEVOPS FILTER
    # ================================
    config = {
        "target_roles": [
            "devops",
            "site reliability",
            "sre",
            "infrastructure engineer",
            "platform engineer",
            "systems engineer",
            "technical support engineer",
            "support engineer",
            "operations engineer",
            "production engineer"
        ],
        "exclude_keywords": [
            "senior", "staff", "principal",
            "manager", "director", "lead"
        ]
    }

    jobs = [job for job in jobs if is_devops_job(job, config)]
    print(f"🎯 After DevOps filter: {len(jobs)}")

    if not jobs:
        return

    # ================================
    # 4. LOCATION FILTER (FINAL)
    # ================================
    def is_valid_location(job):
        location = job.get("location", "").lower()

        # ✅ allow remote (unless restricted)
        if "remote" in location:
            BAD_REMOTE = [
                "india", "china", "korea", "japan",
                "brazil", "argentina", "philippines",
                "latam", "emea", "apac", "europe only"
            ]
            if any(bad in location for bad in BAD_REMOTE):
                return False
            return True

        # ✅ allow US
        US_KEYWORDS = [
            "united states", "usa",
            "new york", "california", "texas",
            "florida", "washington", "virginia",
            "pennsylvania", "illinois", "colorado"
        ]

        if any(word in location for word in US_KEYWORDS):
            return True

        return False

    jobs = [job for job in jobs if is_valid_location(job)]
    print(f"🌍 After Location filter: {len(jobs)}")

    if not jobs:
        return

    # ================================
    # 5. SCORING
    # ================================
    scored_jobs = []

    for job in jobs:
        score = score_job(job)
        if score >= 25:
            job["score"] = score
            scored_jobs.append(job)

    print(f"🔥 After Scoring (≥25): {len(scored_jobs)}")

    if not scored_jobs:
        return

    # ================================
    # 6. SORT + OUTPUT
    # ================================
    scored_jobs.sort(key=lambda x: x["score"], reverse=True)

    print("\n🔥 Top Jobs:\n")

    for job in scored_jobs[:10]:
        print(f'{job["score"]} | {job["title"]} | {job["company"]} | {job["location"]}')

    return scored_jobs
