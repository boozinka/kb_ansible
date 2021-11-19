import re

def parse_ip_arp(arp_string):
    """ Parses output from 'show ip arp' and extracts the mac-addresses """

    # Initialise varible
    arp_addrs = []

    # Strip whitespace for the string
    arp_string = arp_string.strip()

    # Split the string into lines and interate over the lines
    for line in arp_string.splitlines():
        # Skip over the header
        if re.search(r'^Address.*Interface$', line, flags=re.M):
            continue
        mac = line.split()[2]
        arp_addrs.append(mac)

    return arp_addrs


class FilterModule(object):
    def filters(self):
        return {"parse_arp": parse_ip_arp}
