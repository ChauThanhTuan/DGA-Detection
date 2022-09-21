import requests
import json

def getDomains(url):
    domains = []
    headers = {"Content-Type": "application/json"}
    data = { "aggs": { "0": { "terms": { "field": "dns.rrname.raw", "order": { "1": "desc" }, "size": 10000 }, "aggs": { "1": { "cardinality": { "field": "dns.rrname.raw" } } } } }, "size": 0, "query": { "bool": { "filter": [ { "range": { "@timestamp": { "format": "strict_date_optional_time", "gte": "now-15m", "lte": "now" } } } ] } } }

    responses = requests.get(url, headers=headers, data=json.dumps(data)).json()

    for response in responses["aggregations"]["0"]["buckets"]:
        domain = response["key"]
        if domain not in domains:
            domains.append(domain)

    return domains
