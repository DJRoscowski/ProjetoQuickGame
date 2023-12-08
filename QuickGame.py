#DJRoscowski
#In English, please!
import math
import random

unknown = 0
chooseMax = 10
kick = 0

print("Kick - Goal | game")
print()
print("How To Play: ")
print("1. Choose a maximum number;")
print("2. Enter a number until you get it right and move on to the next one.")

print()
print()

while True:

    try:

        chooseMax = int(input("Enter the MAXIMUM limit: "))
        unknown = random.randint(0, chooseMax)
        print(unknown)
        print("Attemps required: +ou- {}".format(math.ceil(math.log2(unknown))))

        while kick != unknown:
            kick = int(input("Enter the value: "))

            if unknown == kick:
                print("YEAH, Success! Next...")
            elif unknown < kick:
                print("Try again! The value is LOWER")
            elif unknown > kick:
                print("Try again! The value is HIGHER")
            else:
                print("Error")
            print()

    except ValueError:

        print("Invalid value!")