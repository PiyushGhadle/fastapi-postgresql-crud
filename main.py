from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session, engine
from sqlalchemy.orm import Session
import database_models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to my page"

products = [
    Product(id=1, name="Phone", description="Budget Phone", price=99.99, quantity=10),
    Product(id=2, name="Laptop", description="Gaming Laptop", price=999.99, quantity=6),
    Product(id=3, name="Headphones", description="Wireless Bluetooth Headphones", price=49.99, quantity=15),
    Product(id=4, name="Smartwatch", description="Fitness Tracking Smartwatch", price=199.99, quantity=8),
    Product(id=5, name="Keyboard", description="Mechanical RGB Keyboard", price=79.99, quantity=12),
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init__db():
    db = session()
    count = db.query(database_models.Product).count()

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))

    db.commit()

init__db()

@app.get("/products")
def get_all_product(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return "Product Not Found"

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product Updated"
    else:
        return "No product Found"

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Deleted Product"
    else:
        return "Product Not Found"



