
from re import L
import statistics



##what is Data Structures

#How to store multiple data/values effectively
#List rules

#BAsic
#Heterogenous ===> it can store more than one data type in a single var/data
#List
#[]
#ordered or indexed data structure
#Mutable
#Allows duplicates
#Concatenation is supported


#Create an empty list (two ways)
#Concatenate with [5,6,7,8]
#add 8,9,1,5,6,7,8,1 elements to that list
#Find frequency of 8 (count)
#find the mean of the list
#find sum (List) + min + Max 
#Find median of the list
#remove duplicates from list and give output in the format of tuple


# Creating a list with inbuilt function 

List =list()
print(type(List))
# creating a empty list 
List_1 =[]
print(type(List_1))

#Concatenate with [5,6,7,8]
# adding to elemnts
List_2 =[5,6,7,8]
List_3 = List+ List_2
print(List_3)

#add 8,9,1,5,6,7,8,1 elements to that list
#Append take only one argumnet 
#insert will take only one argument 
# List_3.append(8)
# List_3.append(9)
# List_3.append(1)
# List_3.append(5)
# List_3.append(6)
# List_3.append(7)
# List_3.append(8)
# List_3.append(1)
List_3.extend([8,9,1,5,6,7,8,1])
print(List_3)


#Find frequency of 8 (count)
Count = List_3.count(8)
print("The Frequency of 8 count = {}" .format(Count))

#find the mean of the list
#Adding all the values in list and divided by len() of the list to find the mean of list  
mean =  sum(List_3) / len(List_3)
print("Mean of the list = {}" .format(mean))

#find sum (List) + min + Max 

sum_1 = sum(List_3)
min_1 =min(List_3)
max_1 =max(List_3)
len_1 =len(List_3)
print("sum = {} min = {} max = {} len = {} ".format(sum_1,min_1,max_1,len_1))


#Find median of the list
#Median of list
# Using loop + "~" operator
List_3.sort()
mid = len(List_3) // 2
res = (List_3[mid] + List_3[~mid]) / 2
print("The medain of the list = {} " .format(res))
#another method for finding the medain of the list
median_1 = statistics.median(List_3)
print("The median of the  list differnet method = {}".format(median_1))

#remove duplicates from list and give output in the format of tuple
for i in List_3:
    if i not in List:
        List.append(i)
print("Remove duplicates from the list = {}" .format(List))        
List_3 =list(set(List_3))
print(List_3)

#remove the elemnts form the list 
List_3.remove(5)
print(List_3)
# sort the elements of list
List_3.sort()
print(List_3)
#reverse the elemnets from the list
List_3.reverse()
print(List_3)


#convert to tuple
List =tuple(List)
print(List)