'''
Unit Test To Check If A String Is Palindrome
'''

import unittest as ut

def palindrome(s):
    return s==s[::-1]

class testpal(ut.TestCase):
    def pal(self):
        s="racecar"
        print("Palindrome String:",s)
        self.assertTrue(palindrome(s),"The string is not a palindrome")
    def notpal(self):
        s="hello"
        print("Non-Palindrome String:",s)
        self.assertFalse(palindrome(s),"The string is a palindrome")

if __name__=="__main__":
    ut.main()