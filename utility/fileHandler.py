import datetime

error_logs = None
msg_logs = None
output_logs = None

def create_files():
    global error_logs,msg_logs,output_logs
    error_logs=open("./logs/error.log","a")
    msg_logs=open("./logs/msg.log","a")
    output_logs=open("./logs/output.log","a")
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    init_log=f"""
    --------------------------------

    {timestamp} Program started
    
    --------------------------------
    
    """
    msg_logs.write(init_log)
    output_logs.write(init_log)
    error_logs.write(init_log)
    output_logs.close()
    msg_logs.close()
    error_logs.close()
    

def write_output(mesg):
    output_logs=open("./logs/output.log","a")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    formatted = f"[{timestamp}] : {mesg}\n"
    output_logs.write(formatted)
    
    output_logs.close()
    
def write_error(mesg):
    error_logs=open("./logs/error.log","a")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    formatted = f"[{timestamp}] : {mesg}\n"
    error_logs.write(formatted)
    
    error_logs.close()
        

def write_mesg(mesg):
    msg_logs=open("./logs/msg.log","a")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    formatted = f"[{timestamp}] : {mesg}\n"
    msg_logs.write(formatted)

    msg_logs.close()
    