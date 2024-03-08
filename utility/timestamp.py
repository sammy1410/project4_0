import datetime
import time


def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def timecode():
    current_time_seconds = int(time.time())
    code = current_time_seconds % 100000000
    return code