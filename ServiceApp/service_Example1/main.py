import sys
sys.path.append('./')
from RTRQ.Extension.KernelDefault import *

def hello(data = None):
    print("example1")

kernel.register_Method(Region_Example1,Node_Example1_handleExample,hello)