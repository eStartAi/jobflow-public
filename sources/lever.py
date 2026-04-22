import requests

def fetch_lever_jobs(company):
    """
    Fetch jobs from Lever API
    """
    url = f"https://api.lever.co/v0/postings/{company}?mode=json"

    try:
        res = requests.get(url, timeout=10)

        if res.status_code != 200:
            print(f"⚠️ Lever failed: {company}")
            return []

        jobs = res.json()

        results = []

        for job in jobs:
            results.append({
                "title": job.get("text"),
                "company": company,
                "location": job.get("categories", {}).get("location", ""),
                "description": "",
                "url": job.get("hostedUrl"),
                "source": "lever"
            })

        print(f"✅ {company} → lever ({len(results)} jobs)")
        return results

    except Exception as e:
        print(f"❌ Lever error: {company} | {e}")
        return []
