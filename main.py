from fastapi import FastAPI
from src.routers import home, health_check, mobile_model
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    # allow_credentials=True,
    allow_methods=["*"],     
    allow_headers=["*"], 
)

app.include_router(home.router)
app.include_router(health_check.router)
app.include_router(mobile_model.router)
