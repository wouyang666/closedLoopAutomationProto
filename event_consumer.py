from kafka import KafkaConsumer
from json import loads
import json
import identify_event
import os



kafka_ip = os.environ.get("KAFKA_IP")
kafka_port = os.environ.get("KAFKA_PORT")
kafka_server = kafka_ip + ":" + str(kafka_port)

try:
    consumer = KafkaConsumer(
         'event', 'host_cpu',
         bootstrap_servers=[kafka_server],
         auto_offset_reset='earliest',
         value_deserializer=lambda x: x.decode('utf-8'),
         enable_auto_commit=True,
         group_id='event')
except Exception as e:
    print(e)


#subscribe to eventService
try:
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
except Exception as e:
    print(e)