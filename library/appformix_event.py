import event

class AppformixEvent(event.Event):
    #init method inherit from InputMessage
    #__init__(self, message):
    #    self.message = message
    #    self.application_name = "healthbot"

    def get_device_ID(self):
        entity_Id = self.message['status']['entityId']
        server_IP = entity_Id.split("__")[1]
        server_IP = server_IP.replace("_",".")
        return server_IP

    def get_device_type(self):
        return self.message["status"]["entityType"]

    def get_severity(self):
        return self.message["spec"]["severity"]

    # message field to be configured to return the actualy value of the metric being monitored
    def get_message(self):
        error_message = self.message["status"]["state"] + " " + self.message["status"]["description"]
        return error_message

    def get_element_name(self):
        return self.message["spec"]["metricType"]

    def get_error_code(self):
        return self.message["spec"]["name"]

    def get_source(self):
        return "appformix"

