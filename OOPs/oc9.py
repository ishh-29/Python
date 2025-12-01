'''
Create A Decorator To Measure The Execution Time Of A Function
'''

#Importing the module 
import time

def measuret(func):
    def wrap(*args,**kwargs):
        st=time.time()
        res=func(*args,**kwargs)
        end=time.time()
        exetime=end-st
        print(f"Execution time of {func.__name__}: {exetime} seconds")
        return res
    return wrap

@measuret
def mult(x,y):
    return x*y
print(mult(5,6))