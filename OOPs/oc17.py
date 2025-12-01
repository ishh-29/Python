'''
Create A Class To Convert Decimal Number To A Roman Numeral
'''

class dectorom:
    def to_rom(self,num):
        val=[1000,900,500,400,100,
             90,50,40,10,9,5,4,1]
        mark=["M","CM","D","CD","C",
            "XC","L","XL","X","IX","V",
            "IV","I"]
        roman=''
        i=0
        while  num > 0:
            for j in range(num//val[i]):
                roman+=mark[i]
                num-=val[i]
            i+=1
        return roman
    
n=int(input("Enter A Number:"))
print(dectorom().to_rom(n))