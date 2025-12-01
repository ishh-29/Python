'''
Create A Person Class And Include Attributes Like 
Name,Country And Date Of Birth
Implement A Method To Determine Person's Age
'''

#Importing datetime module
from datetime import date

class Person:
    #Initializiing an object Person with necessary attributes
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    
    #To calculate age 
    def calcage(self):
        curr=date.today()
        age=curr.year-self.dob.year
        if curr<date(curr.year,self.dob.month,self.dob.day):
            print("Invalid")
            age=-1
        return age

#Main
p1=Person("A","C1",date(2000,5,15))
p2=Person("B","C2",date(1995,10,20))
p3=Person("C","C3",date(2025,1,1))

print(f"{p1.name} from {p1.country} is {p1.calcage()} years old.")
print(f"{p2.name} from {p2.country} is {p2.calcage()} years old.")
print(f"{p3.name} from {p3.country} is {p3.calcage()} years old.")