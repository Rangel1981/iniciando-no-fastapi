from pydantic import Field
from workout.contrib.schemas import BaseSchemas, OutMixin
from typing import Annotated


class Atleta(BaseSchemas):
    nome: Annotated[str, Field(description="Nome do atleta", examples=["João"])]
    cpf: Annotated[str, Field(description="CPF do atleta", examples=["12345678900"])]
    idade: Annotated[int, Field(description="Idade do atleta", examples=[25])]
    peso: Annotated[float, Field(description="Peso do atleta", examples=[75.5])]
    altura: Annotated[float, Field(description="Altura do atleta", examples=[1.75])]
    sexo: Annotated[str, Field(description="Sexo do atleta", examples=["M"])]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    pass
