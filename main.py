from fastapi import FastAPI, Request
from random import randint
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    
    model = {
                "titulo": "GCP Cloud Run",
                "h1": "API de vendas",
                "h4": "Últimas vendas - dados aleatórios"
            }
    
    vendas = [
        [
         x+randint(100, 10000),          # pedido
         f"Cliente {randint(40, 250)}",  # cliente
         f"Filial ({randint(1,10)})",    # loja
         f"Executivo {randint(15, 55)}", # Executivo
         randint(400, 8000)              # valor
        ]
        for x in range(0, randint(5,15))]

    resources = {"request": request, "model": model, "dados":vendas}
    return templates.TemplateResponse("index.html", resources)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)