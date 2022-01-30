#Fizz buzz
#Get one number from user
#5
#Multiple of 3 ==> Fizz
#Multiple of 5 ===> buzz
#Multiple of 3 and 5 ===> Fizzbuzz
#None ==> Invalid number

number =int(input("Enter your number"))
if number%3==0:
    print("Fizz")
elif number%5==0:
    print("buzz")
elif number%3==0 and number%5==0:
    print("Fizzbuzz")
else:
    print("invalid number")