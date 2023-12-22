from WORKOUT_API.contrib.schemas import BaseSchema
from typing import Annotated
from pydantic import Field

class CentroTreinamento(BaseSchema):
    nome:Annotated[str,Field(description='Nome do Centro de Treinamento',example='CT Top',max_length=20)]
    endereço:Annotated[str,Field(description='Endereço Centro de Treinamento',example='Rua das putas',max_length=60)]
    proprietario:Annotated[str,Field(description='Proprietario do Centro de Treinamento',example='joao',max_length=30)]
