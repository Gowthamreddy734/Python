# Task 8 - 12:

# check whether number is prime or no

from math import factorial


number = int(input("Enter your number")) 
if number%2==0:
    print("primenumber")
else:
    print("Not aprime ")
    #Using for loop 
    for i in range(2,number):
        if(number%i==0):
            print("prime number",i)
        else:
            print("Nt a prime number",i)




# check whether number is armstrong number or no

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# Find factorial of a number
number1 = int(input("Enter your number"))
fact=1
for var in range(1,number1+1):
    fact =fact*var
print("the factorial number" ,fact)

# Find Fibnacci series
a = 0
b = 1
f = 1
n = int(input("Till what number would you like to see the fibonacci sequence: "))
while b <= n:
    f = a+b
    a = b
    b = f
    print(a)

# Find factors of a number
# take inputs
num = int(input('Enter number: '))

# find factor of number
print('The factors of', num, 'are:')
for j in range(1, num+1):
    if(num % j) == 0:
        print(j)

# 12: 1,2,3,4,6,12
# 9: 1,3,9
# 10: 1,2,5,10