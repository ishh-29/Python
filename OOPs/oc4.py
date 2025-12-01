'''
Create A Class For Shapes And Different Subclasses 
For Different Shapes And Calculate Their Area And Perimeter
'''

#Importing math module
import math

#Parent Class for defining general shapes
class Shape:
    def area(self): pass
    def perimeter(self): pass

#Child Class for specific shape
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.lenght=length
        self.breadth=breadth
    def area(self):
        return self.lenght*self.breadth
    def perimeter(self):
        return 2*(self.lenght+self.breadth)
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
    def perimeter(self):
        return 4*self.side
class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def area(self):
        s=(self.side1+self.side2+self.side3)/2
        return math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3))
    def perimeter(self):
        return self.side1+self.side2+self.side3

#Main
#Creating objects of different shapes
circle=Circle(5)
rectangle=Rectangle(4,6)
square=Square(4)
triangle=Triangle(3,4,5)

#Calculating area and perimeter of different shapes
print("Circle:Area=",circle.area(),"Perimeter=",circle.perimeter())
print("Rectangle:Area=",rectangle.area(),"Perimeter=",rectangle.perimeter())
print("Square:Area=",square.area(),"Perimeter=",square.perimeter())
print("Triangle:Area=",triangle.area(),"Perimeter=",triangle.perimeter())