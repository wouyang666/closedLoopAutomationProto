import os
import action

class RestartServer(action.Action):
    def run(self):
        print("action is restart server")
        """
        print(vars(event))
        device = event.device_ID
        user = "mememe"
        command_to_run = "ssh -t " + user + "@" + device + " 'sudo reboot'"
        os.system(command_to_run)
        """
        result = "succesful"
        return result