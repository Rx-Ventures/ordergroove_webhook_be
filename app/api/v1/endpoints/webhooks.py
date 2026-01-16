import logging
from datetime import datetime

from fastapi import APIRouter, Header, HTTPException, Request, status
from sqlalchemy import select

from app.core.database import AsyncSessionLocal
from app.models.webhook import WebhookEvent
from app.schemas.webhook import WebhookAck
from app.schemas.common import GenericApiResponse
from app.services.solidgate_service import solidgate_service

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post('/webhook_test')
async def webhook_test(request: Request):

    body = await request.json()


    return GenericApiResponse(
        success=True,
        message="Success", 
        data=body
    )
