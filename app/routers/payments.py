from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.db.database import get_db
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/payments",
    tags=["payments"],
    responses={404: {"description": "Not found"}},
)

# Route to process a payment for an order
@router.post("/", response_model=schemas.Payment)
def process_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    order = crud.get_order(db, order_id=payment.order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if order.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to pay for this order")
    if order.status != "pending":
        raise HTTPException(status_code=400, detail="Order is not pending payment")
    return crud.create_payment(db=db, payment=payment)

# Route to get payment details by payment ID
@router.get("/{payment_id}", response_model=schemas.Payment)
def get_payment(payment_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    payment = crud.get_payment(db, payment_id=payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    if payment.order.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to view this payment")
    return payment

# Route for admins to view all payments
@router.get("/all", response_model=list[schemas.Payment])
def get_all_payments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can view all payments")
    return crud.get_payments(db=db, skip=skip, limit=limit)