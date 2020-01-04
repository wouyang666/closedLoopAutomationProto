import healthbot_event

class HealthbotMessageInterface(healthbot_event.HealthbotEvent):

    def get_interface_name(self):
        return self.message["keys"]["element_name"]


"""
{u"group": u"group_all", u"severity": u"major", u"keys": {u"_instance_id": u"["check_interface_status"]", u"interface-name": u"ge-0/0/6", u"_playbook_name": u"check_interface_status"}, u"device-id": u"vMX-5", u"rule": u"check-interface-status", u"topic": u"interface.statistics", u"trigger": u"link-state", u"message": u"ge-0/0/6 link operator status is DOWN"}

convert to json
{
    "group": "group_all",
    "severity": "major",
    "keys": {
        "_instance_id": "[\"check_interface_status\"]",
        "interface-name": "ge-0/0/6",
        "_playbook_name": "check_interface_status"
    },
    "device-id": "vMX-5",
    "rule": "check-interface-status",  eventID
    "topic": "interface.statistics",
    "trigger": "link-state",
    "message": "ge-0/0/6 link operator status is DOWN"
}

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


