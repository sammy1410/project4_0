import time 
import datetime

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def timecode():
    current_time_seconds = int(time.time())
    print(current_time_seconds)
    code = current_time_seconds % 100000000
    print(code)
    return code

def timestamp_int():
    date_time_str = "2024-03-08 12:30:45"
    date_time_obj = datetime.datetime.now().strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
    print(date_time_obj)
    return date_time_obj

timestamp_int().year