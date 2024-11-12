import json
import os
import sys

sys.path.append("./")

with open(os.path.join(os.path.dirname(__file__),"configure.json"), 'r') as file:
    data = json.load(file)

AppName    = data["AppName"]
EntryPoint = data["EntryPoint"]