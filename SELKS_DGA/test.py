# import datetime
# import time

# latest = datetime.datetime.now()
# # while latest % 60:
# now = datetime.datetime.now()

# current_datetime = datetime.datetime.now()  # local date and time
# current_time = datetime.datetime.time(current_datetime)  # time only
# plus_minute = datetime.datetime.time(current_datetime + datetime.timedelta(minutes=1))
# while True:
#     current_datetime = datetime.datetime.now()
#     current_time = datetime.datetime.time(current_datetime)
#     if current_time == plus_minute:
#         print(current_time)
#         plus_minute = datetime.datetime.time(current_datetime + datetime.timedelta(minutes=1))

import threading

def setInterval(func, sec):
    e = threading.Event()
    while not e.wait(sec):
        func()

# from datetime import datetime
# current_datetime = datetime.now()  # local date and time
# current_time = datetime.time(current_datetime)  # time only
# current_date = datetime.date(current_datetime)  # date only
# print(current_date.strftime("%Y.%m.%d"))