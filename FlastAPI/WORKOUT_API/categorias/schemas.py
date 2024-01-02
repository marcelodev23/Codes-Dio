from typing import Annotated
from pydantic import Field, PositiveFloat
from WORKOUT_API.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome:Annotated[str,Field(discriminator='Nome do Categoria',example='scale',max_length=10)]