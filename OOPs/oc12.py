'''
Implement A Decorator To Validate Function Arguments Based On A Given Condition
'''

def validarg(condn):
    def decorator(func):
        def wrap(*args,**kwargs):
            if condn(*args,**kwargs):
                return func(*args,**kwargs)
            else:
                return "Invalid Argument"
        return wrap
    return decorator

@validarg(lambda x:x>0)

def cube(x):
    return x**3

print(cube(3))
print(cube(-2))