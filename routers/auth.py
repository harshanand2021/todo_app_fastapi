from fastapi import APIRouter

router = APIRouter()

@router.get("/auth/")
async def get_user_auth():
    return {"user": "User is authenticated"}

