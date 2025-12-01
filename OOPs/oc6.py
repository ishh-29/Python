'''
Implement A Linked List And Its Basic Operations 
'''
#Creating a node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#Creating class Linked List
class LinkedList:
    def __init__(self):
        self.head=None
    def display(self):
        curr=self.head
        while curr:
            print(curr.data,end='->')
            curr=curr.next
        print()
    def insert(self,data):
        n=Node(data)
        if not self.head:
            self.head=n
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=n
    def delete(self,key):
        if self.head==None:
            return 
        curr=self.head
        prev=None
        while curr and curr.data!=key:
            prev=curr
            curr=curr.next
        if curr:
            prev.next=curr.next
#Main
l=LinkedList()
for i in range(10,111,10):
    l.insert(i)
print("Linked List after insertion:")
l.display()
l.delete(110)
print("Linked List after deletion of 110:")
l.display()