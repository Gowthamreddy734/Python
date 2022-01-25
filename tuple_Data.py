#Tuple rules
#() or without braces
#ordered or indexed data structure
#Immutable
#Allows duplicates
#Concatenation is supported


#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
#Find the common elements between two tuples
#Concatenate both tuples and remove duplicates from tuple
#Find the index value of 9 (after concatenation)
#multiply above elements 3 times


#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
from pickle import TUPLE3
from numpy import common_type


tup =tuple()
print(type(tup))
tuple = ()
print(tuple)
tup1 =(1,4,5,6,7,8,9)
tup2 =(5,6,7,8,9)

#Find the common elements between two tuples
tup_1 =set(tup1)
tup_2 =set(tup2)
commonElements = (tup_1 & tup_2)
print(" The common elements between two tuple {} = " .format(commonElements))


#concentaing two tuples
tup3 = tup1+tup2
print(tup3)


#Find the index value of 9 (after concatenation)

print("The Idex value of 9  = {} " .format(tup3.index(9)))


# remove the dupliacte form the tuples
my_unique_tup = list(set([i for i in tup3]))
print(my_unique_tup)

#multiply above elements 3 times

print(3*tup3[0],3*tup3[1],3*tup3[2],3*tup3[3],3*tup3[4],3*tup3[5],3*tup3[6])










