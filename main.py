import webview
import Setup.configure as configure
from RTRQ.kernel import *

global window
window = webview.create_window(configure.AppName, configure.EntryPoint)

class Api:
    def __init__(self):
        self.setup_kernel()
        kernel_generate()

    def setup_kernel(self):
        None

    def receiveData(self, data):
        kernel.active_Node(Region_Example2,Node_Example2_handleExample,data)

    def sendData(self,data):
        return data
    
    def changePage(self, data):
        window.load_url(f"Src/View/{data}.html")
        print(window.real_url)
    

    
if __name__ == "__main__":
    api = Api()
    webview.windows[0]._js_api = api
    webview.start()
