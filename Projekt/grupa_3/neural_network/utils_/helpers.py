
from datetime import datetime
import time

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def parse_execution_time(execution_time):
    return str(int(execution_time))
    #return time.strftime("%H:%M:%S", time.gmtime(execution_time))