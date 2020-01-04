import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".", "actions"))
import analyze
from elasticsearch import Elasticsearch
import time

index_name = "test"
def get_new_events():
    es = Elasticsearch([{"host": "localhost", "port": 9200}])
    es_result = es.search(index=index_name, body={"query": {"match": {"status":"new"}}})
    return(es_result)

def update_event_status(event, action_name, result):
    event_id = event["_id"]
    print(event_id)
    es = Elasticsearch([{"host": "localhost", "port": 9200}])
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
    new_events = get_new_events()
    for event in new_events["hits"]["hits"]:
        print(event)
        action = analyze.decide_remidation_action(event["_source"])
        result = action.run()
        update_event_status(event, action.name, result)
    time.sleep(1)
