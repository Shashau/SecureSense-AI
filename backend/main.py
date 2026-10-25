from fastapi import FastAPI
from pydantic import BaseModel
from security.analyzer import (
    analyze_security_headers,
    check_https,
    check_server_disclosure
)
from security.anomaly import detect_anomaly
import requests
import time

app = FastAPI(
    title="SecureSense AI",
    description="API Security & Anomaly Detection Platform",
    version="1.0.0"
)


class APIRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {
        "project": "SecureSense AI",
        "status": "running"
    }


@app.post("/scan")
def scan_api(data: APIRequest):

    start_time = time.time()

    try:
        response = requests.get(data.url, timeout=10)
        security_analysis = analyze_security_headers(response.headers)
        https_analysis = check_https(data.url)

        server_analysis = check_server_disclosure(
        response.headers.get("server")
        )

        response_time = round(time.time() - start_time, 3)
        anomaly_analysis = detect_anomaly(
    response.status_code,
    response_time
)

        return {
            "url": data.url,
            "status_code": response.status_code,
            "response_time": response_time,
            "content_type": response.headers.get("content-type"),
            "server": response.headers.get("server"),
            "security_headers": {
                "X-Content-Type-Options": response.headers.get(
                    "X-Content-Type-Options"
                ),
                "X-Frame-Options": response.headers.get(
                    "X-Frame-Options"
                ),
                "Content-Security-Policy": response.headers.get(
                    "Content-Security-Policy"
                )
            },
            "security_analysis": security_analysis,
            "https_analysis": https_analysis,
            "server_analysis": server_analysis,
            "anomaly_analysis": anomaly_analysis
        }

    except requests.RequestException as e:
        return {
            "url": data.url,
            "error": str(e)
        }