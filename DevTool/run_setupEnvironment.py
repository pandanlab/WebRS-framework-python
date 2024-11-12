import sys
sys.path.append("./")

import subprocess
import os

def run_comand(line:str):
    subprocess.run(line.strip().split())


run_comand("pip install -r DevTool/store/requirement.txt")

for data in os.listdir("ServiceApp"):
    for file in os.listdir(f"ServiceApp/{data}"):
        if ("requirement.txt" in file):
           run_comand(f"pip install -r ServiceApp/{data}/requirement.txt")