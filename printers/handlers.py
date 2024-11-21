from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.db import get_db
from printers.db_utils import get_printers_db, add_printers_db

router = APIRouter(
    tags=["printers"]
)


@router.get("/printers/all", status_code=status.HTTP_200_OK)
def get_all_orders(
        db: Session = Depends(get_db)
):
    return {
        "data": get_printers_db(db)
    }


@router.post("/printers/add")
def add_printers(
        db: Session = Depends(get_db)
):
    add_printers_db(db)
