from fastapi import FastAPI
from typing import Dict, Any

app = FastAPI()

# Lista para almacenar objetos
lista_objetos = []

@app.post("/metodopost")
def metodopost(objeto: Dict[Any, Any]): #que diga dict any any es lo mismo que {} y que puede recibir cualquier tipo de datos, como strings o int
    lista_objetos.append(objeto)
    return {"mensaje": "Objeto agregado", "objeto": objeto}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)