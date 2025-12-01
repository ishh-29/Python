'''
Create a Decorator to Log Function Arguments
'''

def decorator(func):
    #Takes a function as input
    def wrap(*args,**kwargs):
        #arg-> positional arguments (4,5)
        #kwarg-> keyword arguments  (x=4,y=5)
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        #Calling original function and storing the result
        res=func(*args,**kwargs)
        print(f"{func.__name__} returns: {res}")
        return res
    #Returns the inner function that wraps the original function
    return wrap

#Applying the decorator to a function
@decorator
def prod(x,y): #Equivalent Syntax: prod=decorator(prod)
    return x*y

'''
When calling prod,we're actually calling wrap
'''

res=prod(4,5)
print(res)

