from array import *
"""maximum"""
arr = array('i',[2,3,4,55,6,77])
max = arr[0]
for i in range(1,len(arr)):
    if arr[i]>max:
        max=arr[i]
print(max)
"""minimum"""
for i in range(1,len(arr)):
    min = arr[0]
    if arr[i]<min:
        min = arr[i]
print(min)