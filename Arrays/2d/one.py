

#LECTURE 36

# Two Dimanesional Array


# multiple colms and mutliple rows


# why wdo we need it 


# when we deal with matrices 

# games 



# creation 


from array import *


import numpy as np


two_d = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,9]], dtype=int)

print(two_d)


# TIME COMPLEXITY 

# ADD 




# INSERTION 


# To Insaert we need to follow this syntax


# np.insert(array, index, values, axis =0)


# index position

# values list representing the row

# axis :0 = ROw


arr_with_row = np.insert(two_d, 1, [1,2,3,4], axis=0)


print(arr_with_row)

# adding column


arr_With_col = np.insert(two_d, 1, [1,1,1,1], axis=1)

print(arr_With_col)



# PRACTICE WITHLIST TOO WHEN IN LIST TOPIC COMES



# ACCESS ELEMETS 


# [rowindex][columindex]



def accessElement(arr, rowindex, colindex):
    if rowindex >= len(arr) or colindex >= len(arr[0]):
        return -1
    return arr[rowindex][colindex]



print(accessElement(arr_With_col, 1,1))



# TRAVERSAL 


for i in arr_With_col:
    for j in i:
        print(j , end =" ")
    print(" ")




# search 




def search_element(arr, val):
    for row in arr:
        for elem in row:
            if elem == val:
                return True      # early exit
    return False




search_element(arr_With_col,10 )





# adding row













# delete(arr, index, axis)


# when to use Arrays


# multip variables of same datatype


# Random Access