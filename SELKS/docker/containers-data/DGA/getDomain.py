import requests
# import datetime
import json

def getDomains(url):
    domains = []
    headers = {"Content-Type": "application/json"}
    data = {"query": {"range": {"@timestamp": {"gte": "now-15m/m", "lt": "now"}}}, "fields": ["_source.dns.rrname"], "_source": "false"}

    responses = requests.get(url, headers=headers, data=json.dumps(data)).json()

    for response in responses["hits"]["hits"]:
        # strTime = response["_source"]["timestamp"].split("T")[1].split(".")[0]
        # time_obj = datetime.datetime.strptime(strTime, '%H:%M:%S').time()

        # current_datetime = datetime.datetime.now()  # local date and time
        # current_time = datetime.datetime.time(current_datetime)  # time only

        # print("!!!\n", current_time)
        # print(time_obj)
        # print(datetime.datetime.combine(datetime.datetime.min, time_obj) - datetime.datetime.combine(datetime.datetime.min, current_time))

        domain = response["_source"]["dns"]["rrname"]
        if domain not in domains:
            domains.append(domain)

    return domains
