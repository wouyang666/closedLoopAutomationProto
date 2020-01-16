import json
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".", "library"))
import healthbot_event,fluentd_message,appformix_event
   
def identify(message):
    try:
        message = json.loads(message)
        print(message)
        if "ident" in message.keys() or "value" in message.keys():
            application_name = "fluentd"
        elif "trigger" in message.keys():
            application_name = "healthbot"
        elif "kind" in message.keys():
            application_name = "appformix"
        else:
            application_name = "default"
        print("application name:" + application_name)
        if application_name == "healthbot":
            event = healthbot_event.HealthbotEvent(message)
        #if event_type == "app1":
        elif application_name == "appformix":
            event = appformix_event.AppformixEvent(message)
        elif application_name == "fluentd":
            #check if it is fluentd jitter 
            if "message" in message.keys():
                if "jitter" in message["message"]:
                    event = fluentd_message.FluentdMessageJitter(message)
                else:
                    event = fluentd_message.FluentdMessage(message)
            #check if it is fluentd snmp trap
            elif "value" in message.keys():
                if "SNMP" in message["value"]:
                    event = fluentd_message.FluentdMessageSNMPTrap(message)
            else:
                event = fluentd_message.FluentdMessage(message)
        else:
             event = message
    except Exception as e:
        print("invalid format")
        print(e)
        event = message
    return event

