import event
import jinja2
import datetime

class HealthbotEvent(event.Event):
    #init method inherit from InputMessage
    #__init__(self, message):
    #    self.message = message
    #    self.application_name = "healthbot"

    def get_event_ID(self):
        return self.message["trigger"]

    def get_device_ID(self):
        return self.message["device-id"]

    def get_severity(self):
        return self.message["severity"]

    # message field to be configured to return the actualy value of the metric being monitored
    def get_message(self):
        return self.message["message"]

    def get_element_name(self):
        return self.message["keys"]["element_name"]

    def get_error_code(self):
        return self.message["trigger"]

    def generate_output_message(self,output_message_type):
        #j2_env = Environment(loader=PackageLoader("application_events", "templates"))
        templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
        j2_env = jinja2.Environment(loader=templateLoader)
        j2_env.lstrip_blocks = True
        j2_env.trim_blocks = True
        if output_message_type == "appformix":
            payload = j2_env.get_template("appformix_event_payload.j2").render(
                event_ID = self.get_event_ID(),
                element_name = self.get_element_name(),
                Application_ID = "healthbot",
                device_ID = self.get_device_ID(),
                message = self.get_message(),
                severity = self.get_severity()
            )
        # other output message format can be added
        elif output_message_type == "app2":
            print("to be added")

        return payload

    def format(self):
        timeNow = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        try:
            new_message = {
                "device_ID": self.get_device_ID(),
                "device_type": "network",
                "timestamp": timeNow,
                "vendor": "Juniper",
                "element_name" : self.get_element_name(),
                "error_code": self.get_error_code(),
                "error_message": self.get_message(),
                "status": "new",
                "action": "none",
                "source": "healthbot",
                "result": "none"
            }
            self.message = new_message
        except:
            print("exception happened")
            raise

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