#Get one mark from student
#mark 0 to 100 otherwise invalid mark

#50 + PASS otherwise FAIL
#90 to 100 ===> A 
#80 to 89 ===> B
#70 to 79 ===> C
#60 to 69 ===> D
#50 to 59 ===> E

#0 to 49 ===> FAIL


#93 ===> A
#99 ===> A
#88 ====> B

#78

#VALID MARK (between 0 to 100)
#PASS MARK ()
#C




from pickletools import markobject


Mark = int(input("Enter your mark "))

if Mark > 0 and Mark <=100:
    print("Marks are correct")
else :
    print("marks should be between 0 to 100")

if Mark >=50:
    print("pass")
if Mark >=90 and Mark <=100:
    print("A++++++++++")
elif Mark >=80 and Mark <=89:
    print("B++++++++++")
elif Mark >=70 and Mark <=79:
    print("C++++++++++")
elif Mark >=60 and Mark <=69:
    print("D++++++++++")
elif Mark >=50 and Mark <=59:
    print("E++++++++++")
elif Mark >=0 and Mark <=49:
    print("Fail ++++++++++")