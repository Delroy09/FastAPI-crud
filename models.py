from pydantic import BaseModel


# Pydantic Model Creation

class Product(BaseModel):
    id : int
    name : str
    number : int
    price : int 


