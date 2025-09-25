from fastapi import FastAPI
from src.routers import home, health_check, mobile_model
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import os

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

# --- Cron job to ping server every 1 minute ---
def ping_self():
    url = os.getenv("PING_URL", "https://your-app.onrender.com/health")
    try:
        requests.get(url, timeout=10)
        print(f"Pinged {url} successfully ✅")
    except Exception as e:
        print(f"Ping failed: {e}")

scheduler = BackgroundScheduler()
scheduler.add_job(ping_self, "interval", minutes=1)
scheduler.start()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",       
        host="0.0.0.0",   
        port=8000,       
        reload=True        
    )