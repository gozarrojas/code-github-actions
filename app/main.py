from fastapi import FastAPI, HTTPException
from typing import List
from models import Item

# Creamos la app
app = FastAPI()

# Almacenaremos los items en una lista (simulación de base de datos)
fake_db = []

# Index
@app.get("/")
def index():
    return {
        "message": "FastAPI",
        "endpoints": {
            "GET /items/": "Listar todos los items",
            "POST /items/": "Crear un nuevo item",
            "GET /items/{id}": "Obtener item por ID",
            "PUT /items/{id}": "Actualizar item",
            "DELETE /items/{id}": "Eliminar item"
        }
    }

# Crear un nuevo item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    fake_db.append(item)
    return item

# Obtener todos los items
@app.get("/items/", response_model=List[Item])
def get_items():
    return fake_db

# Obtener un item por ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id < 0 or item_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]

# Actualizar un item
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id] = item
    return item

# Eliminar un item
@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = fake_db.pop(item_id)
    return deleted_item