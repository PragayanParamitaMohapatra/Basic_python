class A:
    def __new__(self):
        self.__init__(self)
        print("A's __new__() invoked")