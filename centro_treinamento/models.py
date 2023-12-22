from sqlalchemy import Integer,String
from sqlalchemy.orm import Mapped,mapper_column,relationship
from WORKOUT_API.contrib.models import BaseModel


class CentroTreinamentoModels(BaseModel):
    __tablename__='centros_treinamento'
    pk_id:Mapped[int] = mapper_column(Integer,primary_key=True)
    nome:Mapped[str] = mapper_column(String,nullble=False)
    endereco:Mapped[str]=mapper_column(String,nullble=False)
    proprietario:Mapped(str)=mapper_column(String,nullbe=False)
    atleta:Mapped['AletaModel']= relationship(back_populates='centros_treinamento')