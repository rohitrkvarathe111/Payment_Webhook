# Payment Webhook

This is a simple **FastAPI** project to handle payment webhooks. It supports processing different webhook events like `payment_authorized`, `payment_captured`, and `payment_failed`.

---

## Project Structure

#├─ main.py # FastAPI application
#├─ database.py # Database connection setup
#├─ models.py # SQLAlchemy models
#├─ schemas.py # Pydantic schemas
#├─ utils.py # Utility functions
#├─ zz_test.py # HMAC signature testing script
#├─ payments.db # SQLite database
#├─ requirements.txt # Python dependencies
#├─ mock_payloads/ # Example webhook JSON payloads
#│ ├─ payment_authorized.json
#│ ├─ payment_captured.json
#│ └─ payment_failed.json
#└─ pycache/ # Python cache files
