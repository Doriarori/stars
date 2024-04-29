from pydantic import BaseModel
from typing import Optional

class Star(BaseModel):
    id: Optional[int]
    name: str
    temperature: int
    size: float
    distance: float
