class Circle:
    def __init__(self, r):
        self.radius = r
    def area(self):
        return 3.141 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.141 * self.radius
NewCircle = Circle(7)
print("Area:", NewCircle.area())
print("Perimeter:", NewCircle.perimeter())
