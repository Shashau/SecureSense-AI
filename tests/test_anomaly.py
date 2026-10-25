from security.anomaly import detect_anomaly


def test_normal_response():

    result = detect_anomaly(200, 0.5)

    assert result["anomaly_detected"] is False
    assert result["anomalies"] == []


def test_slow_response():

    result = detect_anomaly(200, 3)

    assert result["anomaly_detected"] is True
    assert result["anomalies"][0]["type"] == "Slow Response"


def test_server_error():

    result = detect_anomaly(500, 0.5)

    assert result["anomaly_detected"] is True
    assert result["anomalies"][0]["type"] == "Server Error"


def test_rate_limit():

    result = detect_anomaly(429, 0.5)

    assert result["anomaly_detected"] is True
    assert result["anomalies"][0]["type"] == "Rate Limit"


def test_redirect():

    result = detect_anomaly(302, 0.5)

    assert result["anomaly_detected"] is True
    assert result["anomalies"][0]["type"] == "Redirect"


def test_client_error():

    result = detect_anomaly(404, 0.5)

    assert result["anomaly_detected"] is True
    assert result["anomalies"][0]["type"] == "Client Error"