from fastapi import APIRouter

router = APIRouter(
          prefix="/address",
          tags=["address"]
        )


@router.get("/")
async def read_users():
    return 'address endpoint'

@router.post("/")
async def create_address():
    return 'cria address'

