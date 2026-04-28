# game.py - dice roll game logic

import random


def roll_dice():
    return random.randint(1, 6)


def play():
    print("\n--- Dice Roll Game ---")
    print("Both you and the computer will roll a dice.")
    input("Press Enter to roll...")

    user_dice = roll_dice()
    comp_dice = roll_dice()

    print("Your dice  :", user_dice)
    print("Computer   :", comp_dice)

    if user_dice > comp_dice:
        print("You Win!")
    elif user_dice < comp_dice:
        print("Computer Wins!")
    else:
        print("It's a Tie!")
