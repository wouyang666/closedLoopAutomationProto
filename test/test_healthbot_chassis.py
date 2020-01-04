import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'library'))
import healthbot_message_chassis


class TestHealthbotMessageChassis(unittest.TestCase):
    def setUp(self):
        message_cpu_high = {u'group': u'group_all', u'severity': u'major', u'keys': {u'slot': u'0', u'_instance_id': u'["device-cpu"]', u'_playbook_name': u'device-cpu'}, u'device-id': u'vMX-2', u'rule': u'check-system-cpu-load-average', u'topic': u'system.cpu', u'trigger': u'cpu-utilization-1min', u'message': u'Routing Engine0 1min CPU utilization(99) exceed high threshold(cpu-utilization-1min-high-threshold)'}
        self.healthtbot_message_cpu_high_event = healthbot_message_chassis.HealthbotMessageChassis(message_cpu_high,'healthbot')

    def test_get_slot_number(self):
        print('test get_slot_number')
        self.assertEqual(self.healthtbot_message_cpu_high_event.get_slot_number(), '0')

    def test_get_fan_number(self):
        #to be add
        print('test get_fan_number')

    def test_get_pfe_number(self):
        #to be add
        print('test test_get_pfe_number')

    def test_get_fabric_plane(self):
        #to be add
        print('test get_fabric_plane')

if __name__ == '__main__':
    unittest.main()