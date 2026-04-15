from pydantic import BaseModel, Field

class calcer(BaseModel):
    number: float = Field(..., example=5, description="任意の数")