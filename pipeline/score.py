def score_job(job):
    score = 0

    title = job.get("title", "").lower()
    desc = job.get("description", "").lower()
    location = job.get("location", "").lower()

    # 🎯 HIGH VALUE ROLES
    if "devops" in title:
        score += 50
    if "site reliability" in title or "sre" in title:
        score += 45
    if "infrastructure" in title or "platform" in title:
        score += 40
    if "support engineer" in title:
        score += 35
    if "technical support" in title:
        score += 30

    # 🧠 CORE SKILLS
    if "linux" in desc:
        score += 15
    if "aws" in desc or "cloud" in desc:
        score += 15
    if "docker" in desc:
        score += 10
    if "kubernetes" in desc:
        score += 10
    if "ci/cd" in desc:
        score += 10
    if "automation" in desc:
        score += 10

    # 🚀 REMOTE BOOST
    if "remote" in location:
        score += 20

    # ❌ PENALTIES
    if "senior" in title:
        score -= 30
    if "staff" in title or "principal" in title:
        score -= 40

    return score
