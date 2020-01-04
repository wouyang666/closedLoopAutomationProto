from kafka import KafkaConsumer
from json import loads
import json
import identify_event

consumer = KafkaConsumer(
    'eventService',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     value_deserializer=lambda x: x.decode('utf-8'),
     enable_auto_commit=True,
     group_id='event')

#subscribe to eventService
for message in consumer:
    message = message.value
    #print(message)
    #print(message["error_message"])
    #check event type
    
    event = identify_event.identify(message)
    #print(event)
    # reformat event message
    event.format()
    print("print event.message")
    print(event.message)
    # store event in Elasticsearch 
    event.saveToDB()

