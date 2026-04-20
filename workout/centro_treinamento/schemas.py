from typing import Annotated

from pydantic import UUID4, Field

from workout.contrib.schemas import BaseSchemas


class CentroTreinamentoIn(BaseSchemas):
    nome: Annotated[
        str,
        Field(
            description="Nome do centro de treinamento",
            example="Ct King",
            max_length=20,
        ),
    ]

    endereco: Annotated[
        str,
        Field(
            description="Endereço do centro de treinamento",
            example="Av. Paulista, 1000",
            max_length=60,
        ),
    ]

    proprietario: Annotated[
        str,
        Field(
            description="Nome do proprietário do centro de treinamento",
            example="João da Silva",
            max_length=30,
        ),
    ]


class CentroTreinamentoAtleta(BaseSchemas):
    nome: Annotated[
        str, Field(description="Nome do atleta", example="João da Silva", max_length=20)
    ]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador do centro de treinamento")]
