import time
import bring_up_interface, put_under_maintenance, restart_server, default_action_junos

def decide_remidation_action(event):
    print(event["error_code"])
    print("decide action")
    time.sleep(2)
    if event["error_code"] == "interface_down":
        remediation = bring_up_interface.BringUpInterface(event, "BringUpInterface")
    elif event["error_code"] == "server_cpu_100":
        remediation = restart_server.RestartServer(event, "RestartServer")
    elif event["error_code"] == "interface_high_packet_drop":
        remediation = put_under_maintenance.PutUnderMaintenance(event, "PutUnderMaintenance")
    else:
        remediation = default_action_junos.DefaultActionJunos(event, "DefaultActionJunos")
    print(remediation)
    return remediation