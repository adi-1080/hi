from fastapi.responses import JSONResponse
from src.utilities.read_image import readImage
from src.utilities.get_prediction import get_prediction
from src.constants.mobile_model import mobile_model

async def mobile_model_controller(file):
    image_bytes = await file.read()
    image = readImage(image_bytes)
    pred_class, confidence = get_prediction(mobile_model, image)
    return JSONResponse(content={"class": pred_class, "confidence": confidence})
