from fastapi.responses import FileResponse
import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

products = []

class Product(BaseModel):
    name: str
    img: str
    price: float
    description: str

products.append(Product(name="Chair", img="chair.webp", price=99.0, description="Stylish chair"))
products.append(Product(name="Counch", img="counch.webp", price=999.0, description="Stylish counch"))

products = [{"id": i + 1, **product.dict()} for i, product in enumerate(products)]

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
