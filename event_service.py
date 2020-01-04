# Use Inheritance for Input Application connection initialization and data flow.
from flask import Flask
from flask import request
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".", "library"))
import healthbot_message_interface,healthbot_message,appformix_message,fluentd_message
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def event_service():
    message = request.json
    print(message)
    #identify application name 
    if "ident" in message.keys() or "value" in message.keys():
        application_name = "fluentd"
    elif "trigger" in message.keys():
        application_name = "healthbot"
    else:
        application_name = "default"
    if application_name == "healthbot":
        event = healthbot_message.HealthbotMessage(message, "healthbot")
    #if event_type == "app1":
    elif application_name == "fluentd":
        #check if it is fluentd jitter 
        if "message" in message.keys():
            if "jitter" in message["message"]:
                event = fluentd_message.FluentdMessageJitter(message, "fluentd")
            else:
                event = fluentd_message.FluentdMessage(message, "fluentd")
        #check if it is fluentd snmp trap
        elif "value" in message.keys():
            if "SNMP" in message["value"]:
                event = fluentd_message.FluentdMessageSNMPTrap(message, "fluentd")
        else:
            event = fluentd_message.FluentdMessage(message, "fluentd")
    print(event)
    event.convert_and_add_to_db()
    converted_data = event.generate_output_message("appformix")
    print("converted data:" + converted_data)
    #create a new output event object to send to AppFormix
    appformix_event = appformix_message.AppFormixMessage(converted_data, "appformix")
    print(appformix_event)
    # send the event to AppFormix
    appformix_event.post_event()
    print("post succesful")
    return json.dumps({"result": "OK"})


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int("10000")
    )




