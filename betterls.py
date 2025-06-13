import os
import json
import platform

usros = platform.system()
files = os.listdir()

config_text = ""

if usros == "Windows":
    if os.path.isfile("C:\\betterls_config.json") == True:
        pass
    elif os.path.isfile("C:\\betterls_config.json") == False:
        configfile = open("C:\\betterls_config.json", "w")
        configfile.close()
elif usros == "Linux":
    if os.path.isfile("~/betterls_config.json") == True:
        pass
    elif os.path.isfile("~/betterls_config.json") == False:
        configfile = open("~/betterls_config.json", "w")
        configfile.close()

for i in files:
    print(i)