from fastapi import FastAPI
from models import Product
from database import session, engine
import database_models


database_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Fetch Data
@app.get("/")
def greet():
    return "Hello Delroy!"



products = [ 

Product(id=1, name="Mobile", number=222, price=550),

Product(id=3, name="Cake", number=872, price=1209),

Product(id=2, name="Meat", number=767, price=1800),

Product(id=4, name="Bamboo", number=968, price=9000),


]

# Database Initialise
def init_db():
    db = session()

    count = db.query(database_models.Product).count()

# Check if database is empty
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()


init_db()

# Fetch All Data
@app.get("/stuff")
def show_ALL_products():
    db = session()
    db.query()

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


# Deleting Data

@app.delete("/product/{id}")
def delete_poduct(id: int):
    for x in range(len(products)):
        if products[x].id == id:
            del products[x]
            return "Product deleted successfully"
    
    return "Cannot find product"