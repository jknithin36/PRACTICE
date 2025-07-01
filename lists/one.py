# Built in Data Structure



# order collection of items


#  Creation 

#[] 


a = [1,2,3,4,5]

print(a)

# we can put any thing in the list 

b = list((1,2,3,4,5))

print(b)

c = list("hello")

print(c)


# Access 


# using Index

print(c[0])

print()






# create 

# accress

# insertion 

# Update

# search 

# find

# slice 

# Del

# reverse 

# count 






# LISTS 

"""
Used to Store Multiple variables



# properties 


ORDERED, Mutable, Indexed, Heterogenous, DynamicSize, Iterable, Scicable, Unhashable, Nested Support Data Structure




"""


# CREATION 


# Empty List 

a =[]

b = list()


print("__________________________")

print(a,b)


# With Elements 

a = [1,2,3,4,5, "hello", True, [], {}]
print(a)


# from Other Itrables 

c = list("hello")
print(c)




# ACCESSING ELEMENTS 


print(c[-1])

print(c[1])

# slicng 


print(c[0:2])

# reversed

print(c[::-1])


# modifying Elemnts 


c[0] = "H"

print(c)

# with slicing 

c[0:2]= ["H", "E"]

print(c)


# adding Elements 

c.append("JK")
print(c)


c.insert(0, 0)
print(c)


c.extend(list("NITHIN"))
print(c)


# remove 

c.pop()
c.pop(1)
c.remove("N")

del c[1]

print(c)


# c.clear()



print("JK" in c)

print(c.count("JK"))

print(c.index("I"))


d = c.copy()
e = c[:]

c.reverse()
print(c)
# change orgial one only


l =[1,2,3,4,5]

print(len(l))
print(min(l))
print(max(l))
print(sum(l))



# enumaurate



# create , Access, Adding, Remove, search , count, copy, reverse, sort, len, max, min, sum , enumurate, list Comphrensions


for i,val in enumerate(l):
    print(i,val)



# list


a = [x* x for x in range(5)]
print(a)

even =[ x for x in l if x % 2 ==0]
print(even)


od_or_even = ["even" if x % 2==0 else "odd" for x in range(5)]
print(od_or_even)



# map()	Magic paintbrush	Changes every item
# filter()	Sieve or strainer	Keeps only good ones
# reversed()	Flipbook	Plays list backwards
# zip()	Zipping coats	Matches two things together
# any()	Any light on?	True if at least one is “on”
# all()	All lights on?	True only if every light is on


# lsit Comphersions 

# 2D ARRAYS WITH LOUT BUILTIN FUNCTIONS i mean accessing and traversing and searcing without numpy sing lsit



