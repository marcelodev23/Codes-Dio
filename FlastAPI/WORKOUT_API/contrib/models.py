from sqlalchemy.orm import DeclarativeBase,Mapped,mapper_column
from sqlalchemy import UUID
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID as pg_UUID

class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapper_column(pg_UUID(as_uuid=True),defaul=uuid4,nullable=False)