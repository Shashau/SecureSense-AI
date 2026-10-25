SECURITY_HEADERS = {
    "X-Content-Type-Options": {
        "weight": 20,
        "recommendation": "Add X-Content-Type-Options: nosniff"
    },
    "X-Frame-Options": {
        "weight": 20,
        "recommendation": "Add X-Frame-Options: DENY or SAMEORIGIN"
    },
    "Content-Security-Policy": {
        "weight": 30,
        "recommendation": "Implement a suitable Content-Security-Policy"
    }
}


def analyze_security_headers(headers):
    findings = []
    score = 100

    for header, info in SECURITY_HEADERS.items():
        if not headers.get(header):
            score -= info["weight"]

            findings.append({
                "header": header,
                "status": "Missing",
                "severity": "Medium",
                "recommendation": info["recommendation"]
            })
        else:
            findings.append({
                "header": header,
                "status": "Present",
                "severity": "Low",
                "recommendation": "No action required"
            })

    if score >= 80:
        risk_level = "Low"
    elif score >= 50:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return {
        "security_score": max(score, 0),
        "risk_level": risk_level,
        "findings": findings
    }