from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import socket
import os
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <body style="background-color:blue;color:white;text-align:center;">
        <h1>BLUE VERSION</h1>
        <h2>Release v1.1.0</h2>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {
        "application": "color-app",
        "version": os.getenv("APP_VERSION", "unknown"),
        "commit": os.getenv("GIT_COMMIT", "unknown"),
        "build_date": os.getenv("BUILD_DATE", "unknown"),
        "hostname": socket.gethostname()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
