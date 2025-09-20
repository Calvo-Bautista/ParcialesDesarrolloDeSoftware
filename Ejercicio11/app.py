# Hacer una suma en una api a través de una biblioteca (get)

from fastapi import FastAPI
from mi_biblioteca_matematica import CalculadoraMatematica

app = FastAPI()

# Instancia global de nuestra calculadora personalizada
calculadora = CalculadoraMatematica()

@app.get("/suma")
def sumar_numeros(a: float, b: float):
    resultado = calculadora.sumar(a,b)
    return {"mensaje":"Resultado calculado", "resultado":resultado}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
