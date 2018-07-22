#!/usr/bin/env python

# Created by un4ckn0wl3z-level99
# Website -> www.un4ckn0wl3z.xyz
# Date -> 7/22/2018

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC Address")
parser.add_option("-m","--mac",dest="new_mac",help="New MAC Address")
(opts,args) = parser.parse_args()

interface = opts.interface
new_mac = opts.new_mac

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether", new_mac])
subprocess.call(["ifconfig",interface,"up"])

print "[+] Changing MAC Address for " + interface + " to " + new_mac







