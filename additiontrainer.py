# Program 2: Addition Trainer
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random
score = 0


def addition(): # I used function so redundancy of long line of codes will be avoided.
    num1 = random.randint(0,99)
    num2 = random.randint(0,99)

    print(str(num1), "+", str(num2), "= ?")
    answer = int(input("Answer = "))


    if(num1 + num2 == answer):
        print("Correct!")
        score = 1
    else: 
        print("Wrong!")
        score = 0
    return score


score = score + addition()
score = score + addition()
score = score + addition()
score = score + addition()
score = score + addition()
score = score + addition()
score = score + addition()
score = score + addition()
score = score + addition()
score = score + addition()

print("Your total score is " + str(score) + "/10")

