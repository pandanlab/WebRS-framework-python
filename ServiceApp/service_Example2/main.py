import sys
sys.path.append('./')
from RTRQ.Extension.KernelDefault import *


def hello(data):
    print(f"example2 : {data}")

kernel.register_Method(Region_Example2,Node_Example2_handleExample,hello)