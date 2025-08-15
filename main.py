from fastapi import FastAPI, Request, HTTPException, Depends
from sqlalchemy.orm import Session
import database, models, schemas, utils
import json

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/webhook/payments")
async def webhook_listener(request: Request, db: Session = Depends(get_db)):
    signature = request.headers.get("X-Razorpay-Signature")
    if not signature:
        raise HTTPException(status_code=403, detail="Missing signature")

    body = await request.body()

    if not utils.verify_signature(body, signature):
        raise HTTPException(status_code=403, detail="Invalid signature")

    try:
        payload = json.loads(body)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    event_type = payload.get("event")
    event_id = payload.get("id")
    try:
        payment_id = payload["payload"]["payment"]["entity"]["id"]
    except (KeyError, TypeError) as e:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid webhook format: {e}"
        )

    if db.query(models.PaymentEvent).filter_by(event_id=event_id).first():
        return {"status": "duplicate_event"}

    db_event = models.PaymentEvent(
        event_id=event_id,
        payment_id=payment_id,
        event_type=event_type,
        payload=payload
    )
    db.add(db_event)
    db.commit()

    return {"status": "success"}

@app.get("/payments/{payment_id}/events", response_model=list[schemas.PaymentEventOut])
def get_payment_events(payment_id: str, db: Session = Depends(get_db)):
    events = (
        db.query(models.PaymentEvent)
        .filter_by(payment_id=payment_id)
        .order_by(models.PaymentEvent.received_at)
        .all()
    )
    return events
