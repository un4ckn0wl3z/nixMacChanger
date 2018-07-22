# Created by un4ckn0wl3z-level99
# Website -> www.un4ckn0wl3z.xyz
# Date -> 7/22/2018

import re

cmd_result = """
eth0      Link encap:Ethernet  HWaddr 88:d7:f6:72:f0:c1
          inet addr:10.2.124.151  Bcast:10.2.124.255  Mask:255.255.255.0
          inet6 addr: fe80::a00f:fa82:8319:f7d/64 Scope:Global
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
"""
mac_addr_group = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", cmd_result)
print mac_addr_group.group(0)