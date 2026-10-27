from fastapi import FastAPI
from app.router import router 
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI(
    title="fastapi docker k8s",version="1.0",
    docs_url=None
)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui():
    return get_swagger_ui_html(
        openapi_url="/fastapi/openapi.json",
        title="FastAPI Swagger UI"
    )

app.include_router(router)