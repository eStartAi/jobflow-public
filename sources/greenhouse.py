import requests

def fetch_greenhouse_jobs(company):
    """
    Fetch jobs from Greenhouse public API
    """
    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

    try:
        res = requests.get(url, timeout=10)

        if res.status_code != 200:
            print(f"⚠️ Greenhouse failed: {company}")
            return []

        data = res.json()
        jobs = data.get("jobs", [])

        results = []

        for job in jobs:
            results.append({
                "title": job.get("title"),
                "company": company,
                "location": job.get("location", {}).get("name", ""),
                "description": "",  # skip detail call for speed
                "url": job.get("absolute_url"),
                "source": "greenhouse"
            })

        print(f"✅ {company} → greenhouse ({len(results)} jobs)")
        return results

    except Exception as e:
        print(f"❌ Greenhouse error: {company} | {e}")
        return []
