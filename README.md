@api.route("/violations/filter/<gbgf>", methods=["GET"])
def filter_by_gbgf(gbgf):
    try:
        severities = ["HighMedium", "Low"]

        all_violations = []
        total_applications = 0
        total_assets = 0

        for sev in severities:
            endpoint = f"/itop2/public/report/weekly/violations/{sev}"
            url = BASE_URL + endpoint

            response = requests.get(
                url,
                headers=HEADERS,
                verify=CERT_PATH
            )

            res_json = response.json()

            data = res_json.get("data", {})

            # ✅ Get violations
            violations = data.get("violationList", [])
            all_violations.extend(violations)

            # ✅ Get summary totals
            summary = data.get("summary", [])

            for item in summary:
                if item.get("gbgf", "").lower() == gbgf.lower():
                    total_applications += item.get("totalApplication", 0)
                    total_assets += item.get("totalAsset", 0)

        # ✅ Filter violations by gbgf
        filtered = [
            v for v in all_violations
            if str(v.get("gbgf", "")).lower() == gbgf.lower()
        ]

        return jsonify({
            "gbgf": gbgf,
            "totalViolations": len(filtered),
            "totalApplications": total_applications,
            "totalAssets": total_assets,
            "violations": filtered
        })

    except Exception as e:
        return jsonify({"error": str(e)})


from flask import request

@api.route("/violations", methods=["GET"])
def filter_violations():
    try:
        gbgf = request.args.get("gbgf")
        gbgf_function = request.args.get("function")

        severities = ["HighMedium", "Low"]

        all_violations = []
        total_applications = 0
        total_assets = 0

        for sev in severities:
            endpoint = f"/itop2/public/report/weekly/violations/{sev}"
            url = BASE_URL + endpoint

            response = requests.get(
                url,
                headers=HEADERS,
                verify=CERT_PATH
            )

            res_json = response.json()
            data = res_json.get("data", {})

            violations = data.get("violationList", [])
            all_violations.extend(violations)

            summary = data.get("summary", [])

            if gbgf:
                for item in summary:
                    if item.get("gbgf", "").lower() == gbgf.lower():
                        total_applications += item.get("totalApplication", 0)
                        total_assets += item.get("totalAsset", 0)

        # 🔥 Filtering logic
        filtered = all_violations

        if gbgf:
            filtered = [
                v for v in filtered
                if str(v.get("gbgf", "")).lower() == gbgf.lower()
            ]

        if gbgf_function:
            filtered = [
                v for v in filtered
                if str(v.get("gbgfFunction", "")).lower() == gbgf_function.lower()
            ]

        return jsonify({
            "gbgf": gbgf,
            "gbgfFunction": gbgf_function,
            "totalViolations": len(filtered),
            "totalApplications": total_applications,
            "totalAssets": total_assets,
            "violations": filtered
        })

    except Exception as e:
        return jsonify({"error": str(e)})

