from fastapi import FastAPI, Response
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import List
from datetime import datetime

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

@app.exception(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return HTMLResponse(
            content="""
            <html>
                <head><title>404</title></head>
                <body>
                    <h1>404 NOT FOUND</h1>
                </body>
            </html>
            """,
            status_code=404
        )