from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class tipodocuSchema(BaseModel):
    id: Optional[int] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None

    class Config:
        orm_mode = True

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
