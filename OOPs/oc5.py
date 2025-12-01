'''
Create A Class Shopping Cart With Methods 
To Add,Remove And Calculate Total Price Of Items In The Cart
'''

#Initializing the class for shopping cart
class Cart:
    def __init__(self):
        self.item=[]
    def additem(self,name,qtn):
        self.item.append((name,qtn))
    def removeitem(self,name,qtn):
        for i in self.item:
            if i[0]==name and qtn>0:
                qtn-=1
            elif i[0]==name and qtn==0:
                self.item.remove((name,i[0]))
                break
            else:
                print("Item Not Found")
    def calc_total(self):
        t=0
        for i in self.item:
            t+=i[1]
        return t

#Main
c=Cart()
c.additem("Apple",10)
c.additem("Banana",10)
c.additem("Mango",10)
# Display the current items in the cart
print("Current Items In Cart:")
for i in c.item:
    print(i[0],"-",i[1])
total=c.calc_total()
print("Total Quantity:",total)
        
    