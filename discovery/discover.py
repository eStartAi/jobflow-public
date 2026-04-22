import sys
import os
import json
import concurrent.futures

# ✅ FIX PATH (works from anywhere)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ✅ CORRECT IMPORTS
from discovery.fetch_companies import fetch_company_list
from discovery.detectors import check_greenhouse, check_lever

# 🔧 CONFIG
MAX_COMPANIES = 250


# ---------------------------
# 🔍 DETECTION LOGIC
# ---------------------------
def detect_company(company):
    try:
        if check_greenhouse(company):
            return ("greenhouse", company)

        if check_lever(company):
            return ("lever", company)

    except Exception as e:
        print(f"⚠️ Error checking {company}: {e}")

    return None


# ---------------------------
# 🚀 MAIN DISCOVERY
# ---------------------------
def run_discovery():
    print("🌐 Fetching HIGH-QUALITY companies...")

    companies = fetch_company_list()

    print(f"✅ Filtered companies: {len(companies)}")

    # 🔥 LIMIT EARLY (PERFORMANCE CONTROL)
    companies = companies[:MAX_COMPANIES]

    greenhouse = []
    lever = []

    print("🚀 Running FAST ATS Discovery...\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        results = executor.map(detect_company, companies)

        for result in results:
            if not result:
                continue

            kind, name = result

            if kind == "greenhouse":
                greenhouse.append(name)
                print(f"✅ {name} → greenhouse")

            elif kind == "lever":
                lever.append(name)
                print(f"✅ {name} → lever")

    output = {
        "greenhouse": greenhouse,
        "lever": lever
    }

    # ✅ SAVE OUTPUT
    output_path = os.path.join(os.path.dirname(__file__), "output.json")

    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print("\n✅ FAST Discovery Complete")
    print(f"Greenhouse: {len(greenhouse)}")
    print(f"Lever: {len(lever)}")


# ---------------------------
# ▶ ENTRY
# ---------------------------
if __name__ == "__main__":
    run_discovery()
