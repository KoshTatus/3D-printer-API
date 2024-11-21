from sqlalchemy import text
from sqlalchemy.orm import Session

from database.orm import Size, PrintersOrm
from schemas.printer_schemas import PrinterModel, PrinterCreate


def get_printers_db(
        db: Session
):
    query = text(f"""
            SELECT * FROM printers
        """)

    result = db.execute(query).all()

    return [PrinterModel(
        id=row[0],
        name=row[1],
        size=Size(
            width=row[2],
            length=row[3],
            heigth=row[4]
        ),
        remainPlastic=row[5],
        state=row[6]
    )
        for row in result]

def get_printer_by_id(
        id: int,
        db: Session
):
    query = text(f"""
                SELECT * FROM printers
                    WHERE printers.id = {id}
            """)

    row = db.execute(query).first()

    return PrinterModel(
        id=row[0],
        name=row[1],
        size=Size(
            width=row[2],
            length=row[3],
            heigth=row[4]
        ),
        remainPlastic=row[5],
        state=row[6]
    )


def add_printers_db(
        db: Session
):
    new_printer = PrintersOrm(
        name="Creality K1",
        size=Size(
            width=220,
            length=220,
            heigth=250
        ),
        remainPlastic=1000,
        state=1
    )
    db.add(new_printer)
    db.commit()
    db.refresh(new_printer)

    new_printer = PrintersOrm(
        name="Bambu Lab P1S",
        size=Size(
            width=256,
            length=256,
            heigth=256
        ),
        remainPlastic=2000,
        state=1
    )
    db.add(new_printer)
    db.commit()
    db.refresh(new_printer)

    new_printer = PrintersOrm(
        name="Bambu Lab P1S",
        size=Size(
            width=256,
            length=256,
            heigth=256
        ),
        remainPlastic=0,
        state=0
    )
    db.add(new_printer)
    db.commit()
    db.refresh(new_printer)