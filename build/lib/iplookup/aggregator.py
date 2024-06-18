from iplookup.iplocation import lookup_ip as iplocation_lookup
from iplookup.virustotal import lookup_ip as virustotal_lookup

def aggregate_ip_data(ip: str) -> dict:
    data = {}
    
    iplocation_data = iplocation_lookup(ip)
    data['iplocation'] = iplocation_data
    
    virustotal_data = virustotal_lookup(ip)
    data['virustotal'] = virustotal_data
    
    return data
