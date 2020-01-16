from elasticsearch import Elasticsearch
import datetime

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

    def format(self):
        timeNow = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        try:
            new_message = {
                "device_ID": self.get_device_ID(),
                "device_type": self.get_device_type(),
                "timestamp": timeNow,
                "vendor": "na",
                "element_name" : self.get_element_name(),
                "error_code": self.get_error_code(),
                "error_message": self.get_message(),
                "status": "new",
                "action": "none",
                "source": self.get_source(),
                "result": "none"
            }
            self.message = new_message
        except Exception as e:
            print(e)