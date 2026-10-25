from security.analyzer import (
    analyze_security_headers,
    check_https,
    check_server_disclosure
)


def test_security_headers_all_present():

    headers = {
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "Content-Security-Policy": "default-src 'self'"
    }

    result = analyze_security_headers(headers)

    assert result["security_score"] == 100
    assert result["risk_level"] == "Low"


def test_security_headers_missing():

    headers = {}

    result = analyze_security_headers(headers)

    assert result["security_score"] == 30
    assert result["risk_level"] == "High"


def test_https_secure():

    result = check_https("https://example.com")

    assert result["status"] == "Secure"


def test_https_insecure():

    result = check_https("http://example.com")

    assert result["status"] == "Insecure"


def test_server_disclosure():

    result = check_server_disclosure("nginx")

    assert result["status"] == "Detected"


def test_server_not_disclosed():

    result = check_server_disclosure(None)

    assert result["status"] == "Not Detected"