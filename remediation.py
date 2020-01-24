import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".", "actions"))
import analyze
from elasticsearch import Elasticsearch
import time

index_name = "test"
elastic_ip = os.environ.get("ELASTIC_IP")
elastic_port = os.environ.get("ELASTIC_PORT")

def get_new_events():
    es = Elasticsearch([{"host": elastic_ip, "port": elastic_port}])
    es_result = es.search(index=index_name, body={"query": {"match": {"status":"new"}}})
    return(es_result)

def update_event_status(event, action_name, result):
    event_id = event["_id"]
    print(event_id)
    es = Elasticsearch([{"host": elastic_ip, "port": elastic_port}])
    source_to_update = {
        "doc": {
            "status": "processed",
            "result": result,
            "action": action_name
        }
    }
    es.update(index=index_name, id=event_id, body=source_to_update)
    print("update finished")



while True:
    try:
        new_events = get_new_events()
        for event in new_events["hits"]["hits"]:
            print(event)
            action = analyze.decide_remidation_action(event["_source"])
            result = action.run()
            update_event_status(event, action.name, result)
    except Exception as e:
        print(e)
    time.sleep(1)
