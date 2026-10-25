from fastapi import FastAPI
from pydantic import BaseModel
from security.analyzer import analyze_security_headers
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
        response_time = round(time.time() - start_time, 3)

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
            "security_analysis": security_analysis
        }

    except requests.RequestException as e:
        return {
            "url": data.url,
            "error": str(e)
        }