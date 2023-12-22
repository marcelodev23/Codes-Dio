from WORKOUT_API.contrib.models import BaseModel
from sqlalchemy.orm import Mapped,mapped_column,relationships
from sqlalchemy import String,Integer,Float,DateTime

class CategoriaModel(BaseModel):
    __tablename__ = 'categoria'
    pk_id:Mapped[int] = mapped_column(Integer,primary_key=True)
    nome:Mapped[str]  = mapped_column(String(50),nullble=False)
    atleta:Mapped['AletaModel']= relationships(back_populates='categoria')