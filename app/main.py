
from fastapi import FastAPI
from app.router import router

app = FastAPI(
    title="fastapi docker k8s",
    version="1.0",
    root_path="/fastapi",
)

app.include_router(router)
