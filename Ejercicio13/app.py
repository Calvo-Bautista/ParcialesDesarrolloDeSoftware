# Api web que retorne/ingrese un nombre de/a una lista (get post)

from fastapi import FastAPI

app = FastAPI()

listanombres=[]

@app.post("/ingresarnombre")
def ingresarnombre(nombre: str):
    listanombres.append(nombre)
    return {"mensaje":"Nombre añadido", "Nombre añadido":nombre}

@app.get("/retornarnombre")
def retornarnombre(nombre: str):
    for lista in listanombres:
        if lista == nombre:
            retorno = lista
    return {"mensaje":"Busqueda completa", "Nombre retornado":retorno}

@app.get("/listanombres")
def retornarlista():
    return {"mensaje":"Busqueda completa", "Lista":listanombres}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)