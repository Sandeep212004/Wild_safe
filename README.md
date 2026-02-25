@api.route("/violations/filter/<gbgf>", methods=["GET"])
def filter_by_gbgf(gbgf):
    try:
        severities = ["High", "Medium", "Low"]
        all_violations = []

        for sev in severities:
            endpoint = f"/itop2/public/report/weekly/violations/{sev}"
            url = BASE_URL + endpoint

            response = requests.get(
                url,
                headers=HEADERS,
                verify=CERT_PATH
            )

            data = response.json()

            # extract details array
            details = data.get("details", [])
            all_violations.extend(details)

        # 🔥 filter by gbgf
        filtered = [
            v for v in all_violations
            if str(v.get("gbgf", "")).lower() == gbgf.lower()
        ]

        return jsonify({
            "gbgf": gbgf,
            "total": len(filtered),
            "violations": filtered
        })

    except Exception as e:
        return jsonify({"error": str(e)})


@api.route("/violations/filter/<gbgf>", methods=["GET"])
def filter_by_gbgf(gbgf):
    try:
        severities = ["HighMedium", "Low"]
        all_violations = []

        for sev in severities:
            endpoint = f"/itop2/public/report/weekly/violations/{sev}"
            url = BASE_URL + endpoint

            response = requests.get(
                url,
                headers=HEADERS,
                verify=CERT_PATH
            )

            res_json = response.json()

            # 🔥 extract details correctly
            details = res_json.get("data", {}).get("details", [])

            all_violations.extend(details)

        print("TOTAL violations fetched:", len(all_violations))

        # 🔥 filter by gbgf
        filtered = [
            v for v in all_violations
            if str(v.get("gbgf", "")).lower() == gbgf.lower()
        ]

        return jsonify({
            "gbgf": gbgf,
            "total": len(filtered),
            "violations": filtered
        })

    except Exception as e:
        return jsonify({"error": str(e)})
        
