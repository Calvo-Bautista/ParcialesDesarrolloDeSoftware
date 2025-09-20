# Api que retorne una lista de nombres(get)

from fastapi import FastAPI

app = FastAPI()

lista=["juan", "pedro", "saul", "roman"]

@app.get("/listanombres")
def retornarlista():
    return {"mensaje":"correcto","lista devuelta":lista}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)