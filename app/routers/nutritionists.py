from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.db.database import get_db
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/nutritionists",
    tags=["nutritionists"],
    responses={404: {"description": "Not found"}},
)

# Route to get a list of all nutritionists
@router.get("/", response_model=list[schemas.User])
def get_nutritionists(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users_by_role(db, role="nutritionist", skip=skip, limit=limit)

# Route to get a specific nutritionist by ID
@router.get("/{nutritionist_id}", response_model=schemas.User)
def get_nutritionist(nutritionist_id: int, db: Session = Depends(get_db)):
    nutritionist = crud.get_user(db, user_id=nutritionist_id)
    if not nutritionist or nutritionist.role != "nutritionist":
        raise HTTPException(status_code=404, detail="Nutritionist not found")
    return nutritionist

# Route for customers to book an appointment with a nutritionist
@router.post("/{nutritionist_id}/appointments", response_model=schemas.Appointment)
def book_appointment(nutritionist_id: int, appointment: schemas.AppointmentCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if current_user.role != "customer":
        raise HTTPException(status_code=403, detail="Only customers can book appointments")
    return crud.create_appointment(db=db, appointment=appointment, customer_id=current_user.id, nutritionist_id=nutritionist_id)

# Route for nutritionists to view their appointments
@router.get("/{nutritionist_id}/appointments", response_model=list[schemas.Appointment])
def get_appointments(nutritionist_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if current_user.id != nutritionist_id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to view these appointments")
    return crud.get_appointments_by_nutritionist(db=db, nutritionist_id=nutritionist_id)