# Functions tasks
# ===================

# #User Def functions
# Write function to concatenate three strings
# Write a function multiply three different integers and return a int
# Write a function to check a string is palindrom or not
# Write a function to return middle char of the string
# write a function to return whether middle character is vowel or not 
# check whether number is prime or no
# check whether number is armstrong number or no
# Find factorial of a number
# Find Fibnacci series
# Find factors of a number

# # Write function to concatenate three strings
def concat(a,b,c):
    sum =a+b+c
    print(sum)
concat("Python"," is very ","Good language to learn")

# Write a function multiply three different integers and return a int

def mutiply(num1,num2,num3):
      return num1*num2*num3

t=mutiply(10,20,-330)
print(t)

# Write a function to check a string is palindrom or not
def isPalindrome(s):
    return s == s[::-1]

s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
#Write a function to return middle char of the string
def middle(name):
    legth =len(name)
    middle =legth //2
    return(name[middle])
t= middle("gowtham")
print(t)
#write a function to return whether middle character is vowel or not 
def midde (vowel):
    length =len(vowel)
    midd =length//2
    Cha = vowel[midd]
    if Cha.lower() in ('a', 'e', 'i', 'o', 'u'):
        return Cha
    elif Cha.upper() in ('A', 'E', 'I', 'O', 'U'):
        return Cha

a =midde("Gowaham")
print(a)

# check whether number is prime or no
n =int(input("Enter your number"))
def prime(n):
    if n%2==0:
        print("prime number")
    else:
        print("Not a prime number")
prime(n)

#check whether number is armstrong number or no

num = int(input("Enter a number: "))
def arm(num):
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
arm(num)
# Find factorial of a number

number1 = int(input("Enter your number"))
def factoial (number1):
    fact=1
    for var in range(1,number1+1):
        fact =fact*var
    print("the factorial number" ,fact)
factoial(number1)

# Find Fibnacci series

a = 0
b = 1
f = 1
n = int(input("Till what number would you like to see the fibonacci sequence: "))
def fibnacci(a,b,f,n):
    while b <= n:
        f = a+b
        a = b
        b = f
        print(a)
fibnacci(a,b,f,n)

# Find factors of a number
# take inputs
num = int(input('Enter number: '))

# find factor of number
print('The factors of', num, 'are:')
def factor(num):
    for j in range(1, num+1):
        if(num % j) == 0:
            print(j)
factor(num)
