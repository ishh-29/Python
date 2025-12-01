'''
Unit Test To Check Whether A Number Is Prime Or Not
'''

#Importing unittest module for test cases

import unittest

def prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

#Test case class inherited from 'unittest.TestCase'.

class testnum(unittest.TestCase):
    def testprime(self):
        p=[2,3,5,7,11,13,17,19,23,29,31]
        print("Prime Numbers:",p)
        for i in p:
            self.assertTrue(prime(i),f"{i} is not recognized as a prime number")
    def testnotprime(self):
        np=[1,4,6,8,9,10,12,14,15,16,18,20]
        print("Non-Prime Numbers:",np)
        for i in np:
            self.assertFalse(prime(i),f"{i} is incorrectly recognized as a prime number")

if __name__=='__main__':
    unittest.main()
