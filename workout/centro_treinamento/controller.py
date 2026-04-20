from uuid import uuid4

from fastapi import APIRouter, status
from fastapi.params import Body

from pydantic import UUID4
from sqlalchemy import select
from workout.centro_treinamento.models import (
    CentroTreinamentoModel,
)
from workout.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from workout.contrib.dependencies import DatabaseDependency

router = APIRouter()


@router.post(
    "/",
    summary="Cria uma novo centro de treinamento",
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
)
async def post(
    db_session: DatabaseDependency,
    centro_treinamento_in: CentroTreinamentoIn = Body(...),
) -> CentroTreinamentoOut:

    centro_treinamento_out = CentroTreinamentoOut(
        id=uuid4(), **centro_treinamento_in.model_dump()
    )
    centro_treinamento_model = CentroTreinamentoModel(
        **centro_treinamento_in.model_dump()
    )

    db_session.add(centro_treinamento_model)
    await db_session.commit()

    return centro_treinamento_out


@router.get(
    "/",
    summary="Consultar todos os centros de treinamento",
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut],
)
async def query(db_session: DatabaseDependency) -> list[CentroTreinamentoOut]:

    centros_treinamento: list[CentroTreinamentoModel] = (
        await db_session.execute(select(CentroTreinamentoModel)).scalars().all()
    )
    return centros_treinamento


@router.get(
    "/[id]",
    summary="Consultar um centro de treinamento pelo ID",
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut,
)
async def query(id: UUID4, db_session: DatabaseDependency) -> CentroTreinamentoOut:
    centro_treinamento: CentroTreinamentoOut = (
        (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id)))
        .scalars()
        .first()
    )
    if not centro_treinamento:
        HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Centro de treinamento não encontrado",
        )
    return centro_treinamento
