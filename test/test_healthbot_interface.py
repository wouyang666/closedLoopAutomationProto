import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'library'))
import healthbot_message_interface
import jinja2
import json

class TestHealthbotMessageInterface(unittest.TestCase):
    def setUp(self):
        templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
        j2_env = jinja2.Environment(loader=templateLoader)
        #message_interface_down = {u'group': u'group_all', u'severity': u'major', u'keys': {u'_instance_id': u'["check_interface_status"]', u'interface-name': u'ge-0/0/6', u'_playbook_name': u'check_interface_status'}, u'device-id': u'vMX-5', u'rule': u'check-interface-status', u'topic': u'interface.statistics', u'trigger': u'link-state', u'message': u'ge-0/0/6 link operator status is DOWN'}
        message_interface_down = j2_env.get_template('healthbot_message.j2').render(
            group_name = "group_all",
            severity = "major",
            instance_id = "check_interface_status",
            element_name = "ge-0/0/6",
            playbook_name = "check_interface_status",
            device_id = "vMX-5",
            rule = "check-interface-status",
            topic = "interface.statistics",
            trigger = "link-state",
            message = "ge-0/0/6 link operator status is DOWN"
            )
        message_delay_exceed = j2_env.get_template('healthbot_message.j2').render(
            group_name = "group_all",
            severity = "major",
            instance_id = "rpm-all",
            element_name = "ge-0/0/0.0",
            playbook_name = "playbook-rpm",
            device_id = "vMX-7",
            rule = "rpm",
            topic = "interface.rpm",
            trigger = "delay-exceed",
            message = "Rtt over threshold"
            )
        #print(message_interface_down)
        message_interface_down = json.loads(message_interface_down)
        message_delay_exceed = json.loads(message_delay_exceed)
        #print(message_interface_down)
        self.healthtbot_message_interface_down = healthbot_message_interface.HealthbotMessageInterface(message_interface_down,'healthbot')
        self.healthtbot_message_delay_exceed = healthbot_message_interface.HealthbotMessageInterface(message_delay_exceed,'healthbot')

    def test_get_interface_name(self):
        print('test get_interface_name')
        self.assertEqual(self.healthtbot_message_interface_down.get_interface_name(), 'ge-0/0/6')
        self.assertEqual(self.healthtbot_message_delay_exceed.get_interface_name(), 'ge-0/0/0.0')

if __name__ == '__main__':
    unittest.main()