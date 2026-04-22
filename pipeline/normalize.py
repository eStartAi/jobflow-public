# ================================
# Job Normalization Layer (FINAL)
# ================================

def normalize_job(job):
    """
    Normalize job data across all sources (Greenhouse, Lever, etc.)
    Ensures consistent structure for pipeline processing
    """

    return {
        "title": job.get("title", "").strip(),

        "company": job.get("company")
        or job.get("company_name")
        or job.get("organization")
        or "Unknown",

        "location": job.get("location")
        or job.get("locations")
        or job.get("city")
        or "Unknown",

        "description": job.get("description")
        or job.get("content")
        or "",

        "url": job.get("url")
        or job.get("apply_url")
        or job.get("absolute_url")
        or "",

        "source": job.get("source", "unknown")
    }


# ================================
# OPTIONAL (SAFE BULK NORMALIZER)
# ================================
def normalize_jobs(jobs):
    return [normalize_job(job) for job in jobs]
