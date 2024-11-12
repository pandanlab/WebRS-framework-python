import sys
sys.path.append("./")

import os
import glob

#Clear Node
files = glob.glob(os.path.join("RTRQ/Node", '*'))
for file in files:
    if (".py" in file):
        os.remove(file)

#generate node and Store
list_store = []

with open("RTRQ/Extension/.env",'r') as fileEnv:
    for data in fileEnv:
        if("Store" in data):
            data = "system_" + data.replace("Store_","") 
            list_store.append(data)
link_ServiceApp = "ServiceApp"

with open("RTRQ/Extension/MacroDefault.py","w") as fileMacro:
    for serviceName in os.listdir(link_ServiceApp):
        print(serviceName)
        link_service = os.path.join(link_ServiceApp,serviceName)
        region_name = f"Region_{serviceName.replace("service_","")}"
        fileMacro.write(f"{region_name} = '{region_name}'\n")
        for filename in os.listdir(link_service):
            # xu li listNode
            if("listNode" in filename):
                link_listNode = os.path.join(link_service,filename)
                with open(link_listNode,"r") as fileListNode:
                    with open(f"RTRQ/Node/Region_{serviceName.replace("service_","")}.py","w") as fileNode:
                        # add header
                        fileNode.write("import sys\n")
                        fileNode.write("sys.path.append('./')\n")
                        fileNode.write("from RTRQ.Extension.NodeDefault import obj_node\n\n")
                        # add Node
                        for line in fileListNode:
                            if("Node" in line):
                                line = line.strip()
                                fileNode.write(f"{line} = obj_node()\n")
                                fileMacro.write(f"Node_{serviceName.replace("service_","")}_{line.replace("Node_","")} = '{line}'\n")
                            elif("Store" in line):
                                data = f"{serviceName.replace('service_','')}_{line.replace('Store_','')}"
                                list_store.append(data)
        
with open("RTRQ/Store/store.py","w") as fileStore:
    for data in list_store:
        fileStore.write(f"{data} = None\n")

#generate kernelfile
link_ServiceApp = "ServiceApp"
with open("RTRQ/kernel.py","w") as fileKernel:
    fileKernel.write("import sys\n")
    fileKernel.write("sys.path.append('./')\n")
    fileKernel.write("from RTRQ.Extension.KernelDefault import *\n\n")
    fileKernel.write("def kernel_generate():\n")
    for serviceName in os.listdir(link_ServiceApp):
        fileKernel.write(f"\timport ServiceApp.{serviceName}.main\n")