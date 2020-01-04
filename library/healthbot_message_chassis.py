import healthbot_event

class HealthbotMessageChassis(healthbot_event.HealthbotEvent):

    def get_slot_number(self):
        return self.message["keys"]["slot"]

    def get_fan_number(self):
        return self.message["keys"]["fan"]

    def get_pfe_number(self):
        return self.message["keys"]["pfe"]

    def get_fabric_plane(self):
        return self.message["keys"]["fabric_plane"]

    




"""
{u"group": u"group_all", u"severity": u"major", u"keys": {u"slot": u"0", u"_instance_id": u"["device-cpu"]", u"_playbook_name": u"device-cpu"}, u"device-id": u"vMX-2", u"rule": u"check-system-cpu-load-average", u"topic": u"system.cpu", u"trigger": u"cpu-utilization-1min", u"message": u"Routing Engine0 1min CPU utilization(99) exceed high threshold(cpu-utilization-1min-high-threshold)"}

converted
>>> print(json.dumps(message, indent=4))
{
    "group": "group_all",
    "severity": "major",
    "keys": {
        "slot": "0",
        "_instance_id": "[\"device-cpu\"]",
        "_playbook_name": "device-cpu"
    },
    "device-id": "vMX-2",
    "rule": "check-system-cpu-load-average",
    "topic": "system.cpu",
    "trigger": "cpu-utilization-1min",
    "message": "Routing Engine0 1min CPU utilization(99) exceed high threshold(cpu-utilization-1min-high-threshold)"
}
"""

