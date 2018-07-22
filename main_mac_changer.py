#!/usr/bin/env python

# Created by un4ckn0wl3z-level99
# Website -> www.un4ckn0wl3z.xyz
# Date -> 7/22/2018

import subprocess

interface = raw_input("interface> ")
new_mac = raw_input("new MAC> ")

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether", new_mac])
subprocess.call(["ifconfig",interface,"up"])

print "[+] Changing MAC Address for " + interface + " to " + new_mac







