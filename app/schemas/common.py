from pydantic import BaseModel
from typing import Optional, Dict, Any

class MessageResponse(BaseModel):
    message: str

class SuccessResponse(BaseModel):
    success: bool
    message: Optional[str] = None

class GenericApiResponse(SuccessResponse):
    data: Dict[str, Any]     
