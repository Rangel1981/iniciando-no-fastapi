from dataclasses import Field
from typing import Annotated

from workout.contrib.schemas import BaseSchemas


class CentroTreinamento(BaseSchemas):
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
