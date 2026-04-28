# menu.py - menu for dice roll game

from games import game


def show_menu():
    print("\n====== DICE ROLL GAME ======")
    print("1. Roll the Dice")
    print("2. Exit")
    print("============================")


def run():
    print("Welcome to the Dice Roll Game!")

    while True:
        show_menu()
        ch = input("Enter your choice: ")

        if ch == "1":
            game.play()

        elif ch == "2":
            print("Thanks for playing! Bye!")
            break

        else:
            print("Invalid choice. Try again.")
