#Web api concatenar dos palabras (get)

from fastapi import FastAPI

app = FastAPI()

@app.get("/concatenar")
def concatenar(p1:str, p2:str):
    pfinal = p1 + p2
    return {"mensaje":"Palabra concatenada", "palabra":pfinal}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)