class x:
    def __init__(self):
        
        self._name = 1
        self.age = 2
        self.__private = 3
        
    def display(self):
        # self._name = 2
        # self.age = 5
        # self.__private = 3
        print(f"Name: {self._name}, Age: {self.age} and Private: {self.__private}")
        
        
class y(x):
    def __init__(self):
        super().__init__()
        self._name = 4
        self.age = 5
        self.__private = 6

   
obj= y()
obj.display()  