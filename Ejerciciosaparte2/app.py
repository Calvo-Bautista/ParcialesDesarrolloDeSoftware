# Consumir un archivo, generar un endpoint y poder filtrarlo por algún filtro que vos elijas

from fastapi import FastAPI

app = FastAPI()


@app.get("/archivo")
def obtener_contenido():
    with open("Ejerciciosaparte2/hola.txt", "r") as archivo:
        lineas = archivo.readlines()
    return {"contenido": [linea.strip() for linea in lineas]}


@app.get("/archivo/filtrar")
def filtrar_por_longitud(min_chars: int):
    with open("Ejerciciosaparte2/hola.txt", "r") as archivo:
        lineas = archivo.readlines()

    resultado = []
    for linea in lineas:
        linea_limpia = linea.strip()
        if len(linea_limpia) >= min_chars:
            resultado.append(linea_limpia)

    return {"filtrado": resultado}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
