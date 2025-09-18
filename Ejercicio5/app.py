from fastapi import FastAPI
import operaciones_matematicas as ops

app = FastAPI()


@app.post("/sumar")
def sumar(a: float, b: float):
    resultado = ops.sumar(a, b)
    return {"operacion": "suma", "a": a, "b": b, "resultado": resultado}


@app.post("/restar")
def restar(a: float, b: float):
    resultado = ops.restar(a, b)
    return {"operacion": "resta", "a": a, "b": b, "resultado": resultado}


@app.post("/multiplicar")
def multiplicar(a: float, b: float):
    resultado = ops.multiplicar(a, b)
    return {"operacion": "multiplicacion", "a": a, "b": b, "resultado": resultado}


@app.post("/dividir")
def dividir(a: float, b: float):
    resultado = ops.dividir(a, b)
    return {"operacion": "division", "a": a, "b": b, "resultado": resultado}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
