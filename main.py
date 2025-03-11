from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Annotated

class Item(BaseModel):
    pnumero: str
    snumero: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/suma")
def suma(numero: Annotated[Item, Form()]):
    x=float(numero.pnumero)
    y=float(numero.snumero)
    resultado = x + y
    return str(resultado)

@app.post("/resta")
def resta(numero: Annotated[Item, Form()]):
    x = float(numero.pnumero)
    y = float(numero.snumero)
    resultado = x - y
    return str(resultado)

@app.post("/multiplicacion")
def multiplicacion(numero: Annotated[Item, Form()]):
    x = float(numero.pnumero)
    y = float(numero.snumero)
    resultado = x * y
    return str(resultado)

@app.post("/division")
def division(numero: Annotated[Item, Form()]):
    x = float(numero.pnumero)
    y = float(numero.snumero)
    
    if y == 0:
        return {"error": "No se puede dividir entre 0"}
    
    resultado = x / y
    return str(resultado)
