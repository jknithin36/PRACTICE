# lecture 29

import numpy as np


np_array = np.array([], dtype=int)


# INSTERTION 


# at first, at the end, in the middle 


from array import *

arr = array("i", [1,2,3,4])



arr.insert(0,0)

print(arr)


arr.append(5)

print(arr)


# Time Complexity --> O(N)

# Space Complexity --> O(1)




# lecture 30

# traverse - visiting elements one by one until the end 


for i in arr:
    print(i)



for i in range(len(arr)):
    print(arr[i])




i =0
length = len(arr)

while i < length:
    print(arr[i])
    i +=1





# Traverse Time and Space Complexity


# O(N) 





# Lecture 31



# Access

# using Index



print(arr[0])



def accessElement(array, index):
    if index > len(arr):
        print("Index is out of bound")
        return
    
    print(array[index])



accessElement(arr, 10)



# Time and Space O(1) and O(1)



# lecture 32 


# Search 


# Linear Search -->iterate through array one by one 


def SearchElement(arr, value):
    if value not in arr:
        return "ELEMENT IS NOT PRESENT IN ARRAY"
    
    for i in arr:
        if i == value:
            print(i)





SearchElement(arr, 5)






# Tiome complecity --> o(N)



# DELETION 


arr.remove(5)


print(arr)


# TIME AND SPACE 


# O(N)


# O(1)


# ALL THE TIME AND SPACE COMPLEXITY


'''


Creation 

Empty --> O(1) O(1)

WITH ELEMENTS --> O(N) O(N)


Insert Value --> O(N) O(1)


TRAVERSE --> O(N) O(1)


Access --> O(1) O(1)


Search --> O(N) O(1)

Delete --> O(N) O(1)

'''