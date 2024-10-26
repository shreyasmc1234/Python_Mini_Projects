#Decimal to Binary program by using python

number=int(input("Please Enter the number"))

store=""

while number>0:
    i=number%2
    store=str(i)+store
    number=number//2

print("The Binary number is "+store)
