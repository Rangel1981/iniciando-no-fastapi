from fastapi import APIRouter, status
from fastapi.params import Body

from workout.atleta.schemas import AtletaIn
from workout.contrib.dependencies import DatabaseDependency

router = APIRouter()


@router.post(
    "/",
    summary="Cria um novo atleta",
    description="Cria um novo atleta com os dados fornecidos.",
    status_code=status.HTTP_201_CREATED,
)
async def post(db_session: DatabaseDependency, atleta_in: AtletaIn = Body(...)):
    pass
