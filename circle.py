class Circle:
    def __init__(self, numbers):
        self.num = numbers
    def read_number(self):
        print(self.num)
list = [10, 501, 22, 37, 100, 999, 87, 351]
obj = Circle(list)
obj.read_number()