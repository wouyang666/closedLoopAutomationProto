import output_message
import requests
import json
import os

class AppFormixMessage(output_message.OutputMessage):
    #get the application ID where the application is originally sent from
    def get_from_application_ID(self):
        payload = json.loads(self.payload)
        return payload["ApplicationId"]

    def get_application_token(self):
        #tempoarily put fix value for server ip and port, 
        #need to change to get it dynamically from a source
        application_ID = self.get_from_application_ID()
        get_application_token_url = os.environ.get("APPFORMIX_URL_BASE") + "/appformix/v1.0/application_registration"
        auth_token = os.environ.get("APPFORMIX_AUTH_TOKEN")
        headers = {
          "Content-Type":"application/json",
          "X-Auth-Type":"appformix",
          "X-Auth-Token":auth_token
        }
        r = requests.get(get_application_token_url, headers=headers, verify=False)
        for i in r.json()["ApplicationsList"]:
            if i["Application"]["ApplicationId"] == application_ID:
                application_token = i["Application"]["ApplicationToken"]
        return application_token

    def post_event(self):
        #tempoarily put fix value for server ip and port, 
        #need to change to get it dynamically from a source
        application_token = self.get_application_token()
        post_event_url_suffix = "/appformix/analytics/v2.0/application_event"
        url = os.environ.get("APPFORMIX_URL_BASE") + post_event_url_suffix
        headers  = {"Content-Type": "application/json", "X-Auth-Type": "appformix", "X-Auth-Token": str(application_token)}
        r = requests.post(url=url, data=self.payload, headers=headers, verify=False)
        return r