from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.db.database import get_db
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/packages",
    tags=["packages"],
    responses={404: {"description": "Not found"}},
)

# Route to get a list of all packages
@router.get("/", response_model=list[schemas.Package])
def get_packages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_packages(db, skip=skip, limit=limit)

# Route to get a specific package by ID
@router.get("/{package_id}", response_model=schemas.Package)
def get_package(package_id: int, db: Session = Depends(get_db)):
    package = crud.get_package(db, package_id=package_id)
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")
    return package

# Route for admins to create a new package
@router.post("/", response_model=schemas.Package)
def create_package(package: schemas.PackageCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can create packages")
    return crud.create_package(db=db, package=package)

# Route for admins to update an existing package
@router.put("/{package_id}", response_model=schemas.Package)
def update_package(package_id: int, package: schemas.PackageUpdate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can update packages")
    db_package = crud.get_package(db, package_id=package_id)
    if not db_package:
        raise HTTPException(status_code=404, detail="Package not found")
    return crud.update_package(db=db, package_id=package_id, package=package)

# Route for admins to delete a package
@router.delete("/{package_id}", response_model=schemas.Package)
def delete_package(package_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can delete packages")
    db_package = crud.get_package(db, package_id=package_id)
    if not db_package:
        raise HTTPException(status_code=404, detail="Package not found")
    return crud.delete_package(db=db, package_id=package_id)