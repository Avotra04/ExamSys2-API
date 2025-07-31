from fastapi import FastAPI, Response, status
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI()

posts_db = []

class Post(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime

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

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(new_posts: List[Post]):
    posts_db.extend(new_posts)
    return posts_db

@app.exception_handler(StarletteHTTPException)
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
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )
