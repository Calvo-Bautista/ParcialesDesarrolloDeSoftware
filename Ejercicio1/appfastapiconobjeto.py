from fastapi import FastAPI
from typing import Dict, Any
from pydantic import BaseModel

app = FastAPI()

# Lista para almacenar objetos
lista_objetos = []

class Objeto(BaseModel):
    nombre: str
    apellido: str

@app.post("/metodopost")
def metodopost(objeto: Objeto):
    lista_objetos.append(objeto)
    return {"mensaje": "Objeto agregado", "objeto": objeto}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)