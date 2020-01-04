from jnpr.junos.device import Device
from jnpr.junos.utils.config import Config
from lxml import etree
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path


userid = "northstar"
password = "Embe1mpls"

class Action:
    def __init__(self, event, name):
        self.event = event
        self.name = name

    def config_junos(self, data, device, format):
        print("connecting to " + device)
        try:
            dev = Device(host=device, user=userid, password=password, normalize=True)
            dev.open()
            cu = Config(dev)
            data = data
            print(data)
            cu.load(data, format=format)
            cu.commit()
            dev.close()
            result = "succesful"
        except Exception as e:
            print(e)
            result = "failed"
            print(result) 
        return result

    def get_junos_version(self, device):
        try:
            with Device(host=device, user=userid, password=password) as dev:
                sw_info_text = dev.rpc.get_software_information({'format':'text'})
                result = etree.tostring(sw_info_text, encoding='unicode')
                print(result)
        except Exception as e:
            result = e
            print(result)
        return result

    def get_junos_config(self, device):
        try:
            with Device(host=device, user=userid, password=password) as dev:
                device_config = dev.rpc.get_config(options={'format':'text'})
                result = etree.tostring(device_config, encoding='unicode')
                #print(result)
        except Exception as e:
            result = e
            print(result)
        return result

    def email_result(self, receiver, subject, message, files):
        sender = 'event_service'
        receiver = receiver
        subject = subject
        message = message
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        for f in files:
            filename = os.path.basename(f)
            attachment = open(f, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(part)
        text = msg.as_string()
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receiver, msg.as_string())
