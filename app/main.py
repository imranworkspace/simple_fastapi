
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from app.router import router

app = FastAPI(
    title="fastapi docker k8s",
    version="1.0",
    docs_url=None,
    root_path="/fastapi",
)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui():
    return get_swagger_ui_html(
        openapi_url="/fastapi/openapi.json",
        title="FastAPI Swagger UI",
    )

app.include_router(router)
