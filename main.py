from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <body style="background-color:blue;color:white;text-align:center;">
        <h1>BLUE VERSION</h1>
        <h2>Release v1.0</h2>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
