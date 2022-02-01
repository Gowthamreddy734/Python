#Task1:

#Using Range function  print multiples of 5 from 0 to 75
#Using Range function  print multiples of 8 from 0 to 72

#Using Range function  print multiples of 5 from 75 to 0
#Using Range function  print multiples of 8 from 96 to 72

#Using Range function  print multiples of 5 from 0 to 75
for i in range(0,76):
    if i %5 ==0:
        print("The mutiple of 5 vlaues ",i)

#Using Range function  print multiples of 8 from 0 to 72
for var in range (0,73):
    if var %8==0:
        print("The mutiple of 8  value",var)


#Using Range function  print multiples of 5 from 75 to 0

for val in range(75,-1,-1):
    if val%5==0:
        print("The mutiple of 5 vlaues",val)
#Using Range function  print multiples of 8 from 96 to 72
for va in range(96,71,-1):
    if va %8==0:
        print("The mutiple of 8  value",va)
