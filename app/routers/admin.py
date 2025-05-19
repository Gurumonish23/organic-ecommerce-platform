from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.db.database import get_db
from app.dependencies import get_current_admin

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_current_admin)],
    responses={404: {"description": "Not found"}},
)

# Route to create a new product
@router.post("/products", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

# Route to update an existing product
@router.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.update_product(db=db, product_id=product_id, product=product)

# Route to delete a product
@router.delete("/products/{product_id}", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.delete_product(db=db, product_id=product_id)

# Route to view all orders
@router.get("/orders", response_model=list[schemas.Order])
def view_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_orders(db, skip=skip, limit=limit)

# Route to view analytics data
@router.get("/analytics", response_model=schemas.Analytics)
def view_analytics(db: Session = Depends(get_db)):
    return crud.get_analytics(db=db)

# Route to manage nutritionists
@router.post("/nutritionists", response_model=schemas.User)
def create_nutritionist(nutritionist: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=nutritionist, role="nutritionist")

# Route to update a nutritionist
@router.put("/nutritionists/{nutritionist_id}", response_model=schemas.User)
def update_nutritionist(nutritionist_id: int, nutritionist: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_nutritionist = crud.get_user(db, user_id=nutritionist_id)
    if not db_nutritionist or db_nutritionist.role != "nutritionist":
        raise HTTPException(status_code=404, detail="Nutritionist not found")
    return crud.update_user(db=db, user_id=nutritionist_id, user=nutritionist)

# Route to delete a nutritionist
@router.delete("/nutritionists/{nutritionist_id}", response_model=schemas.User)
def delete_nutritionist(nutritionist_id: int, db: Session = Depends(get_db)):
    db_nutritionist = crud.get_user(db, user_id=nutritionist_id)
    if not db_nutritionist or db_nutritionist.role != "nutritionist":
        raise HTTPException(status_code=404, detail="Nutritionist not found")
    return crud.delete_user(db=db, user_id=nutritionist_id)