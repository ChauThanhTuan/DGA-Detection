import requests
import datetime

def start(url):
    domains = []
    responses = requests.get(url).json()
    id = responses["hits"]["hits"][0]["_id"]

    for response in responses["hits"]["hits"]:
        domains.append(response["_source"]["dns"]["rrname"])

    return (id, domains)

def getDomains(url, id):
    domains = []
    responses = requests.get(url).json()

    for response in responses["hits"]["hits"]:
        # strTime = response["_source"]["timestamp"].split("T")[1].split(".")[0]
        # time_obj = datetime.datetime.strptime(strTime, '%H:%M:%S').time()

        # current_datetime = datetime.datetime.now()  # local date and time
        # current_time = datetime.datetime.time(current_datetime)  # time only

        # print("!!!\n", current_time)
        # print(time_obj)
        # print(datetime.datetime.combine(datetime.datetime.min, time_obj) - datetime.datetime.combine(datetime.datetime.min, current_time))
        if response["_id"] == id:
            break

        domains.append(response["_source"]["dns"]["rrname"])

    id = responses["hits"]["hits"][0]["_id"]

    return (id, domains)
