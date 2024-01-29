from fastapi import APIRouter

router = APIRouter(
    prefix="/api/class",
    tags=["class"],
    responses={404: {"description": "The requested url was not found"}},
)


@router.put("")
def create_class():
    pass


@router.get("")
def get_class():
    pass
