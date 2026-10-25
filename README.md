# 🛡️ SecureSense AI

### Intelligent API Security & Anomaly Detection Platform

SecureSense AI is a lightweight API security assessment platform that analyzes public APIs for common security weaknesses, detects abnormal API responses, and generates actionable security insights.

It combines **API security checks, anomaly detection, response analysis, and an AI-style security insight layer** into a simple web dashboard.

> 🚀 Built for **Hack With Bangalore 4.0**

---

## 🎯 Problem Statement

Modern applications depend heavily on APIs, but APIs can expose security weaknesses such as:

- Missing security headers
- Insecure HTTP connections
- Server information disclosure
- Unexpected HTTP errors
- Slow API responses
- Rate-limit responses
- Redirects and client-side errors

Manually checking these issues across multiple APIs can be time-consuming.

**SecureSense AI provides a simple way to scan an API and understand its security posture in seconds.**

---

## 💡 Solution

SecureSense AI accepts an API URL and performs an automated assessment.

```text
API URL
   ↓
SecureSense AI
   ↓
┌─────────────────────────────┐
│ Security Header Analysis    │
│ HTTPS Security Check        │
│ Server Disclosure Check     │
│ Response Time Analysis      │
│ Anomaly Detection           │
│ Security Insight Generation │
└─────────────────────────────┘
   ↓
Security Dashboard
```

---

## ✨ Key Features

### 🛡️ Security Header Analysis

Checks for important HTTP security headers:

- `X-Content-Type-Options`
- `X-Frame-Options`
- `Content-Security-Policy`

The platform calculates a security score based on missing headers.

### 🔒 HTTPS Detection

Determines whether the scanned API uses HTTPS.

### 🖥️ Server Information Disclosure

Checks whether the API exposes its server information through the `Server` response header.

### 🚨 Anomaly Detection

Detects suspicious or unusual API responses including:

- Slow responses
- HTTP 4xx errors
- HTTP 5xx errors
- Rate limiting (`429`)
- Redirects (`3xx`)

### 🤖 Security Insights

Generates rule-based security insights and recommendations based on the scan results.

> **Note:** The current AI layer is rule-based rather than an external LLM or machine-learning model.

### 📊 Interactive Dashboard

The dashboard displays:

- Security Score
- Risk Level
- HTTPS Status
- Response Time
- API Information
- Security Findings
- Detected Anomalies
- Security Insights

---

## 📈 Security Scoring

SecureSense AI currently uses the following scoring model:

| Security Score | Risk Level |
|---|---|
| 80–100 | 🟢 Low |
| 50–79 | 🟡 Medium |
| 0–49 | 🔴 High |

Security header weights:

| Header | Weight |
|---|---:|
| X-Content-Type-Options | 20 |
| X-Frame-Options | 20 |
| Content-Security-Policy | 30 |

The initial score is **100**, with points deducted when supported security headers are missing.

---

## 🧪 Example Scan

Example API:

```text
https://httpbin.org/get
```

Possible analysis:

```text
Status Code: 200
HTTPS: Secure
Security Score: 30/100
Risk Level: High
```

The result can also identify missing security headers and provide recommendations.

---

## 🧰 Tech Stack

### Backend

- Python
- FastAPI
- Requests
- Pydantic

### Frontend

- HTML
- CSS
- JavaScript

### Testing

- Pytest
- FastAPI TestClient
- HTTPX

### Development

- Git
- GitHub
- macOS / Python virtual environment

---

## 📁 Project Structure

```text
SecureSense-AI/
│
├── analytics/
│
├── backend/
│   └── main.py
│
├── frontend/
│   ├── index.html
│   └── style.css
│
├── security/
│   ├── analyzer.py
│   ├── anomaly.py
│   └── ai_analysis.py
│
├── screenshots/
│
├── tests/
│   ├── __init__.py
│   ├── test_analyzer.py
│   ├── test_anomaly.py
│   └── test_api.py
│
├── TEST_APIS.md
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Shashau/SecureSense-AI.git
```

### 2. Enter the project

```bash
cd SecureSense-AI
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the environment

macOS / Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install fastapi uvicorn requests pydantic pytest httpx
```

---

## ▶️ Run the Backend

From the project root:

```bash
uvicorn backend.main:app --reload
```

The API will start at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🌐 Run the Dashboard

Open:

```text
frontend/index.html
```

in your browser.

Enter a public API URL and click:

```text
🔍 Scan API
```

The dashboard will send the URL to the SecureSense AI backend and display the security analysis.

---

## 🧪 Running Tests

SecureSense AI currently contains **15 automated tests**.

Run the complete test suite:

```bash
pytest
```

Expected result:

```text
15 passed
```

### Test Coverage

```text
Security Analyzer     → 6 tests
Anomaly Detection     → 6 tests
FastAPI API            → 3 tests
--------------------------------
Total                 → 15 tests
```

---

## 🔍 Public API Testing

The repository includes a collection of **100 public API endpoints** that can be used for testing SecureSense AI.

See:

```text
TEST_APIS.md
```

The collection contains APIs from multiple public services and can be used to demonstrate different API responses.

---

## 🔐 Security Checks

SecureSense AI currently performs the following checks:

```text
                 ┌───────────────────┐
                 │     API URL       │
                 └─────────┬─────────┘
                           ↓
              ┌────────────────────────┐
              │    HTTP Request        │
              └───────────┬────────────┘
                          ↓
          ┌───────────────────────────────┐
          │      Security Analysis        │
          ├───────────────────────────────┤
          │ Security Headers              │
          │ HTTPS                         │
          │ Server Disclosure             │
          │ Response Time                 │
          │ HTTP Status                   │
          └───────────────┬───────────────┘
                          ↓
             ┌────────────────────────┐
             │  Anomaly Detection     │
             └───────────┬────────────┘
                         ↓
             ┌────────────────────────┐
             │ Security Insights      │
             └───────────┬────────────┘
                         ↓
             ┌────────────────────────┐
             │   Web Dashboard        │
             └────────────────────────┘
```

---

## 📊 Current Project Status

| Component | Status |
|---|---|
| FastAPI Backend | ✅ Complete |
| API Scanner | ✅ Complete |
| Security Header Analysis | ✅ Complete |
| Security Score | ✅ Complete |
| Risk Classification | ✅ Complete |
| HTTPS Check | ✅ Complete |
| Server Disclosure Check | ✅ Complete |
| Anomaly Detection | ✅ Complete |
| Security Insight Layer | ✅ Complete |
| Dashboard | ✅ Complete |
| Public API Test Catalog | ✅ Complete |
| Automated Testing | ✅ Complete |
| README | ✅ Complete |

---

## 🚧 Future Improvements

Potential future enhancements include:

- Machine-learning based anomaly detection
- Authentication and authorization testing
- API rate-limit analysis
- JWT security analysis
- CORS security analysis
- SQL injection detection
- API fuzzing
- OpenAPI/Swagger specification analysis
- Historical scan results
- Security report generation
- Cloud deployment
- More advanced AI/LLM security recommendations

---

## ⚠️ Disclaimer

SecureSense AI is intended for **educational, research, and authorized security testing purposes**.

Only scan APIs and systems that you own or have explicit permission to test.

Do not use this tool to perform unauthorized security testing.

---

## 👥 Team

### SecureSense AI Team

- **Shashank H C**
- **Sharath**
- **Vijetha**
- **Akhilesh**

Built for **Hack With Bangalore 4.0** 🚀

---

## ⭐ Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

**SecureSense AI — Scan. Detect. Understand. Secure.**
