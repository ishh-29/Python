'''
Unit Test To Checks If A Function Handles Floating-point Calculations Accurately.
'''

import unittest as ut

class testfloat(ut.TestCase):
    def test_addition(self):
        a=0.1
        b=0.2
        res=a+b
        print(f"Testing Addition: {a}+{b}={res}")
        self.assertAlmostEqual(res,0.3,places=7)
    def test_subtraction(self):
        a=0.3
        b=0.1
        res=a-b
        print(f"Testing Subtraction: {a}-{b}={res}")
        self.assertAlmostEqual(res,0.2,places=7)
    def test_multiplication(self):
        a=0.1
        b=0.2
        res=a*b
        print(f"Testing Multiplication: {a}*{b}={res}")
        self.assertAlmostEqual(res,0.02,places=7)
    def test_division(self):
        a=0.3
        b=0.1
        result=a/b
        print(f"Testing Division:{a}/{b}={result}")
        self.assertAlmostEqual(result,3.0,places=7)

if __name__=="__main__":
    ut.main()