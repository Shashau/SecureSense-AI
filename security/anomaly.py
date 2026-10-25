def detect_anomaly(status_code, response_time):
    anomalies = []

    if response_time > 2:
        anomalies.append({
            "type": "Slow Response",
            "severity": "Medium",
            "message": "API response time is unusually high."
        })

    if status_code >= 500:
        anomalies.append({
            "type": "Server Error",
            "severity": "High",
            "message": "API returned a server-side error."
        })

    if status_code == 429:
        anomalies.append({
            "type": "Rate Limit",
            "severity": "Medium",
            "message": "API rate limit may have been triggered."
        })

    if 300 <= status_code < 400:
        anomalies.append({
            "type": "Redirect",
            "severity": "Low",
            "message": "API returned a redirect response."
        })

    if 400 <= status_code < 500:
        anomalies.append({
            "type": "Client Error",
            "severity": "Medium",
            "message": "API returned a client-side error."
        })

    return {
        "anomaly_detected": len(anomalies) > 0,
        "anomalies": anomalies
    }