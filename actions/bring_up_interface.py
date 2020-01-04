import action

"""
this is a simple example as a starting point demo
more detailed logic and output needs to be added 
"""
class BringUpInterface(action.Action):
    def run(self):
        print("this action is to bring up interface")
        print(self.event)
        device = self.event["device_ID"]
        interface = self.event["element_name"]
        data = "delete interfaces " + interface + " disable"
        print(data)
        result = self.config_junos(data, device, "set")
        return result

