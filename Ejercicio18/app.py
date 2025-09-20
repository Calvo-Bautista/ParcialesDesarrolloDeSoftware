# Hacer una aplicación de ventanas que muestre un mensaje ingresado por el usuario en una ventana independiente.


import tkinter as tk

ventana = tk.Tk()
ventana.title("Mensaje aparte")

tk.Label(ventana, text="Mensaje:").pack()
mensaje = tk.Entry(ventana)
mensaje.pack()


def mostrar_mensaje():
    # Crear una nueva ventana independiente
    ventana_mensaje = tk.Toplevel(ventana)
    ventana_mensaje.title("Tu mensaje")

    # Obtener el texto del campo de entrada
    texto = mensaje.get()

    # Mostrar el mensaje en la nueva ventana
    tk.Label(ventana_mensaje, text=texto).pack()

    # Botón para cerrar la ventana del mensaje
    tk.Button(ventana_mensaje, text="Cerrar", command=ventana_mensaje.destroy).pack()


# Botón para mostrar el mensaje
tk.Button(ventana, text="Mostrar mensaje", command=mostrar_mensaje).pack()

ventana.mainloop()
