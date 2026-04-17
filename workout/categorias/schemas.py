from pydantic import Field, UUID4  # Field e UUID4 vêm do pydantic
from typing import Annotated
from workout.contrib.schemas import BaseSchemas


class Categoria(BaseSchemas):
    nome: Annotated[
        str, Field(description="Nome da categoria", examples=["Sclae"], max_length=10)
    ]


class CategoriaIn(Categoria):
    pass


class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description="Identificador da categoria")]
