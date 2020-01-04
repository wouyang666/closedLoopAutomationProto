import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'library'))
import fluentd_message
import jinja2
import json

class TestFluentdMessage(unittest.TestCase):
    def setUp(self):
        templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
        j2_env = jinja2.Environment(loader=templateLoader)
        message1 = j2_env.get_template('fluentd_message.j2').render(
            host = "vmx101",
            ident = "mgd",
            pid = "37304",
            message = "UI_LOGIN_EVENT: User 'root' login, class 'super-user' [37304], ssh-connection '', client-mode 'junoscript'"
            )
        message1 = json.loads(message1)
        self.fluentd_message1 = fluentd_message.FluentdMessage(message1,"fluentd")

    def test_get_device_ID(self):
        print("test get_device_ID")
        self.assertEqual(self.fluentd_message1.get_device_ID(), "vmx101")

    def test_get_element_name(self):
        print("test get_element_name")
        self.assertEqual(self.fluentd_message1.get_element_name(), "mgd")

    def test_get_event_ID(self):
        print("test get_event_ID")
        self.assertEqual(self.fluentd_message1.get_event_ID(), "syslog")

    def test_get_message(self):
        print("test get_message")
        self.assertEqual(self.fluentd_message1.get_message(), "UI_LOGIN_EVENT: User 'root' login, class 'super-user' [37304], ssh-connection '', client-mode 'junoscript'")

    def test_get_metric(self):
        print("test get_metric")
        self.assertEqual(self.fluentd_message1.get_metric(), 0)

class TestFluentdMessageJitter(unittest.TestCase):
    def setUp(self):
        templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
        j2_env = jinja2.Environment(loader=templateLoader)
        message1 = j2_env.get_template('fluentd_message.j2').render(
            host = "vmx101",
            ident = "cscript",
            message = "RPM_TEST_RESULTS: test-owner=northstar-ifl test-name=ge-0/0/6.0 loss=0 min-rtt=3 max-rtt=38 avgerage-rtt=8.83 jitter=46.599"
            )
        #print(message1)
        message1 = json.loads(message1)
        self.fluentdJitter_message1 = fluentd_message.FluentdMessageJitter(message1,"fluentd")

    def test_get_element_name(self):
        print("fluentdJitter test get_element_name")
        self.assertEqual(self.fluentdJitter_message1.get_element_name(), "ge-0/0/6.0")

    def test_get_metric(self):
        print("fluentdJitter test get_metric")
        self.assertEqual(self.fluentdJitter_message1.get_metric(), 46.599)

    def test_get_event_ID(self):
        print("fluentdJitter test get_event_ID")
        self.assertEqual(self.fluentdJitter_message1.get_event_ID(), "syslogJitter") 

class TestFluentdMessageSNMPTrap(unittest.TestCase):
    def setUp(self):
        templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
        j2_env = jinja2.Environment(loader=templateLoader)
        message1 = j2_env.get_template('fluentd_SNMPTrap.j2').render(
            value = '#<SNMP::SNMPv2_Trap:0x00007ff10c4b9b00 @request_id=1231324186, @error_status=0, @error_index=0, @varbind_list=[#<SNMP::VarBind:0x00007ff10c4c5db0 @name=[1.3.6.1.2.1.1.3.0], @value=#<SNMP::TimeTicks:0x00007ff10c4c5e50 @value=669549243>>, #<SNMP::VarBind:0x00007ff10c4c4eb0 @name=[1.3.6.1.6.3.1.1.4.1.0], @value=[1.3.6.1.6.3.1.1.5.3]>, #<SNMP::VarBind:0x00007ff10c4c4460 @name=[1.3.6.1.2.1.2.2.1.1.531], @value=#<SNMP::Integer:0x00007ff10c4c44b0 @value=531>>, #<SNMP::VarBind:0x00007ff10c4bb928 @name=[1.3.6.1.2.1.2.2.1.7.531], @value=#<SNMP::Integer:0x00007ff10c4bba18 @value=2>>, #<SNMP::VarBind:0x00007ff10c4baa78 @name=[1.3.6.1.2.1.2.2.1.8.531], @value=#<SNMP::Integer:0x00007ff10c4baaf0 @value=2>>, #<SNMP::VarBind:0x00007ff10c4b9c40 @name=[1.3.6.1.2.1.31.1.1.1.1.531], @value=\\"ge-0/1/1\\">], @source_ip=\\"10.49.65.133\\">',
            host = "10.49.65.133",
            type = "alert"
            )
        #print(message1)
        message1 = json.loads(message1)
        self.fluentdSNMPTrap_message1 = fluentd_message.FluentdMessageSNMPTrap(message1,"fluentd")

    def test_get_device_ID(self):
        print("fluentd_SNMPTrap test get_device_ID")
        self.assertEqual(self.fluentdSNMPTrap_message1.get_device_ID(), "10.49.65.133")

    def test_get_element_name(self):
        print("fluentd_SNMPTrap test get_element_name")
        self.assertEqual(self.fluentdSNMPTrap_message1.get_element_name(), None)

    def test_get_event_ID(self):
        print("fluentd_SNMPTrap test get_event_ID")
        self.assertEqual(self.fluentdSNMPTrap_message1.get_event_ID(), "SNMPTrap")

    def test_get_message(self):
        print("fluentd_SNMPTrap test get_message")
        self.assertEqual(self.fluentdSNMPTrap_message1.get_message(), '<SNMP::SNMPv2_Trap:0x00007ff10c4b9b00 @request_id=1231324186, @error_status=0, @error_index=0, @varbind_list=[#<SNMP::VarBind:0x00007ff10c4c5db0 @name=[1.3.6.1.2.1.1.3.0], @value=#<SNMP::TimeTicks:0x00007ff10c4c5e50 @value=669549243>>, #<SNMP::VarBind:0x00007ff10c4c4eb0 @name=[1.3.6.1.6.3.1.1.4.1.0], @value=[1.3.6.1.6.3.1.1.5.3]>, #<SNMP::VarBind:0x00007ff10c4c4460 @name=[1.3.6.1.2.1.2.2.1.1.531], @value=#<SNMP::Integer:0x00007ff10c4c44b0 @value=531>>, #<SNMP::VarBind:0x00007ff10c4bb928 @name=[1.3.6.1.2.1.2.2.1.7.531], @value=#<SNMP::Integer:0x00007ff10c4bba18 @value=2>>, #<SNMP::VarBind:0x00007ff10c4baa78 @name=[1.3.6.1.2.1.2.2.1.8.531], @value=#<SNMP::Integer:0x00007ff10c4baaf0 @value=2>>, #<SNMP::VarBind:0x00007ff10c4b9c40 @name=[1.3.6.1.2.1.31.1.1.1.1.531], @value="ge-0/1/1">], @source_ip="10.49.65.133"')


if __name__ == '__main__':
    unittest.main()