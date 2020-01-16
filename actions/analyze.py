import time
import bring_up_interface, put_under_maintenance, restart_server, default_action_junos, no_action

def decide_remidation_action(event):
    try:
        print(event["error_code"])
        print("decide action")
        time.sleep(2)
        if event["error_code"] == "interface_down":
            remediation = bring_up_interface.BringUpInterface(event, "BringUpInterface")
        elif event["error_code"] == "host_cpu":
            if "active" in event["error_message"]:
                remediation = restart_server.RestartServer(event, "RestartServer")
                remediation = no_action.NoAction(event, "NoAction")
            else:
                remediation = no_action.NoAction(event, "NoAction")
        elif event["error_code"] == "interface_high_packet_drop":
            remediation = put_under_maintenance.PutUnderMaintenance(event, "PutUnderMaintenance")
        else:
            remediation = default_action_junos.DefaultActionJunos(event, "DefaultActionJunos")
        print(remediation)
    except Exception as e:
        print(e)
        remediation = no_action.NoAction(event, "NoAction")
    return remediation