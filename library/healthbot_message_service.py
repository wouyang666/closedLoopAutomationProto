import healthbot_event

class HealthbotMessageService(healthbot_event.HealthbotEvent):
    def get_alarm_element(self):
        element = dict()
        #assume that the value is returned in the message field
        element["value"] = healthbot_message.HealthbotMessage.get_message()
        event_ID = healthbot_message.HealthbotMessage.get_event_ID()
        #including service-set-packet-drop-statistics/cpulimit-drops + memlimit-drops + flowlimit-drops
        if "service_set_errors"in event_ID:
            element["service_set_name"] = get_service_set_name()
            element["interface_name"] = get_interface_name()
        elif event_ID == "ip_sec_ikes_status":
            print()
        elif event_ID == "ip_sec_sas_status":
            print()
        return element
        # more event types to add
# e.g. IPsecSAStatistics,GVPN_KEK_SA,GVPN_SA_Status,FW_HighAvailability

    def get_service_set_name(self):
        return self.message["keys"]["service-set-name"]

    def get_interface_name():
        return self.message["keys"]["interface-name"]


"""
#sample cli output:
user@host> show services service-sets cpu-usage

Interface   Service set (system category)                   CPU utilization %
sp-4/1/0    idp_recommended                                           18.20 %
sp-4/1/0    Idle                                                      44.69 %
sp-4/1/0    System                                                     7.01 %
sp-4/1/0    Receive                                                   15.10 %
sp-4/1/0    Transmit                                                  15.00 %
"""
