import time

def fetch_all_violations():
    global CACHE

    # if cached within 5 min → reuse
    if CACHE["data"] and (time.time() - CACHE["last_fetch"] < 300):
        print("⚡ Using cached data...")
        return CACHE["data"]

    print("🌐 Fetching from CBMT APIs...")

    severities = ["HighMedium", "Low"]
    all_violations = []
    all_summary = []

    for sev in severities:
        endpoint = f"/itop2/public/report/weekly/violations/{sev}"
        url = BASE_URL + endpoint

        response = requests.get(url, headers=HEADERS, verify=CERT_PATH)
        res_json = response.json()
        data = res_json.get("data", {})

        all_violations.extend(data.get("violationList", []))
        all_summary.extend(data.get("summary", []))

    # save cache
    CACHE["data"] = {
        "violations": all_violations,
        "summary": all_summary
    }
    CACHE["last_fetch"] = time.time()

    return CACHE["data"]
