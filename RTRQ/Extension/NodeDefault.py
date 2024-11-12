class obj_node:
    def __init__(self) -> None:
        self.value = None
        self.list_Method = []
        self.list_idMethod = []
        self.list_valuePriority = []
        self.list_indexPriority = []

    def set(self,data):
        self.value = data

    def get(self):
        return self.value
    
    def active(self,data=None):
        self.value = data
        list_value = []
        for index in self.list_indexPriority:
            self.list_Method[index](data)
            list_value.append(self.value)
        self.value = list_value
        return self.value

    def reset_method(self):
        self.list_Method = []
        self.list_idMethod = []
        self.list_valuePriority = []
        self.list_indexPriority = []

    def generate_priority(self):
        self.list_indexPriority = sorted(range(len(self.list_valuePriority)), key=lambda i: self.list_valuePriority[i], reverse=True)

    def add_method(self,method,priority=0):
        self.list_Method.append(method)
        self.list_idMethod.append(method.__name__)
        self.list_valuePriority.append(priority)
        self.generate_priority()

    def rm_method(self,name):
        index = self.list_idMethod.index(name)
        self.list_idMethod.pop(index)
        self.list_Method.pop(index)
        self.list_valuePriority.pop(index)
        self.generate_priority()

    def getinfo_methods(self):
        list_info = []
        for index,value in enumerate(self.list_Method):
            id_method = id(value)
            name = value.__name__
            priority = self.list_valuePriority[index]
            execution_index = self.list_indexPriority.index(index)
            info = [index,hex(id_method),name,priority,execution_index+1]
            list_info.append(info)
        return list_info
    