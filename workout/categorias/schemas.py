from dataclasses import Field
from typing import Annotated

from workout.contrib.schemas import BaseSchemas


class Categoria(BaseSchemas):
    nome: Annotated[
        str, Field(description="Nome da categoria", examples="Sclae", max_length=10)
    ]
