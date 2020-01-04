import jinja2
import json
import requests
import json
from elasticsearch import Elasticsearch

index_name = "test"

class Event:
    def __init__(self, message):
        self.message = message

    def get_source(self):
        return self.source

    def saveToDB(self):
        es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        #use vars() to convert obj to dic and add to elasticsearch
        es.index(index=index_name, body = self.message)
        print("saved to Elastic")
