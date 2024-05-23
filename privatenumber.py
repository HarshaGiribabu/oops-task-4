class myClass:
    __num = 45

    def __privMeth(self):
        print("I'm inside class myClass")

    def hello(self):
        print("Private Variable value:", self.__num)

pov = myClass()
pov.hello()
