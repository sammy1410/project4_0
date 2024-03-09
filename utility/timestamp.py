import datetime
import time


def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def timeorder():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def earliestdelivery():
    current_datetime = datetime.datetime.now()
    new_datetime = current_datetime + datetime.timedelta(days=5)
    return new_datetime

def timecode():
    current_time_seconds = int(time.time())
    code = current_time_seconds % 100000000
    return code