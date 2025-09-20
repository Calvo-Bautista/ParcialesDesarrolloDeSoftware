# Calcular la longitud de un string con una api con servicio

from fastapi import FastAPI
from services.longitudService import LongitudService

app = FastAPI()

servicio = LongitudService()

@app.get("/devolverlongitud")
def devolverlongitud(cadena:str):
    caracteres = servicio.longitud(cadena)
    return {"mensaje":cadena, "longitud":caracteres}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)