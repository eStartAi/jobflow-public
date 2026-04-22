# ================================
# JobFlow MAIN (FINAL - FIXED)
# ================================

from utils.parallel_fetch import parallel_fetch
from sources.lever import fetch_lever_jobs
from sources.greenhouse import fetch_greenhouse_jobs
from config.companies import get_active_companies
from run_pipeline import run_pipeline


def build_tasks():
    tasks = []

    companies = get_active_companies()

    # ✅ CORRECT WAY (DICT ACCESS)
    lever_companies = companies.get("lever", [])
    greenhouse_companies = companies.get("greenhouse", [])

    print(f"🔎 Lever companies: {len(lever_companies)}")
    print(f"🔎 Greenhouse companies: {len(greenhouse_companies)}")

    # ================================
    # SAFETY FIX (prevents letter bug)
    # ================================
    if isinstance(lever_companies, str):
        lever_companies = [lever_companies]

    if isinstance(greenhouse_companies, str):
        greenhouse_companies = [greenhouse_companies]

    # ================================
    # BUILD TASKS
    # ================================
    for company in lever_companies:
        tasks.append(lambda c=company: fetch_lever_jobs(c))

    for company in greenhouse_companies:
        tasks.append(lambda c=company: fetch_greenhouse_jobs(c))

    return tasks


def main():
    print("🚀 JobFlow TURBO Started...")

    tasks = build_tasks()

    # ================================
    # PARALLEL FETCH
    # ================================
    all_jobs = parallel_fetch(tasks, max_workers=6)

    print(f"\n📊 Total Jobs Collected: {len(all_jobs)}")

    if not all_jobs:
        print("⚠️ No jobs collected — check sources/config")
        return

    # ================================
    # RUN PIPELINE
    # ================================
    run_pipeline(all_jobs)


if __name__ == "__main__":
    main()
