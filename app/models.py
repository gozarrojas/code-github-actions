from pydantic import BaseModel

# Modelo de datos para el CRUD
class Item(BaseModel):
    name: str
    description: str