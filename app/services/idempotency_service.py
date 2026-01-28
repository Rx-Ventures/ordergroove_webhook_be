from app.schemas.webhook import WebhookEventCreate, WebhookEventResponse
from app.crud import (
    webhook_events as webhook_events_crud
)
from sqlalchemy.orm import Session
from typing import Optional
import logging as logger
from fastapi import HTTPException,status


class IdempotencyService:
    async def create_webhook_event(
            self,
            db: Session,
            webhook_event_log: WebhookEventCreate
        ) -> WebhookEventResponse:
        try:

            print(f"webhook_event_log: {webhook_event_log}")

            existing_webhook = await webhook_events_crud.get_webhook_event_by_event_id(
                db,
                webhook_event_log.event_id
            )
            if existing_webhook:
                logger.info(f"Webhook event log already exists: {webhook_event_log.event_id}")
                return False
            webhook_event = await webhook_events_crud.create_webhook_event(db, webhook_event_log)
            if webhook_event:
                return webhook_event
            else:
                logger.info(f"Error creating webhook_event log")
        except Exception as e:
            logger.error(f"Error getting subscription webhook_event: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An unexpected error occurred"
            )
                
idempotency_service = IdempotencyService()