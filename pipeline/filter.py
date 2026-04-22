def is_valid_job(job, config):
    title = job.get("title", "").lower()
    location = (job.get("location") or "").lower()

    if not title:
        return False

    # =========================
    # ❌ EXCLUDE BAD ROLES
    # =========================
    exclude = config.get("exclude_keywords", [])
    for word in exclude:
        if word.lower() in title:
            return False

    # =========================
    # 🌍 LOCATION (RELAXED)
    # =========================
    if config.get("locations"):
        if not any(loc.lower() in location for loc in config["locations"]):
            # allow remote
            if "remote" not in location:
                return False

    # =========================
    # ✅ ROLE MATCH (RELAXED)
    # =========================
    ROLE_KEYWORDS = [
        "devops",
        "cloud",
        "sre",
        "site reliability",
        "platform",
        "infrastructure",
        "backend",
        "software engineer",
        "data engineer"
    ]

    if not any(k in title for k in ROLE_KEYWORDS):
        return False

    return True
