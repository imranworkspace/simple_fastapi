from fastapi import APIRouter,HTTPException

router = APIRouter(prefix='/health',tags=['health'])

@router.get('/')
async def health_chk():
    return {'status':'welome'}
