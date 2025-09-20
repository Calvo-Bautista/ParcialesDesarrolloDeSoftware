#API web que traiga una ciudad y lo ingrese en una lista(get post)

from fastapi import FastAPI

app = FastAPI()

listaciudades=[]

@app.post("/ingresarciudad")
def ingresarciudad(ciudad: str):
    listaciudades.append(ciudad)
    return {"Mensaje finalizado":"Correcto","ciudad añadida":ciudad}

@app.get("/devolverciudad")
def retornarciudad(ciudad: str):
    for lista in listaciudades:
        if lista == ciudad:
            ciudadretornada = lista
    return {"Mensaje finalizado":"Correcto","ciudad existente en lista":ciudadretornada}

@app.get("/devolverlistaciudades")
def devolverlistaciudades(ciudad: str):
    return {"Mensaje finalizado":"Correcto","lista de ciudades":listaciudades}

if __name__ == "__main__": 
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)