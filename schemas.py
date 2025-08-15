from pydantic import BaseModel
from datetime import datetime
from typing import List

class PaymentEventOut(BaseModel):
    event_type: str
    received_at: datetime

    class Config:
        from_attributes = True
