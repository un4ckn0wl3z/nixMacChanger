#!/usr/bin/env python

# Created by un4ckn0wl3z-level99
# Website -> www.un4ckn0wl3z.xyz
# Date -> 7/22/2018

import subprocess
import optparse
import re




def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (opts, args) = parser.parse_args()
    if not opts.interface:
        # handle error
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not opts.new_mac:
        # handle error
        parser.error("[-] Please specify an new MAC Address, use --help for more info.")

    return opts

def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print "[+] Changing MAC Address for " + interface + " to " + new_mac

def get_current_mac(interface):
    cmd_result = subprocess.check_output(["ifconfig", interface])
    mac_addr_group = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", cmd_result)

    if mac_addr_group:
        return mac_addr_group.group(0)
    else:
        print "[-] Sorry, could not read MAC Address."


opts = get_args()
current_mac = get_current_mac(opts.interface)
print "Current MAC Address: " + str(current_mac)

change_mac(opts.interface,opts.new_mac)

current_mac = get_current_mac(opts.interface)
if current_mac == opts.new_mac:
    print "[+] MAC Address was successfully changed to " + current_mac
else:
    print "[-] MAC Address did not changed."




