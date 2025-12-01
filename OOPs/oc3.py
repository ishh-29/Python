#Create a class for basic arithmetic operations

class Calc:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def prod(self,x,y):
        return x*y
    def div(self,x,y):
        if y==0:
            return "Undefined"
        return x/y
    
#Main
c=Calc()
print("Addition:",c.add(10,5))
print("Subtraction:",c.sub(10,5))
print("Product:",c.prod(10,5))
print("Division:",c.div(10,0))