from datetime import datetime
from WORKOUT_API.contrib.models import BaseModel
from sqlalchemy.orm import Mapped,mapped_column,relationships 
from sqlalchemy import String,Integer,Float,DateTime,ForeignKey
from dio.FlastAPI.WORKOUT_API.categorias.models import CategoriaModel
from dio.FlastAPI.WORKOUT_API.centro_treinamento.models import CentroTreinamentoModels

class AletaModel(BaseModel):
    __tablename__ = 'atletas'
    pk_id:Mapped[int] = mapped_column(Integer,primary_key=True)
    nome:Mapped[str]  = mapped_column(String(50),nullble=False)
    cpf:Mapped[str]   = mapped_column(String(11),unique=True,nullble=True)
    idade:Mapped[int] = mapped_column(Integer,nullble=True)
    peso:Mapped[float]= mapped_column(Float,nullble=False)
    altura:Mapped[float]=mapped_column(Float,nullble=False)
    sexo:Mapped[str] = mapped_column(String(1),nullble=False)
    create_at:Mapped[datetime] = mapped_column(DateTime,nullble=True)
    
    categoria:Mapped['CategoriaModel']= relationships(back_populates='atletas')
    categoria_id:Mapped[int] = mapped_column(ForeignKey('categoria.pk_id'))

    centroTreinamento:Mapped['CentroTreinamentoModels'] = relationships(back_populates='atletas')
    centroTreinamento_id:Mapped[int]= mapped_column(ForeignKey('centros_treinamento.pk_id'))