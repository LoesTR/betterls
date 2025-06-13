import os
import json
import platform

usros = platform.system()
files = os.listdir()

config_text = ""

if usros == "Windows":
    if os.path.isfile("C:\\betterls_config.json") == True:
        configfile = open("C:\\betterls_config.json", "w")
        jsondata = json.loads(configfile.read)
        config_text = jsondata["text"]
        configfile.close()
        for i in files:
            print(config_text)
    elif os.path.isfile("C:\\betterls_config.json") == False:
        configfile = open("C:\\betterls_config.json", "w")
        configfile.close()
        for i in files:
            print(i)
elif usros == "Linux":
    if os.path.isfile("~/betterls_config.json") == True:
        configfile = open("C:\\betterls_config.json", "w")
        jsondata = json.loads(configfile.read)
        config_text = jsondata["text"]
        configfile.close()
        for i in files:
            print(config_text)
    elif os.path.isfile("~/betterls_config.json") == False:
        configfile = open("~/betterls_config.json", "w")
        configfile.close()
        for i in files:
            print(i)