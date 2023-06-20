from fastapi import FastAPI
from starlette.responses import HTMLResponse
import js2py

app = FastAPI()

@app.get("/")
def run_js():
    # Buat instance dari mesin js2py
    js = js2py.EvalJs()

    # Kode JavaScript yang akan dijalankan
    # javascript_code = '''
    # console.log("Hello, from JavaScript!");
    # '''
    javascript_code = '''
    alert("hai123123")
    '''
    # Jalankan kode JavaScript dengan js2py
    js.execute(javascript_code)

    # Buat respons HTML dengan skrip JavaScript
    html_response = f'''
    <html>
        <body>
            <script>{javascript_code}</script>
        </body>
    </html>
    '''

    return HTMLResponse(content=html_response, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
