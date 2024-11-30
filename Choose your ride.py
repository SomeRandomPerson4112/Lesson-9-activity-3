print("Select your ride:")
print("1: Bike")
print("2: Car")
choice=int(input("Enter your choice: "))
if choice==1:
    print("What type of bike?")
    print("1.Scooty")
    print("2.Scooter")
    choice2=int(input("Enter your choice: "))
    if choice2==1:
        print("You have chosen scooty")
    else:
        print("You have chosen scooter")
elif choice==2:
    print("What type of car?")
    print("1.Sedan")
    print("2.XUV")
    choice2=int(input("Enter your choice: "))
    if choice2==1:
        print("You have chosen Sedan")
    else:
        print("You have chosen XUV")
else:
    print("error")