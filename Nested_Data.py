#Task1

from re import L


Li1 = [2,3,4,5,[45,56,67,78,[111,222,333,[5555,3333,[10000,50000,"python","computer"],1111,7777,8888],444,555,666,777],89,23,34]]

print(Li1[3])
print(Li1[-1][1])
# print(Li1[-2][1][1])


# 5
# 56
# 222
# 50000
# put
# 5555
# 7777
# 666
# 89
# on
# 333

# 3333

# Task2


a = [1,2,3,4,[100,101,102,"Computer_science"],200,203]
# Extract
print(a[4][3][8:])
print(a[4][3][0:8])
# #science
# #computer

# Task3
a = [1,2,3,4,[101,102,103,[201,202,[999]], 666, 777]]
#print(a[5][5][1])
# Extract
#666
#201
#102
#999
#777


# Task4:

Li1 = [2,3,"python","hello",4,5,0]  

# Extract
print(Li1[3][2:4])
print(Li1[2][2:])
# #ll
# #thon

# Task5
Li1 = [1,2,3,4,5,[11,22,33,44,55,[111,222,333,444],6666,7777],7777]

# Output Prediction 

print(Li1[5][0])
print(Li1[5][6])
print(Li1[5][-2])
print(Li1[5][7])
print(Li1[6])
print(Li1[5][5][1])
print(Li1[-2][-1])
print(Li1[-2][2:4])


# Task6:

a = {1: [1,2,3,"python"], 2:{10:"hello",20:"welcome",40: "science"}, 99: {3,4,5,6}, 40:{1:"zoology", 2:"Botany"}}


#py
#ello
#en
#zoo
#Bot



print(a)