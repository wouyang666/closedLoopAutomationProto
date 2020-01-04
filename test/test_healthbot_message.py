import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'library'))
import healthbot_message
import jinja2
import json

class TestHealthbotMessage(unittest.TestCase):    
    def setUp(self):
        templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
        j2_env = jinja2.Environment(loader=templateLoader)
        #message_interface_down = {u'group': u'group_all', u'severity': u'major', u'keys': {u'_instance_id': u'["check_interface_status"]', u'interface-name': u'ge-0/0/6', u'_playbook_name': u'check_interface_status'}, u'device-id': u'vMX-5', u'rule': u'check-interface-status', u'topic': u'interface.statistics', u'trigger': u'link-state', u'message': u'ge-0/0/6 link operator status is DOWN'}
        message1 = j2_env.get_template('healthbot_message.j2').render(
            group_name = "group_all",
            severity = "major",
            instance_id = "check_interface_status",
            element_name = "0",
            playbook_name = "check_interface_status",
            device_id = "vMX-2",
            rule = "check-system-cpu-load-average",
            topic = "system.cpu",
            trigger = "cpu-utilization-1min",
            message = "Routing Engine0 1min CPU utilization(99) exceed high threshold(cpu-utilization-1min-high-threshold)"
            )
        #print(message_interface_down)
        message1 = json.loads(message1)
        #print(message_interface_down)
        #message = {u'group': u'group_all', u'severity': u'major', u'keys': {u'slot': u'0', u'_instance_id': u'["device-cpu"]', u'_playbook_name': u'device-cpu'}, u'device-id': u'vMX-2', u'rule': u'check-system-cpu-load-average', u'topic': u'system.cpu', u'trigger': u'cpu-utilization-1min', u'message': u'Routing Engine0 1min CPU utilization(99) exceed high threshold(cpu-utilization-1min-high-threshold)'}
        self.healthtbot_message1 = healthbot_message.HealthbotMessage(message1,'healthbot')

    def test_get_event_ID(self):
        print('test get_event_ID')
        self.assertEqual(self.healthtbot_message1.get_event_ID(), 'cpu-utilization-1min')

    def test_get_device_ID(self):
        print('test get_device_ID')
        self.assertEqual(self.healthtbot_message1.get_device_ID(), 'vMX-2')

    def test_get_severity(self):
        print('test get_event_severity')
        self.assertEqual(self.healthtbot_message1.get_severity(), 'major')

    def test_get_message(self):
        print('test get_message')
        self.assertEqual(self.healthtbot_message1.get_message(), 'Routing Engine0 1min CPU utilization(99) exceed high threshold(cpu-utilization-1min-high-threshold)')

if __name__ == '__main__':
    unittest.main()

