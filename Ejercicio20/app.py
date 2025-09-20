#hacer una app que multiplique dos numeros ingresados por el usuario


from fastapi import FastAPI

app = FastAPI()

@app.get("/multiplicar")
def multiplicar(num1: int, num2: int):
    resultado = num1*num2
    return {"mensaje":"correcto", "numero 1": num1, "numero 2": num2, "resultado": resultado}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)