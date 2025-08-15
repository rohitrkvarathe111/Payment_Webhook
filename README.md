# Payment Webhook

This repository contains a FastAPI project that handles payment webhooks. It supports multiple webhook events like payment_authorized, payment_captured, and payment_failed with HMAC signature verification.

## Prerequisites
- Python 3.11+
- Git

## Setup Locally

Clone the repository

```bash
git clone https://github.com/rohitrkvarathe111/Payment_Webhook.git
```
```bash
cd Payment_Webhook
```

create VENV
```bash
python -m venv venv
.\venv\Scripts\Activate
```

To install the packages listed in a requirements.txt
```bash
pip install -r requirements.txt

pip install fastapi uvicorn
```
Then run this project
```bash
uvicorn main:app --reload
```

to check go to this url
```bash
http://127.0.0.1:8000/docs
```
