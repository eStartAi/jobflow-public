import requests

TIMEOUT = 5


def check_lever(company):
    """
    Check if company uses Lever ATS
    """
    url = f"https://api.lever.co/v0/postings/{company}?mode=json"

    try:
        response = requests.get(url, timeout=TIMEOUT)

        if response.status_code == 200:
            data = response.json()
            return True, len(data)

        elif response.status_code == 404:
            return False, 0

        else:
            return False, 0

    except requests.exceptions.RequestException:
        return False, 0


def check_greenhouse(company):
    """
    Check if company uses Greenhouse ATS
    """
    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

    try:
        response = requests.get(url, timeout=TIMEOUT)

        if response.status_code == 200:
            data = response.json()
            jobs = data.get("jobs", [])
            return True, len(jobs)

        elif response.status_code == 404:
            return False, 0

        else:
            return False, 0

    except requests.exceptions.RequestException:
        return False, 0
