
#mark calculation

#collect physics / checmistry / mathematics mark from user
#all the marks should be between 0 -200 ==> 
#calculate aggregate = phy/4  + chem/4  + maths / 2

#pass mark: 70



# aggregate > 190 :  First class
    
# aggregate > 150 : second class
    
# aggregate > 70 : Third class 
    
# aggregate < 70 : Fail Try again
    
    
#valid or invalid
#Pass or Fail
#Class 





Physics = int(input("Enter your physics marks"))
chemistry =int(input("Enter your Chemistry marks"))
mathematics = int (input("Enter your mathematics marks"))

if Physics > 0 and Physics <=200:
    print ("valid marks phsics")
elif chemistry >0 and chemistry <=200:
    print("valid marks chemistry")
elif mathematics >0 and mathematics <=200:
    print("valid marks maths")
else:
    print("invalid marks")


avg =Physics/4 +chemistry/4 + mathematics/2
print(avg)
if avg >190:
    print("First class")
elif avg >150:
    print("Second class")
elif avg >70:
    print("Third class")
elif avg <=70:
    print("Fail Try again")