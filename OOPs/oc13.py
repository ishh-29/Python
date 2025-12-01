'''
Import A Built-In Array Module And Display The Namespace Of The Said Module
'''

#Importing the module
import array

for i in array.__dict__:
    print(i)