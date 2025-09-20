# Web api que liste países(get)

from fastapi import FastAPI

app = FastAPI()

lista = ["francia", "argentina", "croacia", "marruecos"]

@app.get("/listarpaises")
def listarpaises():
    return {"mensaje entendido":"OK", "lista de paises":lista}