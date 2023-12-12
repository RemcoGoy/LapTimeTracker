from fastapi import FastAPI

from .routers import sessions

app = FastAPI()

app.include_router(sessions.router)


@app.get("/")
async def main():
    return {"message": "Hello World"}
