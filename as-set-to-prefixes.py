#!/usr/bin/env python
from netaddr import IPNetwork, cidr_merge
import pythonwhois
import requests
import re
import sys
import json

whois_raw = pythonwhois.net.get_whois_raw(
    sys.argv[1], server='whois.radb.net')

asns = set()
prefixes = set()

for line in whois_raw[0].splitlines():
    if line.startswith('members'):
        asns.add(re.split(r'\W+', line)[-1].strip('AS'))

for asn in asns:
    # TODO: Set the `sourceapp` param https://stat.ripe.net/docs/data_api
    r = requests.get('https://stat.ripe.net/data/ris-prefixes/data.json?resource={}&list_prefixes=true'.format(asn))  # noqa
    j = r.json()
    try:
        for v in j['data']['prefixes']:
            for t in j['data']['prefixes'][v]:
                for cidr in j['data']['prefixes'][v][t]:
                    prefixes.add(IPNetwork(cidr.strip()))
    except KeyError:
        pass

for cidr in cidr_merge(prefixes):
    print(cidr)
