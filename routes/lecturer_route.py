router = APIRouter(
    prefix="/api/lecturer",
    tags=["attendance"],
    responses={404: {"description": "The requested url was not found"}},
)