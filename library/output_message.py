import requests

class OutputMessage:
    def __init__(self, payload, to_application):
        self.payload = payload
        #application name where to send event to
        self.to_application = to_application

'''
    def post_event(self):
        if self.application == "appformix":
            url = "http://10.49.68.44:9000/appformix/analytics/v2.0/application_event"
            headers  = {"Content-Type": "application/json", "X-Auth-Type": "appformix", "X-Auth-Token":"9ad32c42-b93d-11e9-b7db-0242ac120005"}
        elif self.application == "app2":
            url = "http for app2"
        #more destination app can be added
        r = requests.post(url=url, data=self.payload, headers=headers, verify=False)
        return r
'''


