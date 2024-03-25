import os,pickle
from utility.fileHandler import DB_PATH, USER_PATH, PRODUCT_PATH
from utility.fileHandler import USER_DB, ORDER_DB, PRODUCT_DB
from utility.fileHandler import USER_NO,PRODUCT_NO

def firstAdmin():
    user_data = {
        "ID": 1,
        "first_name": "Sameer",
        "last_name": "Timsina",
        "gender": "Male",
        "email": "sameer",
        "phone": "9867",
        "pass": "pass",
        "access": "Admin"
    }

    return user_data

def __main__():
    os.makedirs(DB_PATH)
    os.makedirs(USER_PATH)
    os.makedirs(PRODUCT_PATH)

    with open(USER_DB,"wb") as file:
        pickle.dump(firstAdmin(),file)
        os.makedirs(f"{USER_PATH}UID1")
        with open(f"{USER_PATH}UID1/events.log","w") as file:
            pass
        with open(f"{USER_PATH}UID1/orders.db","wb") as file:
            pass

        pass
    with open(PRODUCT_DB,"wb") as file:
        pass
    with open(ORDER_DB,"wb") as file:
        pass
    with open(USER_NO,"w") as file:
        file.write('1')
        pass
    with open(PRODUCT_NO,"w") as file:
        file.write('0')
        pass

    pass

if __name__ == "__main__":
    __main__()