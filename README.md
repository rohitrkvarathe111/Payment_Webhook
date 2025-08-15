
# Payment Webhook

This repository contains a **FastAPI** project that handles payment webhooks. It supports multiple webhook events like `payment_authorized`, `payment_captured`, and `payment_failed` with HMAC signature verification.

---

## Repository Contents



---

## Prerequisites

- Python 3.11+
- Git

---

## Setup Locally

1. **Clone the repository**

```bash
git clone https://github.com/rohitrkvarathe111/Payment_Webhook.git
cd Payment_Webhook


# Windows PowerShell
python -m venv bdtenv
.\bdtenv\Scripts\Activate.ps1

# Windows CMD
bdtenv\Scripts\activate.bat

pip install -r requirements.txt
or
pip install fastapi uvicorn
# THEN RUN THIS PROJECT
uvicorn main:app --reload

# to check go to this url
http://127.0.0.1:8000/docs

