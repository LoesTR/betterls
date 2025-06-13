import os
import json
import platform

usros = platform.system()
files = os.listdir()

config_text = ""

def checkconferrors():
    config_text_flnm = config_text.count("{flnm}")
    if config_text_flnm != 1:
        exit("Config Error! {flnm} must be in the config once")

def betterlsconfig():
    pass

if usros == "Windows":
    if os.path.isfile("C:\\betterls\\betterls_config.json") == True:
        configfile = open("C:\\betterls\\betterls_config.json", "r")
        jsondata = json.loads(configfile.read())
        config_text = jsondata["lstext"]
        configfile.close()
        checkconferrors()
        for i in files:
            print(config_text)
    elif os.path.isfile("C:\\betterls\\betterls_config.json") == False:
        os.mkdir("C:\\betterls")
        configfile = open("C:\\betterls\\betterls_config.json", "w")
        emptyconf = {"lstext": "{flnm}"}
        configfile.write(json.dumps(emptyconf))
        configfile.close()
        for i in files:
            print(i)
elif usros == "Linux":
    if os.path.isfile("~/betterls_config.json") == True:
        configfile = open("~/betterls_config.json", "r")
        jsondata = json.loads(configfile.read())
        config_text = jsondata["lstext"]
        configfile.close()
        checkconferrors()
        for i in files:
            print(config_text)
    elif os.path.isfile("~/betterls_config.json") == False:
        configfile = open("~/betterls_config.json", "w")
        emptyconf = {"lstext": "{flnm}"}
        configfile.write(json.dumps(emptyconf))
        configfile.close()
        for i in files:
            print(i)