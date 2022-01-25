#Sets

#{}
#ordered or indexed data structure not supported
#Mutable
#Dont Allows duplicates
#Concatenation is not supported



#Create two empty sets
#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
#check whether set2 is subset of set1 or no ?
#check whether both have common elements are no ?
#remove 8 from set 1 and set 2 ==> find the inferences
#discard 0 from set1 and set2 
#find collection of both sets ===> set1 and set2

#Create two empty sets
Set =set()
print(Set)
#update set1 with 7,8,9,1,2,3,4,5,0
Set1 ={7,8,9,1,2,3,4,5,0}
print(Set1)
#update set2 with 4,5,6,0
Set2={4,5,6,0}
print(Set2)
#check whether set2 is subset of set1 or no ?
a = Set1.issubset(Set2)
print(a)

#check whether both have common elements are no ?
b = Set1.isdisjoint(Set2)
print(b)

#remove 8 from set 1 and set 2 ==> find the inferences

Set1.remove(8)
print(Set1)

c = Set1.difference(Set2)
print(c)


#discard 0 from set1 and set2 
Set1.discard(0)
Set2.discard(0)
print(Set1)
print(Set2)



#find collection of both sets ===> set1 and set2

D =Set1