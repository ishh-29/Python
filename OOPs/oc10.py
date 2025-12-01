'''
To Create A Decorator To Convert The Return Value Of A Function To A Specified Data Type.
'''

def converttype(dtyp):
    def decorator(func):
        def wrap(*args,**kwargs):
            res=func(*args,**kwargs)
            return dtyp(res)
        return wrap
    return decorator

@converttype(str)

def add(x,y):
    print(x+y)
    return x+y

print(type(add(4,5)))