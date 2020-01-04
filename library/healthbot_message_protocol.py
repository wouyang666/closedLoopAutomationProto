import healthbot_event

class HealthbotMessageProtocol(healthbot_event.HealthbotEvent):

    def get_bgp_neighbor_address(self):
        return self.message["keys"]["neighbor-address"]

    def get_evpn_instance(self):
        return self.message["keys"]["evpn_instance"]

    def get_lacp_interface(self):
        return self.message["keys"]["lacp_interface_name"]
#{u"group": u"group_all", u"severity": u"normal", u"keys": {u"neighbor-address": u"11.0.0.101", u"_instance_id": u"["check-bgp-state"]", u"_playbook_name": u"check-bgp-state"}, u"device-id": u"vMX-2", u"rule": u"check-bgp-session-state", u"topic": u"protocol.bgp", u"trigger": u"neigbor-state", u"message": u"Neighbor(11.0.0.101) session up"}
"""
 print(json.dumps(message, indent=4))
{
    "group": "group_all",
    "severity": "normal",
    "keys": {
        "neighbor-address": "11.0.0.101",
        "_instance_id": "[\"check-bgp-state\"]",
        "_playbook_name": "check-bgp-state"
    },
    "device-id": "vMX-2",
    "rule": "check-bgp-session-state",
    "topic": "protocol.bgp",
    "trigger": "neigbor-state",
    "message": "Neighbor(11.0.0.101) session up"
}
"""
