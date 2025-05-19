from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.db.database import get_db
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    responses={404: {"description": "Not found"}},
)

# Route for customers to create a new order
@router.post("/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if current_user.role != "customer":
        raise HTTPException(status_code=403, detail="Only customers can create orders")
    return crud.create_order(db=db, order=order, user_id=current_user.id)

# Route for customers to view their orders
@router.get("/", response_model=list[schemas.Order])
def get_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if current_user.role != "customer":
        raise HTTPException(status_code=403, detail="Only customers can view their orders")
    return crud.get_orders_by_user(db=db, user_id=current_user.id, skip=skip, limit=limit)

# Route for admins to view all orders
@router.get("/all", response_model=list[schemas.Order])
def get_all_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can view all orders")
    return crud.get_orders(db=db, skip=skip, limit=limit)

# Route to get a specific order by ID
@router.get("/{order_id}", response_model=schemas.Order)
def get_order(order_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    order = crud.get_order(db, order_id=order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if order.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to view this order")
    return order

# Route to update the status of an order (admin only)
@router.put("/{order_id}/status", response_model=schemas.Order)
def update_order_status(order_id: int, status: schemas.OrderStatusUpdate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can update order status")
    order = crud.get_order(db, order_id=order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return crud.update_order_status(db=db, order_id=order_id, status=status)