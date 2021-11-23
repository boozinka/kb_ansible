import re

def parse_ip_arp_dict(arp_string):
    """ Parses output from 'show ip arp' and creates a dictionary of IP/MAC pairings """

    # Initialise varible
    ip_mac_dict = {}

    # Strip whitespace for the string
    arp_string = arp_string.strip()

    # Split the string into lines and interate over the lines
    for line in arp_string.splitlines():
        # Skip over the header
        if re.search(r'^Protocol.*Interface$', line, flags=re.M):
            continue
        ipaddr = line.split()[1]
        mac = line.split()[3]
        ip_mac_dict.update({ipaddr: mac})

    return ip_mac_dict 


class FilterModule(object):
    def filters(self):
        return {"parse_arp_dict": parse_ip_arp_dict}

