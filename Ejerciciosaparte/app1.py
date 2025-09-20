# Haga una vista con una imagen de 150px × 150px

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Crear directorio para archivos estáticos si no existe
if not os.path.exists("static"):
    os.makedirs("static")

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def mostrar_vista_con_imagen():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Vista con Imagen 150x150px</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
                background-color: #f0f0f0;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .imagen-150 {
                width: 150px;
                height: 150px;
                border: 2px solid #333;
                border-radius: 8px;
                object-fit: cover;
                margin: 20px 0;
            }
            h1 {
                color: #333;
                margin-bottom: 20px;
            }
            .info {
                background-color: #e8f4f8;
                padding: 15px;
                border-radius: 5px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Vista con Imagen 150px × 150px</h1>
            
            <!-- Imagen desde URL externa -->
            <img src="https://via.placeholder.com/150x150/4CAF50/white?text=150x150" 
                 alt="Imagen de ejemplo 150x150px" 
                 class="imagen-150">
            
            <div class="info">
                <p><strong>Dimensiones:</strong> 150px × 150px</p>
                <p><strong>Tipo:</strong> Imagen de placeholder</p>
                <p><strong>Estilo:</strong> Bordes redondeados y sombra</p>
            </div>
            
            <!-- Imagen local (si existe) -->
            <h3>Imagen Local (si existe):</h3>
            <img src="/static/imagen_local.jpg" 
                 alt="Imagen local 150x150px" 
                 class="imagen-150"
                 onerror="this.style.display='none'">
        </div>
    </body>
    </html>
    """
    return html_content


@app.get("/imagen-simple", response_class=HTMLResponse)
def vista_imagen_simple():
    """Vista más simple con solo la imagen"""
    html_simple = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Imagen 150x150</title>
        <style>
            body { text-align: center; padding: 50px; }
            img { width: 150px; height: 150px; border: 1px solid #ccc; }
        </style>
    </head>
    <body>
        <h2>Imagen 150px × 150px</h2>
        <img src="https://via.placeholder.com/150x150/FF6B6B/white?text=Python" alt="Imagen 150x150">
    </body>
    </html>
    """
    return html_simple


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
