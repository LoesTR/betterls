import os
import json
import platform

usros = platform.system()
files = os.listdir()

for i in files:
    print(i)