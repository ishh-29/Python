'''
Unit Test To Check If A List Is Sorted n Ascending Order
'''

import unittest as ut

def sortl(l):
    return all(l[i]<=l[i+1] for i in range(len(l)-1))

class testsort(ut.TestCase):
    def sorted(self):
        l=[1,2,4,5,7,9,11,12,13,14]
        print("Sorted List:",l)
        self.assertTrue(sortl(l),"The list is not sorted in ascending order")
    
    def unsortedl(self):
        l=[1,3,5,4,6,2,3]
        print("Unsorted List:",l)
        self.assertFalse(sortl(l),"The list is sorted in ascending order")

if __name__=="__main__":
    ut.main()