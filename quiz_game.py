print("Welcome to Quiz !! :)")

i=input("Do you want to Play Quiz :")

if i.lower()=='yes': #ignoring the casing
    h = input("Please enter your Name :")
    s=0
    j=input("What is the full form of CPU? :")
    if j.upper()=="CENTRAL PROCESSING UNIT":
       s = s+1
       print("Correct !")
    else:
        print("Incorrect !")

    k=input("Which is the largest ocean in the Earth? :")
    if k.title()=="Pacific Ocean":
        s += 1
        print("Correct !")
    else:
        print("Incorrect !")

    k = input("Who is the co-founder of Microsoft? :")
    if k.lower() == "bill gates":
        s += 1
        print("Correct !")
    else:
        print("Incorrect !")

    k = input("What is the largest Plannet in the solar system? :")
    if k.lower() == "jupiter":
        s += 1
        print("Correct !")
    else:
        print("Incorrect !")

    k = input("What is the square root of 64? :")
    if k == "8":
        s += 1
        print("Correct !")
    else:
        print("Incorrect !")

    print(f"Thank you {h} for participating the Quiz !!")
    print(f"Your Total Score is : {s} !! Happy Learning")
else:

    quit()
