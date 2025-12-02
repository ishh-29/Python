'''
Create A Function That Takes An Arbitrary Number Of Arguments Using *args And 
Prints Each Argument.
'''

#Defining Ellipsis Constant
x=...
def printarg(*args):
    for i,j in enumerate(args):
        print(f"Argument->{i+1}:{j}")
    if not args:
        print(f"\nUnspecified Arguments:{x}")

#Main
printarg(1,2,3,"Py")
printarg() #Unspecified Arguments