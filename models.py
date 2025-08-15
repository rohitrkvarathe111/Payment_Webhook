from sqlalchemy import Column, String, JSON, DateTime
from datetime import datetime
from database import Base


class PaymentEvent(Base):
    __tablename__ = "payment_events"

    event_id = Column(String, primary_key=True, index=True)
    payment_id = Column(String, index=True)
    event_type = Column(String)
    payload = Column(JSON)
    received_at = Column(DateTime, default=datetime.utcnow)
