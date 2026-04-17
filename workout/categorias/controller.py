from uuid import uuid4

from fastapi import APIRouter, status
from fastapi.params import Body

# Provavelmente o correto é importar do módulo de categorias
from workout.categorias.models import CategoriaModel
from workout.categorias.schemas import CategoriaIn, CategoriaOut
from workout.contrib.dependencies import DatabaseDependency

router = APIRouter()


@router.post(
    "/",
    summary="Cria uma nova categoria",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def post(
    db_session: DatabaseDependency, categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:

    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_in.model_dump())
    breakpoint()
    pass
