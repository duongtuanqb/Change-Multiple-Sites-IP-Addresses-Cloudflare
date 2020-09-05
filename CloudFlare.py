import requests
import simplejson
from define import DOMAINS, BASE_URL, CURRENT_IP, NEW_IP, HEADERS


class CloudFlare:
    def __init__(self):
        self.domains = DOMAINS

    def get_zone_ids(self):
        url = BASE_URL + "/zones"

        loop = True
        page = 1
        while loop:
            params = {
                'status': 'active',
                'page': page
            }

            response = requests.request("GET", url, headers=HEADERS, params=params)
            json = response.json()
            if response.status_code != 200:
                print(json)
                return

            if len(response.json()['result']):
                for zone in response.json()['result']:
                    if zone['name'] in self.domains:
                        yield zone['id']
            else:
                loop = False

            page += 1

    def get_dns_record_ids(self, zone_id):
        url = f'{BASE_URL}/zones/{zone_id}/dns_records'

        params = {
            'type': 'A',
            'content': CURRENT_IP
        }

        response = requests.request("GET", url, headers=HEADERS, params=params)
        json = response.json()
        if response.status_code != 200:
            print(json)
            return

        if not json['success']:
            print(json['errors'])
        else:
            for dns_record in json['result']:
                yield dns_record['id'], dns_record['name']

    def update_new_ip_for_dns_record(self, zone_id, dns_record_id, dns_record_name):
        url = f'{BASE_URL}/zones/{zone_id}/dns_records/{dns_record_id}'

        payload = {
            "type": "A",
            "content": NEW_IP,
            "name": dns_record_name
        }

        response = requests.request("PUT", url, headers=HEADERS, data=simplejson.dumps(payload))

        json = response.json()
        if response.status_code != 200:
            print(json)
            return

        if json['success']:
            print(
                f'Updated success domain {json["result"]["zone_name"]}: value {json["result"]["name"]}, type {json["result"]["type"]}, '
                f'content {json["result"]["content"]}')
        else:
            print(f'Updated error domain {json["result"]["zone_name"]}: {json["messages"]}')
