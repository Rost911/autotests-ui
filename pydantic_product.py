# pydantic_product.py
from pydantic import BaseModel, Field
from typing import List


class Market(BaseModel):
    id: int
    name: str


class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Price should be greater than 0")
    tags: List[str] = []
    market: Market


product_data = {
    "name": "Phone",
    "price": 499.99,
    "tags": ["electronics", "smartphone"],
    "market": {
        "id": 1,
        "name": "Amazon"
    }
}

product = Product(**product_data)
print(product)
