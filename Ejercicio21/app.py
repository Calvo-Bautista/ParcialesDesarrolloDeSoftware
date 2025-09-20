# hacer una aplicacion web que muestre el texto en rojo

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/linearoja", response_class=HTMLResponse)
def linearoja():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Texto en Rojo</title>
    </head>
    <body>
        <p style="color: red;">hola mundo</p>
    </body>
    </html>
    """
    return html_content


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
