print("Please select an option from the list beneath: ")
Learn_Python = 1
Learn_Java = 2
Go_Swimming = 3
Have_Dinner = 4
Go_To_Bed = 5
Watch_a_Show = 6
Exit = 0

print("1. Learn Python")
print("2. Learn Java")
print("3. Go Swimming")
print("4. Have Dinner")
print("5. Go To Bed")
print("6. Watch a show")
print("0. Exit")

command = int(input("Enter command"))
if command == 1:
    print("Please be careful with learning Python, it can be complicated :/")
elif command == 2:
    print("Java is okay, but can be cool")
elif command == 3:
    print ("Going swimming is cool, but keep an eye out")
elif command == 4:
    print("You really enjoy dinner when you are really hungry")
elif command == 5:
    print("Sleeping can be the highlight of your day!")
elif command == 6:
    print("The best shows are the ones with many seasons")
elif command == 0:
    print("Exiting")
