'''
Create A Class Named Student With Attributes Like Name And Marks.
Add A New Attribute Grade , Display The Entire Attribute And The Values Of The Class.
Now Remove The Name Attribute And Display The Entire Attribute With Values.
'''
class Student:
    name='A'
    marks=90

print("Original Attributes And Their Values Of The Student Class:")

for i,j in Student.__dict__.items():
    if not i.startswith('_'):
        print(f'{i}->{j}')

print("\nAfter Removing The name,attributes And Their Values From The Said Class:")

del Student.name
for i,j in Student.__dict__.items():
    if not i.startswith('_'):
        print(f'{i}->{j}')