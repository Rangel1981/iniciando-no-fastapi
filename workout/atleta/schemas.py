from typing import Annotated

from pydantic import BaseModel, Field, PositiveFloat

from workout.contrib.schemas import BaseSchemas

class Atleta(BaseSchemas):
    nome: Annotated[str, Field(description="Nome do Atleta", examples="Arthur", max_length=50)]
    cpf: Annotated[int, Field(description="CPF do Atleta", examples="00000000000", max_length=11)]
    idade: Annotated[int, Field(description="Idade do Atleta", examples="28")]
    peso: Annotated[PositiveFloat, Field(description="Peso do Atleta", examples=85.5)]
    altura: Annotated[float, Field(description="Altura do Atleta", examples="180.5")]
    sexo: Annotated[int, Field(description="Sexo do Atleta", examples="M", max_length=1)]
