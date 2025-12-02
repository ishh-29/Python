'''
Create A Function That Takes A Function As An Argument And 
Calls It With Any Number Of Arguments
'''
def callfunc(func,*args,**kwargs): #Returns the result of calling the function.
    return func(*args,**kwargs)
def add(a,b):
    return a+b
def message(name,text="Good Morning"):
    return f"{name},{text}!"
print(callfunc(add,2,3))
print(callfunc(message,"A",text=...))