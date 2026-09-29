from pydantic import BaseModel, Field
from typing import Literal


class MarketingCopy(BaseModel):
    """Strict output schema for generated marketing copy."""
    product_name: str
    platform: Literal["LinkedIn", "Instagram", "Email"]
    tone: str
    generated_copy: str = Field(..., description="Final platform-ready marketing copy")
    character_count: int
    word_count: int
    temperature_used: float
