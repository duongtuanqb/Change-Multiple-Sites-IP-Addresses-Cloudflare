from CloudFlare import CloudFlare

if __name__ == '__main__':
    cloudFlare = CloudFlare()
    for zone_id in cloudFlare.get_zone_ids():
        for dns_record_id, dns_record_name in cloudFlare.get_dns_record_ids(zone_id):
            cloudFlare.update_new_ip_for_dns_record(zone_id, dns_record_id, dns_record_name)