class Point:    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:    
    def __init__(self, p, r):        
        self.x = p.x
        self.y = p.y
        self.r = r
    def get_area(self):
        return 3.14 * self.r ** 2

    def get_perimeter(self):
        return 3.14 * 2 * self.r

    def get_center(self):
        return (self.x , self.y)

    def print(self):
        print(f'Circle: ({self.x}, {self.y}), r: {self.r}')

pl = Point(0, 0)
c1 = Circle(pl, 3)
print(c1.get_area())
print(c1.get_perimeter())
print(c1.get_center())
c1.print()
p2 = Point(4, 5)
c2 = Circle(p2, 1)
print(c2.get_area())
print(c2.get_perimeter())
print(c2.get_center())
c2.print()