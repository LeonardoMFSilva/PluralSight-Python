import random

roll = random.randint(1,6)

guess = int(input('Guess the dice roll:\n'))

# while guess != roll:
if roll == guess:
    print("You have guessed!\n" + "The computer rolled a " + str(roll) + " and you guessed with a " + str(guess))

else:
    print("You did not guess it =/")
    print("The computer rolled a " + str(roll))
