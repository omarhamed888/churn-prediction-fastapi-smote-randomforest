from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>FastAPI Badge</title>
            <style>
                body { background: #f4f4f4; font-family: Arial, sans-serif; }
                .badge {
                    margin: 100px auto;
                    width: 350px;
                    padding: 30px;
                    background: #fff;
                    border-radius: 16px;
                    box-shadow: 0 4px 24px rgba(0,0,0,0.08);
                    text-align: center;
                }
                .badge-title {
                    font-size: 2em;
                    color: #009688;
                    margin-bottom: 10px;
                }
                .badge-desc {
                    color: #555;
                    font-size: 1.1em;
                }
            </style>
        </head>
        <body>
            <div class="badge">
                <div class="badge-title">🚀 FastAPI is Running!</div>
                <div class="badge-desc">Your FastAPI app is live.<br>Try adding endpoints or explore the <a href="/docs">API docs</a>.</div>
            </div>
        </body>
    </html>
    """
