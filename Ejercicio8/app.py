from fastapi import FastAPI
from services.calculadora import CalculadoraService

app = FastAPI()

calcu = CalculadoraService()

@app.get("/sumar")
def sumar(a:float, b:float):
    resultado = calcu.suma(a,b)
    return {
        "operacion":"suma",
        "numero1": a,
        "numero2": b,
        "resultado": resultado
    }

@app.get("/multiplicar")
def multiplicar(a:float, b:float):
    resultado = calcu.multiplicacion(a,b)
    return {
        "operacion":"multiplicacion",
        "numero1": a,
        "numero2": b,
        "resultado": resultado
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)