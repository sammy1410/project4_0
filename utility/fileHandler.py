from utility.timestamp import timestamp

def product_image(id):
    return f"./database_fold/products/{id}.jpg"

def product_description(id):
    return f"./database_fold/description/{id}.txt"

def customer_dp(id):
    return f"./database_fold/customers/{id}.jpg"

def default_dp(gender):
    if gender == "Female" or gender == "female":
        return f"./database_fold/customers/default_girl_profile.png"
    else:
        return f"./database_fold/customers/default_boy_profile.png"


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