import os
import action

class RestartServer(action.Action):
    def run(self):
        try:
            print("action is to restart server")
            #print(vars(event))
            device = self.event["device_ID"]
            user = "jcluser"
            command_to_run = "ssh -t " + user + "@" + device + " 'sudo reboot'"
            os.system(command_to_run)
            result = "succesful"
        except Exception as e:
            print(e)
            result = "failed"
            print(result) 
        return result