from fastapi import Request, HTTPException
import jwt


def get_pyload(request: Request):
    try:
        token = request.headers.get("authorization", None)
        if token is None:
            raise jwt.PyJWTError()
        header_token, token = token.split()
        payload = jwt.decode(token, options={"verify_signature": False})
        if not payload.get("is_paid_for", None):
            raise HTTPException(status_code=403, detail="не оплачено")
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=403, detail="нет доступа")


# stmt = select(User).where(User.id == 1)
# r = await session.scalars(stmt)
# stmt = insert(User).values(**schema.dict())
# await session.execute(stmt)
# await session.commit()
