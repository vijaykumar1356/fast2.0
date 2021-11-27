from fastapi import FastAPI

from backend.api import api_router

app = FastAPI(debug=True)

app.include_router(api_router, prefix='/api/v1')
