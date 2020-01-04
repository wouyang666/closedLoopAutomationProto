import json
from pprint import pprint
import os
from jinja2 import Environment, FileSystemLoader
import datetime
import time
import requests
import action

class PutUnderMaintenance(action.Action):
    """
    def get_link_info_from_ip(interface_ip):
        network_info = get_link()
        for i in network_info.json():
            if "ipv4Address" in i["endA"]:
                if (i['endA']['ipv4Address']['address'] == interface_ip) or (i['endZ']['ipv4Address']['address'] == interface_ip):
                    index_number = i['linkIndex']
        return index_number

    def generate_maitenance_json(index_number, use, maintenance_type):
        #start = 1 for now
        # end = 6000 
        maintenance_type = maintenance_type
        current_time=datetime.datetime.utcnow().strftime("%Y%m%d%H%M")
        if use == 'for_simulation':
            name = 'created_for_simulation'
            start = 3600
            end = 6000
        else:
            name = 'Healthbot-' + maintenance_type + '-health-alert' + current_time
            start = 1
            end = 6000
        THIS_DIR = os.path.dirname(os.path.abspath('__file__'))
        j2_env = Environment(loader=FileSystemLoader(THIS_DIR),
                             trim_blocks=True)

        payload = j2_env.get_template('maintenance.j2').render(
            maintenance_type=maintenance_type,
            index_number=index_number,
            current_time=current_time,
            name=name,
            start_time=getTimeSeqUTC(start),
            end_time=getTimeSeqUTC(end)
        )
        return (payload)
        """

    def run(self):
        """
        rest_index_number = get_link_info_from_ip(source_address)
        rest_payload = generate_maitenance_json(rest_index_number, 'for_maint', 'link')
        print(rest_payload)
        r = create_maintenance(rest_payload)
        return r
        """
        print("action is PutUnderMaintenance")