from fastapi import APIRouter,HTTPException

router = APIRouter(prefix='/health',tags=['health'])

@router.get('/')
async def health_chk():
    return {'status':'welome'}

@router.get('/{name}')
async def get_name(name:str):
    return {'status':f'hi {name}'}
