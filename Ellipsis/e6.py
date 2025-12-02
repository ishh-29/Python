'''
Create A Custom Class With An 'init' Method.
Use 'Ellipsis' To Indicate That Some Attributes May Be Added Dynamically.
'''
class Class:
    def __init__(self,attr1,attr2,attr3,attr4=...):
        self.attr1=attr1
        self.attr2=attr2
        self.attr3=attr3
        self.attr4=attr4
    def setattr(self,val):
        self.attr4=val
obj=Class("A","B","C")
print(obj.attr1)
print(obj.attr2)
print(obj.attr3)
print(obj.attr4)
obj.setattr("D")
print(obj.attr4)