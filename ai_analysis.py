def generate_security_insight(
    security_score,
    risk_level,
    https_status,
    findings,
    anomalies
):
    insights = []

    if security_score < 50:
        insights.append(
            "The API has a high security risk and requires immediate attention."
        )
    elif security_score < 80:
        insights.append(
            "The API has moderate security weaknesses that should be addressed."
        )
    else:
        insights.append(
            "The API has a strong security configuration."
        )

    if https_status == "Insecure":
        insights.append(
            "HTTPS is not enabled. Sensitive API traffic may be exposed."
        )

    for finding in findings:
        if finding["status"] == "Missing":
            insights.append(
                f"{finding['header']} is missing. "
                f"Recommendation: {finding['recommendation']}"
            )

    for anomaly in anomalies:
        insights.append(
            f"Anomaly detected: {anomaly['type']}. "
            f"{anomaly['message']}"
        )

    return {
        "summary": insights[0],
        "insights": insights,
        "risk_level": risk_level,
        "recommendation_count": len(findings)
    }