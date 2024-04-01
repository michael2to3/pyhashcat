#!/usr/bin/env python

from pyhashcat import Hashcat

print("-------------------------------")
print("---- Hashcat devices info  ----")
print("-------------------------------")

hc = Hashcat()
print("[!] Hashcat object init with id: ", id(hc))

hc.backend_info = True
hc.no_threading = True
hc.quiet = True
rc = hc.hashcat_session_init()
print(hc.get_backend_devices_info())
