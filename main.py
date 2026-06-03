from fastapi import FastAPI
from models import Product

app = FastAPI()


@app.get("/")
def greet():
    return "Hello Delroy!"



products = [ 

Product(id=1, name="Mobile", number=222, price=456),

Product(id=3, name="Cake", number=872, price=100),

Product(id=2, name="Meat", number=767, price=800)



]

# Fetch Data

@app.get("/stuff")
def show_ALL_products():
    return products


@app.get("/stuff/{id}")
def one_product(id: int):
    for product in products:
        if product.id == id:
            return product
        
    return "Product not found"

# Sending Data
@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product


# Updating Data
@app.put("/product/{id}")
def update_product(id: int, product: Product):
    for x in range(len(products)):
        if products[x].id == id:
            products[x] = product
            return "Item updated"
        
    return {"message":"item not found"}


#deleting data

@app.delete("/product/{id}")
def delete_poduct(id: int):
    for x in range(len(products)):
        if products[x].id == id:
            del products[x]
            return "Product deleted successfully"
    
    return "Cannot find product"