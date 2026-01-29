from pydantic import BaseModel
from fastapi import status
from typing import Optional, Dict, Any

class MessageResponse(BaseModel):
    message: str

class SuccessResponse(BaseModel):
    success: bool
    status_code: int | None = status.HTTP_200_OK    
    message: str| None = None    

class GenericApiResponse(SuccessResponse):
    data: Dict[str, Any] | None = None    

