from fastapi import APIRouter, UploadFile, File
from src.controllers.mobile_model import mobile_model_controller

router = APIRouter()

@router.post("/mobile-model")
async def mobile_model(file: UploadFile = File(...)):
    return await mobile_model_controller(file)