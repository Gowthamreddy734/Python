# Task2:

# Get a dynamic list from user

# clues Task2 and Task3
#1. get number of elements from user
#Loop through range
#append to list/dicti

#Inputs of Number of inputs user want to enter:

print("Task 2 started")
n = int(input("Enter your number"))
# defining empy list:
L=[]
# Taking multiple inputs based on n:
for i in range(n):
    #print(i)
    L.append(i)
print(L)


# Task3:
# Get a dynamic dictionary from user
print("Task 3 started")
n1 = int(input("Enter your number"))
# defining empy Dict:
L1= {}
# Taking multiple inputs based on n:
for i1 in range(n1):
    key=input("Enter key")
    Value=input("Enter value")
    L1[key]=[Value]
print(L1)



# Task4:

# Get two integers from user
# print multiples of 8 between them
# clues:
# Use range function in for loop
# Use if condition inside for loop
# add in to list
# input 10 100
# multiples of 8
# [16,24,32.....,96]


print("Task 4 started")


x=int(input("Enter your values"))
y= int (input("Enter your values"))
Li1 =[]
for i in range(x,y):
    if i%8==0:
        print(i)
        Li1.append(i)
print(Li1)


# Task5:

# Input:
# Li1 = [3,4,5,2,7,8,9,10]

# Output:
# Li_odd = [3,5,7,9]
# Li_even = [4,2,8,10]

# #Li1 = [3,4,5,2,7,8,9,10]
print("Task 5 Started")

Li2=[3,4,5,2,7,8,9,10]
#creating empty list 
even =[]
odd =[]
# itearting the list vales
for var in Li2:
    if var %2==0:
        even.append(var)
    else:
        odd.append(var)
print(odd)
print(even)

# Task6:

# Input: [-1, -7,8,10,20,21,17,28,-3,0,0,]
    
# Output:
# neg_LI = [-1,-7,-3]
# pos_LI = []
# Zeros = []

# Numeber of postivie ele: 7
# Number nega: 3
# Number of zeros: 2
print("Task 6 started")
Li3 =[-1,-7,8,10,20,21,17,28,-3,0,0,]
Neg =[]
pos =[]
Zero =[]
#iteriting list values in for loop
for val in Li3:
    #check the values
    if val >0:
        pos.append(val)
    elif val <0:
        Neg.append(val)
    else:
        Zero.append(val)
print(Neg)
print(pos)
print(Zero)


#Task 7
print("Task 7 started")
print(list(range(5)))
print(list(range(1,5)))
print(list(range(5,20)))
print(list(range(-5,5)))
print(list(range(10,100,10)))
print(list(range(10,0,-1)))
print(list(range(-5,5,3)))
print(list(range(10,100,5)))
print(list(range(10,0,-2)))
