from fastapi import FastAPI

app = FastAPI()

@app.get("/auth/")
async def get_user_auth():
    return {"message": "User is authenticated"}

