from pydantic import BaseModel



class Product(BaseModel):
    id : int
    name : str
    number : int
    price : int 


