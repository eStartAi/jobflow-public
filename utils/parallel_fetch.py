from concurrent.futures import ThreadPoolExecutor, as_completed

def parallel_fetch(fetch_tasks, max_workers=5):
    all_jobs = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(task) for task in fetch_tasks]

        for future in as_completed(futures):
            try:
                jobs = future.result()
                if jobs:
                    all_jobs.extend(jobs)
            except Exception as e:
                print(f"⚠️ Fetch error: {e}")

    return all_jobs
