import tkinter as tk
import operaciones_matematicas as ops

ventana = tk.Tk()
ventana.title("Calculadora")

# Entradas
tk.Label(ventana, text="Número 1:").pack()
num1 = tk.Entry(ventana)
num1.pack()

tk.Label(ventana, text="Número 2:").pack()
num2 = tk.Entry(ventana)
num2.pack()

# Resultado
resultado = tk.Label(ventana, text="Resultado: 0")
resultado.pack()


# Funciones
def sumar():
    res = ops.sumar(float(num1.get()), float(num2.get()))
    resultado.config(text=f"Resultado: {res}")


def restar():
    res = ops.restar(float(num1.get()), float(num2.get()))
    resultado.config(text=f"Resultado: {res}")


def multiplicar():
    res = ops.multiplicar(float(num1.get()), float(num2.get()))
    resultado.config(text=f"Resultado: {res}")


# Botones
tk.Button(ventana, text="Sumar", command=sumar).pack()
tk.Button(ventana, text="Restar", command=restar).pack()
tk.Button(ventana, text="Multiplicar", command=multiplicar).pack()

ventana.mainloop()
