from fastapi import APIRouter

router = APIRouter()

@router.get("/health-check")
def healthCheck():
    return {"message": "API is working fine!!!"}