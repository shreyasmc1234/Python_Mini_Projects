import random

user_point=0
computer_point=0

selection = ["ROCK","PAPER","SCISSOR"]
user_name=input("Please Enter your name : ")

while True:

    user_input=input("Please select your choice : \"Rock, Paper, Scissor\" or Please Enter \"Q\" to quit : ")

    if user_input.upper()=="Q":::wq
        print("Thank you ! Come again :) \n\n")
        break

    if user_input.upper() not in selection:
        continue

    computer_input=selection[random.randint(0,2)]

    if user_input.upper()=="ROCK" and computer_input.upper()=="SCISSOR":
        user_point+=1
        print(f"{user_name} Won")
    elif user_input.upper()=="PAPER" and computer_input.upper()=="ROCK":
        user_point+=1
        print(f"{user_name} Won")
    elif user_input.upper()=="SCISSOR" and computer_input.upper()=="PAPER":
        user_point+=1
        print(f"{user_name} Won")
    else:
        computer_point+=1
        print("Computer Won")

print(f"Hey !! {user_name}, Thanks for Playing the Game!!")
print("Your Score is",user_point)
print("Computer Score is",computer_point)

if user_point>computer_point:
    print("Final Result: You Won!")
elif user_point==computer_point:
    print("You both scored the same point")
else:
    print("You Lost! Computer Won Try Again")