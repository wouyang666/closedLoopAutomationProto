import smtplib
import action

class DefaultActionJunos(action.Action):
    def run(self):
        print("defalt action")
        device = self.event["device_ID"]
        junos_version_info = self.get_junos_version(device)
        junos_config = self.get_junos_config(device)
        #save result to file
        file_location_version = "/tmp/show_version.txt"
        file_location_config = "/tmp/show_config.txt"
        files = [file_location_version, file_location_config]
        text_file = open(file_location_version, "w")
        text_file.write(junos_version_info)
        text_file.close()
        text_file = open(file_location_config, "w")
        text_file.write(junos_config)
        text_file.close()
        self.email_result("wouyang@juniper.net", "from event service", "please take a look", files)
