
from pydantic import BaseModel, ConfigDict

class SolidgateWebhookBase(BaseModel):
    event: str | None = None
    order_id: str | None = None
    transaction_id: str | None = None
    amount: int | None = None
    currency: str | None = None
    status: str | None = None
    payment_token: str | None = None
    
    model_config = ConfigDict(extra="allow")
    
    def to_json(self):
        return self.model_dump_json()

class SolidgateWebhookPayload(SolidgateWebhookBase):
    event: str
    order_id: str
    transaction_id: str
    amount: int
    currency: str
    status: str
