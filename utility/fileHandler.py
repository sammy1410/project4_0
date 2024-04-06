from utility.timestamp import timestamp
import pickle

DB_PATH = "./database/"

USER_DB = "./database/users.db"
ORDER_DB = "./database/orders.db"
PRODUCT_DB = "./database/products.db"
PRODUCT_NO = "./database/productNo"
USER_NO = "./database/userNo"

USER_PATH = "./database/users/"
PRODUCT_PATH = "./database/products/"
TMP_PATH = "./tmp/"

default_male = "./images/default_boy_profile.png"
default_female= "./images/default_girl_profile.png"
default_product= "./images/default_product.png"


def user_events_file(UID):
    return f"{USER_PATH}UID{UID}/events.log"

def user_orders_file(UID):
    return f"{USER_PATH}UID{UID}/orders.db"

def user_image(UID):
    return f"{USER_PATH}UID{UID}/profile_pic.png"

def product_image(PID):
    return f"{PRODUCT_PATH}PID{PID}/image.jpg"

def product_info(PID):
    return f"{PRODUCT_PATH}PID{PID}/infoFile"

def product_data(pid):
    product_entry=None
    with open(PRODUCT_DB,"rb") as product_db:
        while True:
            try:
                entry= pickle.load(product_db)
                if entry["ID"] == pid:
                    product_entry = entry
                    break
            except EOFError:
                break
    return product_entry

def write_output(mesg):
    with open("./logs/output.log","a") as output_logs:
        output_logs.write(f"[{timestamp()}] : {mesg}\n")
    
def write_error(mesg):
    with open("./logs/error.log","a") as error_logs:
        error_logs.write(f"[{timestamp()}] : {mesg}\n")
        
def write_mesg(mesg):
    with open("./logs/msg.log","a") as msg_logs:
        msg_logs.write(f"[{timestamp()}] : {mesg}\n")

def SCADA_log(mesg):
    with open("./logs/SCADA.log","a") as SCADA_logs:
        SCADA_logs.write(f"[{timestamp()}] : {mesg}\n")

def create_files():
    
    init_log=f"""
    --------------------------------

    {timestamp()} Program started
    
    --------------------------------
    
    """
    write_error(init_log)
    write_mesg(init_log)
    write_output(init_log)