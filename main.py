from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/ping")
def ping():
    return Response(content="pong", media_type="text/plain", status_code=200)



@app.get("/home", response_class=HTMLResponse)
def home():
    html_content = """
    <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <h1>Welcome home!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
