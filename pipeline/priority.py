# pipeline/priority.py

def assign_priority(job):
    score = job.get("score", 0)
    title = job.get("title", "").lower()

    # 🔥 APPLY NOW
    if score >= 20 and any(x in title for x in ["devops", "sre"]):
        job["priority"] = "🔥 APPLY NOW"

    # ⚡ APPLY IF QUALIFIED
    elif score >= 12:
        job["priority"] = "⚡ APPLY IF QUALIFIED"

    # ❌ SKIP
    else:
        job["priority"] = "❌ SKIP"

    return job


def rank_jobs(jobs):
    # assign priority
    jobs = [assign_priority(job) for job in jobs]

    # sort by score
    return sorted(jobs, key=lambda x: x.get("score", 0), reverse=True)
