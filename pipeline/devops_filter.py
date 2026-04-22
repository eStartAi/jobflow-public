def is_devops_job(job, config):
    title = job.get("title", "").lower()

    # ================================
    # ❌ HARD EXCLUDE (software-heavy roles)
    # ================================
    if any(word in title for word in [
        "software engineer",
        "frontend",
        "backend",
        "full stack",
        "machine learning",
        "ai engineer",
        "data engineer",
        "data platform",
        "data infrastructure"
    ]):
        return False

    # ================================
    # ❌ EXCLUDE SENIOR
    # ================================
    if any(word in title for word in [
        "senior", "staff", "principal",
        "director", "manager", "lead"
    ]):
        return False

    # ================================
    # ✅ STRICT TARGET ROLES
    # ================================
    TARGET = [
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
    ]

    # must match at least one target role
    if not any(role in title for role in TARGET):
        return False

    return True
