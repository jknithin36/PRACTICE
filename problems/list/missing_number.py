
# Missing Number
# Write a function to find the missing number in a given integer array of 1 to 100. The function takes to parameter the array and the number of elements that needs to be in array.  For example if we want to find missing number from 1 to 6 the second parameter will be 6.

# Example

# missing_number([1, 2, 3, 4, 6], 6) # 5



# def missing_number(arr, total):
#     return total *  (total +1) // 2 - sum(arr)




# print(missing_number([1,2,3,4,5,6,8],8)
# )
    




#  Problem 1: Sum of First N Natural Numbers
# Input: n = 100
# Output: 5050

#  Write a function to return the sum of first n numbers without using loops.




def sum_of_first_n(n):
    return n * (n+1)//2

print(sum_of_first_n(10))



#Problem 2: Missing Number in Array
# You are given an array of n distinct numbers in the range 1 to n+1, with one number missing.

# python
# Copy
# Edit
# Input: [1, 2, 4, 5, 6]
# Output: 3




def missing_number(arr, n):
    return n * (n+1) //2 - sum(arr)


print(missing_number([1,3,4,5], 5))




def two_sum(arr, val):
     sorted_array = sorted(list(arr))
     left = 0
     right = len(sorted_array) -1

     while left < right:
         current_sum = sorted_array[left] + sorted_array[right]
         if current_sum == val:
             return [left, right]
         elif current_sum < val:
             left+=1
         else:
             right -=1
    
     return None
             
         

        

print(two_sum([3,2,4],6))

        

# Max Product of Two Integers
# Find the maximum product of two integers in an array where all elements are positive.

# Example

# arr = [1, 7, 3, 4, 9, 5] 
# max_product(arr) # Output: 63 (9*7)



def max_product(arr):
    max = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] > max:
                max = arr[i] * arr[j]
    
    return max



print(max_product([1, 7, 3, 4, 9, 5]))