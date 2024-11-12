import sys
sys.path.append("./")

import os
import shutil

def create_service(data):
    name = f"service_{data}" 
    os.mkdir(f"ServiceApp/{name}")
    with open(f"ServiceApp/{name}/main.py","w") as file:
        file.write("import sys\n")
        file.write("sys.path.append('./')\n")
        file.write("from RTRQ.Extension.Kernel_Default import *\n\n")

    with open(f"ServiceApp/{name}/listNode","w") as file:
        file.write(f"Node_dataExample\n")
        file.write(f"Node_handleExample\n")

    with open(f"ServiceApp/{name}/requirement.txt","w") as file:
        None

def remove_service(data):
    shutil.rmtree(f"ServiceApp/{data}")

def list_service():
    print(os.listdir("ServiceApp"))

if __name__ == "__main__":
    while 1:
        data = input("user : ")
    
        try:
            if("mkdir" in data):
                data = data.replace("mkdir ","")
                for name in data.split():
                    create_service(name)

            elif("rm" in data):
                data = data.replace("rm ","")
                for name in data.split():
                    remove_service(name)

            elif("ls" in data):
                list_service()

            elif("clear" in data):
                # Đối với Windows
                if os.name == 'nt':
                    os.system('cls')
                # Đối với macOS và Linux
                else:
                    os.system('clear')

            elif("exit" in data):
                break
        except:
            None