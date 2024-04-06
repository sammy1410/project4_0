import time
from sqlalchemy import insert

if __name__ == "__main__":
    from model import Customer, Product,session,session_local
else:
    from database_fold.model import Customer, Product,session,session_local

def getUserdata(_email):
    return (
        session.query(
            Customer
        ).where(Customer.email==_email).scalar()
    )

def customersAll():
    return(
        session.query(
            Customer
        ).all()
    )
def customerslimited(no):
    return(
        session.query(
            Customer
        ).limit(no).all()
    )

def addUser(data):
    new = insert(Customer).values(data)

    session.execute(new)
    session.commit()

def entryExists(email):
    exists = session.query(
        session.query(Customer).filter_by(email=email).exists()
    ).scalar()
    return exists

def productEntryExists(_id):
    return(
        session.query(
            session.query(Product).filter_by(id=_id).exists()
        ).scalar()
    )

def addProduct(data):
    add = insert(Product).values(data)

    session.execute(add)
    session.commit()

def productAll():
    return(
        session.query(
            Product
        ).all()
    )

def productlimited(no):
    return (
        session.query(
            Product
        ).limit(no).all()
    )

def productDetails(_id):
    return(
        session.query(
            Product
        ).filter(Product.id==_id).first()
    )
