from WORKOUT_API.contrib.models import BaseModel
from sqlalchemy.orm import Mapped,mapped_column,relationships
from sqlalchemy import String,Integer,Float,DateTime
from dio.FlastAPI.WORKOUT_API.atleta.models import AletaModel

class CategoriaModel(BaseModel):
    __tablename__ = 'categoria'
    pk_id:Mapped[int] = mapped_column(Integer,primary_key=True)
    nome:Mapped[str]  = mapped_column(String(50),unique=True,nullble=False)
    atleta:Mapped['AletaModel']= relationships(back_populates='categoria')