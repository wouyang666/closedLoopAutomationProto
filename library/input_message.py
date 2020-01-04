import jinja2
import json
import requests
import json
from elasticsearch import Elasticsearch


class InputMessage:
    def __init__(self, message, application_name):
        self.message = message
        self.application_name = application_name

    def get_application_name(self):
        return self.application_name

    def add_to_elastic(self, event):
        es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        #use vars() to convert obj to dic and add to elasticsearch
        es.index(index='events', body = event)
