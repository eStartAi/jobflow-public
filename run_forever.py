import time
from main import main

INTERVAL = 1800  # 30 minutes

while True:
    print("\n⏱️ Running job scan cycle...\n")

    try:
        main()
    except Exception as e:
        print(f"❌ Crash: {e}")

    print(f"\n😴 Sleeping for {INTERVAL/60} minutes...\n")
    time.sleep(INTERVAL)
