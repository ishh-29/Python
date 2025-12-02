'''
Create A Function That Takes A Multidimensional Array And 
Slices The First Two Elements From The Third Dimension.
'''

#Importing numpy for multidimensional array handling
import numpy as np

def slice3d(arr):
    return arr[...,:2] #Slicing 1st two elements form 3rd dimension

#Creating a 3D array
nums=np.array([[[1,2,3],[4,5,6]],
            [[7,8, 9],[10,11,12]],
            [[13,14,15],[16,17,18]]])
print("Sliced Array:",slice3d(nums))