
import random

def roll_dice():
    while True:
        input("Press Enter to roll the dice...")

        dice = random.randint(1, 6)

        print("You rolled:", dice)

        choice = input("Roll again? (yes/no): ")

        if choice.lower() != "yes":
            print("Thanks for playing!")
            break

roll_dice()