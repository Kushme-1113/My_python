"""Build a number guessing game"""
"""computer picks a random number,user keeps guessing until correct """
import random
com = random.randint(1,100)
tries = 0
while True:
    tries += 1
    hum = int(input("Guess your number between 1 and 100: "))

    if hum == com:
        print(f"congratulations you have won the game in {tries} tries")
    elif hum > com:
        print("sorry wrong guess go lower")
    else:
        print("sorry wrong guess go higher")


