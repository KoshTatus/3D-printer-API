from sqlalchemy import text
from sqlalchemy.orm import Session


def approve_order_db(
        id: int,
        db: Session
):
    query = text(f"""
        UPDATE orders
            SET state=1
            WHERE orders.id={id}
    """)
    db.execute(query)
    db.commit()

def pause_order_db(
        id: int,
        db: Session
):
    query = text(f"""
        UPDATE orders
            SET state=2
            WHERE orders.id={id}
    """)
    db.execute(query)
    db.commit()

def continue_order_db(
        id: int,
        db: Session
):
    query = text(f"""
            UPDATE orders
                SET state=1
                WHERE orders.id={id}
        """)
    db.execute(query)
    db.commit()