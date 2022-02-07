# Miniproject: (3 hours) 

# rock paper scissor

# 1 player: user  2nd player: system

# rock + rock ==> Tie
# paper + paper ==> Tie
# scissor + scissor ==> Tie

# rock + scissor ==> rock
# paper + scissor ==> scissor 
# rock + paper  ===> paper

# How to collect user input ==> input

# How to collect system input ==> random

# import random

# Li1 = ["rock","paper","scissor"]

# print(random.choice(Li1))
# print(random.choice(Li1))
# print(random.choice(Li1))
# print(random.choice(Li1))
# print(random.choice(Li1))

# Number of games you want to play ? collect one integer

# Who wins?

# Number of games you want to play ?  3

# Game 1:
# Give your input ["rock","paper","scissor"] : rock
# System input: random 


# Game 2:

# Give your input ["rock","paper","scissor"] : rock
# System input: random 

# Game3

# Give your input ["rock","paper","scissor"] : rock
# System input: random 

# Total of number games: 3
# System points ==> 0
# User point ==> 2
# Tie ===> 1

# USER wins the game !!! Congrats !!!!



import random

Game =int(input("Enter How many games you need play"))
computerwins = 0
playerwins = 0
ties = 0
for i in range(1,Game):
    user_input =input("Enter you values(rock,paper,scissor)")
    print("Game",i)
    Li1 = ["rock","paper","scissor"]
    computer_action=random.choice(Li1)
    print("user {} Computer {}" .format(user_input,computer_action))

    if user_input == computer_action:
        print("User {} computer {}  its tie ".format(user_input,computer_action))
        ties += 1
    elif user_input == "rock":
        if computer_action == "scissor":
            print("Rock wins")
            playerwins +=1
        else:
            print("paper wins")
            computerwins += 1
    elif user_input=="paper":
        if computer_action == "rock":
            print("paper wins")
            playerwins +=1
        else:
            print("scissor wins")
            computerwins += 1
    elif user_input=="scissor":
        if computer_action=="paper":
            print("scissor wins")
            playerwins +=1        
        else:
            print("Rock wins")
            computerwins+1
print("Total number of games",i)
print("System points ==",computerwins)
print("user points==",playerwins)
print("Tie points==",ties)
if playerwins >computerwins:
    print("USER wins the game !!! Congrats !!!!")
else:
    print("System wins the game !!! Congrats !!!!")
