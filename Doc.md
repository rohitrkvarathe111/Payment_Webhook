# API Documentation - Payment Webhook

This document describes the endpoints available in the **Payment Webhook** FastAPI application.

---

## Base URL

http://127.0.0.1:8000


---

## Endpoints

### 1. POST `/webhook/payments`

**Description:**  
Receives webhook events for payments and verifies HMAC signature.

**Headers:**
- `Content-Type: application/json`
- `X-Razorpay-Signature: <HMAC_SIGNATURE>`

**Body:**  
JSON payload depending on the webhook type. Example: `payment_authorized.json`:

```json
{
  "id": "pay_12345",
  "status": "authorized",
  "amount": 1000,
  "currency": "INR"
}

**Response:** 
200 OK – Webhook received successfully.
{
    "status": "success"
}

400 Bad Request – Invalid signature or payload.
{
  "error": "Invalid signature"
}

---

**Example cURL request:** 
curl --location 'http://127.0.0.1:8000/webhook/payments' \
--header 'Content-Type: application/json' \
--header 'X-Razorpay-Signature: 936617082e4ce4ba95e14b030924443aebb602c1d461d651521a50434ab5453a' \
--data-binary '@/C:/Users/Desktop/webhook/mock_payloads/payment_authorized.json'

### 2. GET /payments/{id}/events
Description:
Fetches all webhook events for a specific payment by ID.

Path Parameters:

id (string) – Payment ID to retrieve events for.

Response:

200 OK
[
  {
    "event": "payment_authorized",
    "payment_id": "pay_12345",
    "status": "authorized",
    "timestamp": "2025-08-15T15:00:00Z"
  },
  {
    "event": "payment_captured",
    "payment_id": "pay_12345",
    "status": "captured",
    "timestamp": "2025-08-15T15:05:00Z"
  }
]

404 Not Found – If payment ID does not exist.
{
  "error": "Payment not found"
}

curl --location 'http://127.0.0.1:8000/payments/pay_12345/events'



### HMAC Signature Testing

You can generate a signature for testing using zz_test.py:
python zz_test.py mock_payloads/payment_authorized.json

It will return a HMAC signature you can use in the X-Razorpay-Signature header.

Notes

All webhook requests must include a valid HMAC signature.

The app uses SQLite (payments.db) to store received events.

Example payloads are available in mock_payloads/.
