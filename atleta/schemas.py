from typing import Annotated
from pydantic import Field, PositiveFloat
from WORKOUT_API.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome:Annotated[str,Field(discriminator='Nome do atleta',example='joao',max_length=50)]
    cpf:Annotated[str,Field(description='CPF do atleta',example='12345678900',max_length=11)]
    idade:Annotated[int,Field(description='Idade do atleta',example=25)]
    peso:Annotated[PositiveFloat,Field(description='Peso do atleta',example = 75.5)]
    altura:Annotated[PositiveFloat,Field(description='Altura do atleta',example=1.75)]
    sexa:Annotated[str,Field(description='Sexo do atleta',example='M',max_length=1)]