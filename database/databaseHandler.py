from model import Customer, Product,session
from sqlalchemy import insert

#from utility.timestamp import timestamp,timecode
import time

def timecode():
    current_time_seconds = int(time.time())
    code = current_time_seconds % 100000000
    return code

def getUserdata(_email):
    global session
    return (
        session.query(
            Customer
        ).where(Customer.email==_email)
    )

def getUserdata_Admin(_email):
    return (
        session.query(
            Customer
        ).where(Customer.email==_email)
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

for i in getUserdata("sammy"):
    print(i)
    print(i.all())

#print(getUserdata("sammy"))
#print(ifexists("dfasdf"))
