'''
Implement A Decorator To Cache The Result Of A Function
'''

def cacheres(func):
    cache={}
    def wrap(*args,**kwargs):
        key=(*args,*kwargs.items())
        if key in cache:
            print("Retrieving result from cache...")
            return cache[key]
        res=func(*args,**kwargs)
        cache[key]=res
        return res
    return wrap

@cacheres

def mult(x,y):
    print("Calculating product...")
    return x*y

print(mult(4,5))
print(mult(4,5))