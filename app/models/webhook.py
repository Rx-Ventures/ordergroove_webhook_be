"""
Webhook event model for storing PSP webhook data.
"""

import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


def generate_webhook_id() -> str:
    return f"wh_evt_{uuid.uuid4().hex}"


class WebhookEvent(Base):
    __tablename__ = "webhook_events"
    
    id: Mapped[str] = mapped_column(
        String(50),
        primary_key=True,
        default=generate_webhook_id,
    )
    event_id: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
    )
    psp: Mapped[str] = mapped_column(
        String(50),
        index=True,
    )
    event_type: Mapped[str] = mapped_column(
        String(100),
    )
    medusa_order_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True,
    )
    payload: Mapped[dict] = mapped_column(
        JSONB,
    )
    processed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )
    error_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    processed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    
    def __repr__(self) -> str:
        return f"<WebhookEvent {self.id} {self.psp}:{self.event_type}>"