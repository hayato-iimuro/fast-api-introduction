from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession




import api.schemas.calc as calc_schema

router = APIRouter()


@router.post("/calc_pow")
async def squared(request_body: calc_schema.calcer):
    result = request_body.number **2
    return {"input": request_body.number, "ans":result}

