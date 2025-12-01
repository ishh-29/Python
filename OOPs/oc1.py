#Create A Class Circle And Calculate Area And Circumference

#Importing math module
import math

#Definfing class Circle
class Circle:
    #Initializing Circle object with a radius
    def __init__(self,radius):
        self.radius=radius
    #Calculating area 
    def area(self):
        return math.pi(self.radius**2)
    #Calculating circumference
    def circumference(self):
        return 2*math.pi*self.radius
    
#Main 

rad=float(input("Enter Radius Of Cirlce:"))
c=Circle(rad)
print("Area Of Circle:",c.area())
print("Circumference Of Circle:",c.circumference())

