from fastapi import FastAPI

app = FastAPI()


@app.post("/concatenar")
def concatenar(palabra1: str, palabra2: str):
    palabrafinal = palabra1 + palabra2
    return {"mensaje": "Palabra concatenada", "palabra": palabrafinal}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
