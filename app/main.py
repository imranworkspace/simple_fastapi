from fastapi import FastAPI
from app.router import router 

app = FastAPI(
    title="fastapi docker k8s",version="1.0",
    openapi_url="/fastapi/openapi.json",
    docs_url="/fastapi/docs",
    redoc_url="/fastapi/redoc"
)
app.include_router(router)