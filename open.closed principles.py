class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
            return self.length **2
class Circule(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
            return 3.14* (self.radius**2)
class Triangle(Shape):
    def __init__(self,base,hight):
        self.base=base
        self.hight=hight
    def area(self):
            return 0.5 *self.base*self.hight


square=Square(4)
circule=Circule(2)
triangle=Triangle(4,8)

print("Area of Square:", square.area()) 
print("Area of Circule:", circule.area())  
print("Area of Triangle:", triangle.area())