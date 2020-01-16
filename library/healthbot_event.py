import event

class HealthbotEvent(event.Event):
    #init method inherit from InputMessage
    #__init__(self, message):
    #    self.message = message
    #    self.application_name = "healthbot"

    def get_event_ID(self):
        return self.message["trigger"]

    def get_device_ID(self):
        return self.message["device-id"]

    def get_device_type(self):
        return "network"

    def get_severity(self):
        return self.message["severity"]

    # message field to be configured to return the actualy value of the metric being monitored
    def get_message(self):
        return self.message["message"]

    def get_element_name(self):
        return self.message["keys"]["element_name"]

    def get_error_code(self):
        return self.message["trigger"]

    def get_source(self):
        return "healthbot"

"""
    def convert_and_add_to_db(self):
        event = {
                timestamp: datetime.now
                device_ID: get_device_ID(),
                device_type: "network",
                vendor: "Juniper",
                element_name: get_element_name(),
                error_code: get_event_ID(),
                error_message: get_message(),
                status: "new",
                result: "none"
        }
        input_message.add_to_elastic(event)
"""


"""
event from hb format:
{u"group": u"group_all", u"severity": u"major", u"keys": {u"_instance_id": u"["rpm-all"]", u"rpm-test-name": u"ge-0/0/0.0", u"_playbook_name": u"playbook-rpm"}, u"device-id": u"vMX-7", u"rule": u"rpm", u"topic": u"external", u"trigger": u"trigger_1", u"message": u"Rtt over threshold"}

convert to json
{
    "group": "group_all",
    "severity": "major",
    "keys": {
        "_instance_id": "[\"rpm-all\"]",
        "rpm-test-name": "ge-0/0/0.0",
        "_playbook_name": "playbook-rpm"
    },
    "device-id": "vMX-7",
    "rule": "rpm",
    "topic": "external",
    "trigger": "trigger_1",
    "message": "Rtt over threshold"
}
"""