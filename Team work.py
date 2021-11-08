# Miguel Jusino, leslie Bacajol
import random

num = random.randrange(1, 11)
print (num)

# take off when turn in

guess = int(input("please guess a number 1 and 10 ="))

while guess != num:
    if guess > num:
        print("please guess lower")
    elif guess < num:
        print("please guess higher")
    else:

        break

    guess = int(input("please guess a number 1 and 10 ="))

print("correct!")

