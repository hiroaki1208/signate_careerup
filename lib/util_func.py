import datetime

def print_log(msg):
    dt_now = datetime.datetime.now()
    print(f'{dt_now}: {msg}')