# create and array traverse

from array import *


one = array("i", [1,2,3,4,5])


for i in one:
    print(i)

# Access using index


print(one[0])
print(one[1])


# append any value using append method 


one.append(6)
one.append(7)
print(one)



# insert an value using Insert MEthod


one.insert(0,0)

print(one)


# extend an array 


one.extend([8,9])

print(one)



lis = [1,2,3,4,5]

a = array("i")

a.fromlist(lis)


print(a)




a.remove(5)
print(a)

a.pop()

print(a)


print(a.index(3))



a.reverse()

print(a)


print(a.buffer_info())


print(a.count(1))


