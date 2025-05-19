from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.db.database import get_db
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)

# Route to get a list of all products
@router.get("/", response_model=list[schemas.Product])
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

# Route to get a specific product by ID
@router.get("/{product_id}", response_model=schemas.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Route for admins to create a new product
@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can create products")
    return crud.create_product(db=db, product=product)

# Route for admins to update an existing product
@router.put("/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can update products")
    db_product = crud.get_product(db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.update_product(db=db, product_id=product_id, product=product)

# Route for admins to delete a product
@router.delete("/{product_id}", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can delete products")
    db_product = crud.get_product(db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.delete_product(db=db, product_id=product_id)