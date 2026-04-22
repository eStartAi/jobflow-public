def fast_filter(job):
    title = job.get("title", "").lower()

    # ❌ remove junk roles
    BAD_KEYWORDS = [
        "recruiter", "sales", "marketing", "finance",
        "hr", "legal", "account", "business", "intern"
    ]

    for word in BAD_KEYWORDS:
        if word in title:
            return False

    return True
