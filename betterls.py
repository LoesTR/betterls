import os
import json
import platform

usros = platform.system()
files = os.listdir()

config_text = ""
config_header = ""

def checkconferrors():
    config_text_flnm = config_text.count("{flnm}")
    config_text_size = config_text.count("{size}")
    config_header_path = config_header.count("{path}")
    if config_text_flnm != 1:
        exit("Config Error! {flnm} must be in the config once")
    if config_text_size > 1:
        exit("Config Error! {size} must be in the config once")
    if config_header_path > 1:
        exit("Config Error! {path} must be in the config once")

def betterlsconfig(filename: str):
    global config_text
    config_text = config_text.replace("{flnm}", filename)
    print(config_text)

if usros == "Windows":
    if os.path.isfile("C:\\betterls\\betterls_config.json") == True:
        configfile = open("C:\\betterls\\betterls_config.json", "r")
        jsondata = json.loads(configfile.read())
        config_text = jsondata["lstext"]
        config_header = jsondata["header"]
        configfile.close()
        checkconferrors()
        if(config_header != ""):
            headeroutput = config_header.replace("{path}", os.getcwd())
            print(headeroutput + "\n")
        for i in files:
            output = config_text.replace("{flnm}", i)
            output = output.replace("{size}", str(os.path.getsize(i)))
            print(output)
    elif os.path.isfile("C:\\betterls\\betterls_config.json") == False:
        os.mkdir("C:\\betterls")
        configfile = open("C:\\betterls\\betterls_config.json", "w")
        emptyconf = {"lstext": "{flnm}", "header": ""}
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
        if config_header != "":
            headeroutput = config_header.replace("{path}", os.getcwd())
            print(headeroutput + "\n\n")
        for i in files:
            output = config_text.replace("{flnm}", i)
            output = output.replace("{size}", i)
            print(output)
    elif os.path.isfile("~/betterls_config.json") == False:
        configfile = open("~/betterls_config.json", "w")
        emptyconf = {"lstext": "{flnm}", "header": ""}
        configfile.write(json.dumps(emptyconf))
        configfile.close()
        for i in files:
            print(i)