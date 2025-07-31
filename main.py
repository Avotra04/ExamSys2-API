from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/ping")
def ping():
    return Response(content="pong", media_type="text/plain", status_code=200)


