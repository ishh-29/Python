'''
Create An Instance Of A Specified Class And Display The Namespace Of The Said Instance.
'''

class Student: 
    def __init__(self,stud_id,stud_name,class_name):
        self.stud_id=stud_id
        self.stud_name=stud_name
        self.class_name=class_name 
stud=Student('1', 'A','a')
print(stud.__dict__)
