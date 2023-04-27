from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from fastapi import APIRouter, Depends
from services import get_pyload

router = APIRouter()


@router.get("/test")
async def test(payload: dict = Depends(get_pyload), session: AsyncSession = Depends(get_async_session)):
    return {"status": payload}


# user_id = payload.get("user_id")
# company_id = payload.get("company")
# is_owner = payload.get("is_owner")
