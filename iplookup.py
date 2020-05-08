#!/usr/bin/env python3

import sys
from ipwhois import IPWhois
from pprint import pprint

def getAddressInfo(address, type=None):
    if address is None:
        raise Exception("Invalid address...")

    ip = IPWhois(address)
    res = None

    if (type == None or type == "whois"):
        res = ip.lookup_whois()
    elif type == "rdap":
        res = ip.lookup_rdap()
    
    pprint(res)

getAddressInfo(sys.argv[1], sys.argv[2])