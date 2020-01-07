import event
import jinja2

class FluentdMessage(event.Event):

    def get_device_ID(self):
        return self.message["host"]

    def get_element_name(self):
        return self.message["ident"]

    #for regular syslog,  element_name = event_ID = ident. 
    #for the jitter, event_ID is jitter
    def get_event_ID(self):
         return "syslog"      

    def get_message(self):
        return self.message["message"]

    def get_metric(self):
        return 0


    def generate_output_message(self,output_message_type):
        #j2_env = Environment(loader=PackageLoader("application_events", "templates"))
        templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
        j2_env = jinja2.Environment(loader=templateLoader)
        j2_env.lstrip_blocks = True
        j2_env.trim_blocks = True
        if output_message_type == "appformix":
            payload = j2_env.get_template("appformix_event_payload.j2").render(
                event_ID = self.get_event_ID(),
                metric = self.get_metric(),
                element_name = self.get_element_name(),
                device_ID = self.get_device_ID(),
                message = self.get_message(),
                Application_ID = "fluentd"
            )
        # other output message format can be added
        elif output_message_type == "app2":
            print("to be added")

        return payload


#the FluentdMessageJitter is based on the fix format of syslog that 
#contains the rpm info from rpm-log.slax
#{u'host': u'vmx101', u'ident': u'cscript', u'message': u'RPM_TEST_RESULTS: test-owner=northstar-ifl test-name=ge-0/1/1.0 loss=0 min-rtt=2 max-rtt=41 avgerage-rtt=4.71 jitter=40.495'}
class FluentdMessageJitter(FluentdMessage):

    #return the test name of the rpm
    def get_element_name(self):
        element_name = self.get_message().split(" ")[2].split("=")[1]
        return element_name

    #return the jitter value
    def get_metric(self):
        jitter = self.get_message().split(" ")[7].split("=")[1]
        jitter = float(jitter)
        return jitter
    
    def get_event_ID(self):
        return "syslogJitter"



'''
{u'host': u'vmx101', u'ident': u'pccd', u'message': u"[62175] PCCD received message 'PCEP_MSG_KEEPALIVE' from libpcep"}
{u'host': u'vmx101', u'ident': u'cscript', u'message': u'RPM_TEST_RESULTS: test-owner=northstar-ifl test-name=ge-0/1/1.0 loss=0 min-rtt=2 max-rtt=41 avgerage-rtt=4.71 jitter=40.495'}
['RPM_TEST_RESULTS:', 'test-owner=northstar-ifl', 'test-name=ge-0/1/1.0', 'loss=0', 'min-rtt=53', 'max-rtt=53', 'avgerage-rtt=25', 'jitter=52.558']
'''

class FluentdMessageSNMPTrap(FluentdMessage):
        
    def get_device_ID(self):
        return self.message["tags"]["host"]

    def get_element_name(self):
        return None

    def get_event_ID(self):
        return "SNMPTrap"

    def get_message(self):
    	#neeed to get rid of first and last "
        return self.message["value"][1:-1]

#{u'value': u'"#<SNMP::SNMPv2_Trap:0x00007ff10c4b9b00 @request_id=1231324186, @error_status=0, @error_index=0, @varbind_list=[#<SNMP::VarBind:0x00007ff10c4c5db0 @name=[1.3.6.1.2.1.1.3.0], @value=#<SNMP::TimeTicks:0x00007ff10c4c5e50 @value=669549243>>, #<SNMP::VarBind:0x00007ff10c4c4eb0 @name=[1.3.6.1.6.3.1.1.4.1.0], @value=[1.3.6.1.6.3.1.1.5.3]>, #<SNMP::VarBind:0x00007ff10c4c4460 @name=[1.3.6.1.2.1.2.2.1.1.531], @value=#<SNMP::Integer:0x00007ff10c4c44b0 @value=531>>, #<SNMP::VarBind:0x00007ff10c4bb928 @name=[1.3.6.1.2.1.2.2.1.7.531], @value=#<SNMP::Integer:0x00007ff10c4bba18 @value=2>>, #<SNMP::VarBind:0x00007ff10c4baa78 @name=[1.3.6.1.2.1.2.2.1.8.531], @value=#<SNMP::Integer:0x00007ff10c4baaf0 @value=2>>, #<SNMP::VarBind:0x00007ff10c4b9c40 @name=[1.3.6.1.2.1.31.1.1.1.1.531], @value=\\"ge-0/1/1\\">], @source_ip=\\"10.49.65.133\\">"', u'tags': {u'host': u'10.49.65.133', u'type': u'alert'}}
