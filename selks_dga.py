from getDomain import getDomains, start
from predictDGA import get_prediction

from datetime import datetime, timezone
import pytz
import threading

id = None

def setInterval(func, sec):
    e = threading.Event()
    while not e.wait(sec):
        func()

def main():
    global id
    current_datetime = datetime.now()  # local date and time
    UTC = pytz.utc
    current_datetime = UTC.localize(current_datetime)
    VN_TZ = pytz.timezone('Asia/Ho_Chi_Minh')
    current_datetime = current_datetime.astimezone(VN_TZ)
    # current_date = current_date.replace(tzinfo=timezone.utc+7)
    current_time = datetime.time(current_datetime)  # time only
    current_date = datetime.date(current_datetime)  # date only

    print("\n=====================================================================================")
    print("Current: ", current_datetime)
    print("=====================================================================================\n")

    if id:
        url = f'http://172.16.60.10:9200/logstash-dns-{current_date.strftime("%Y.%m.%d")}/_search?pretty&&size=100'
        id, domains = getDomains(url, id)
    else:
        url = f'http://172.16.60.10:9200/logstash-dns-{current_date.strftime("%Y.%m.%d")}/_search'
        id, domains = start(url)
    
    get_prediction(domains, show=True)

if __name__ == "__main__":
    setInterval(main, 10)