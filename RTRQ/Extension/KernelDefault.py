import sys
sys.path.append("./")

import os
import importlib

class obj_Kernel:
    def __init__(self):
        None

    def getListRegion(self):
        listRegion = []
        pathNode = os.path.join(os.path.dirname(__file__),"..","Node") 
        for fileNode in os.listdir(pathNode):
            if ".py" in fileNode:
                fileNode = fileNode.strip().replace(".py","")
                listRegion.append(fileNode)
        return listRegion
    
    def getListNode(self,Region):
        Region = importlib.import_module(f"RTRQ.Node.{Region}")
        listNode = []
        vars_Region = vars(Region)
        for name,value in vars_Region.items():
            if("Node" in name) and not "Default" in name:
                listNode.append(name)
        print(listNode)
        return listNode
    
    def get_Node(self,Region,Node):
        Region = importlib.import_module(f"RTRQ.Node.{Region}")
        return getattr((Region),Node).get()
    
    def set_Node(self,Region,Node,value):
        Region = importlib.import_module(f"RTRQ.Node.{Region}")
        getattr((Region),Node).set(value)
    
    def active_Node(self,Region,Node,value=None):
        Region = importlib.import_module(f"RTRQ.Node.{Region}")
        getattr((Region),Node).active(value)
        return getattr((Region),Node).value

    def register_Method(self,Region,Node,method,priority=0):
        Region = importlib.import_module(f"RTRQ.Node.{Region}")
        getattr((Region),Node).add_method(method,priority)

    def unregister_Method(self,Region,Node,name):
        try:
            Region = importlib.import_module(f"RTRQ.Node.{Region}")
            getattr((Region),Node).rm_method(name)
        except:
            None

    def clear_Method(self,Region,Node):
        Region = importlib.import_module(f"RTRQ.Node.{Region}")
        getattr((Region),Node).reset_method()

    def getinfo_node(self,Region,Node):
        Region = importlib.import_module(f"RTRQ.Node.{Region}")
        return getattr((Region),Node).getinfo_methods()    

import RTRQ.Store.store as store
from RTRQ.Extension.MacroDefault import *
kernel = obj_Kernel()
