from fastapi.responses import FileResponse
import os
from fastapi import FastAPI

app = FastAPI()

products = [
    {
        "name": "Chair",
        "img": "chair.webp",
        "price": 99,
        "description": "Stylish chair"
    },
    
    {
        "name": "Counch",
        "img": "counch.webp",
        "price": 999,
        "description": "Stylish counch"
    },
]

products = [{"id": i+1, **productItem} for i, productItem in enumerate(products)]

# Routes
@app.get("/product/{id}")
def product(id: int):
    product = next((productItem for productItem in products if productItem["id"] == id), None)
    if product:
        return product
    return {"erro": "Produto não encontrado"}

@app.get("/product/{id}/image")
def get_imagem(id: int):
    product = next((productItem for productItem in products if productItem["id"] == id), None)
    
    if product:
        img_url = os.path.join("images", product["img"])
        if not os.path.isfile(img_url):
            return {"erro": "Imagem não encontrada"}
        return FileResponse(img_url)
    
    return {"erro": "Produto não encontrado"}
