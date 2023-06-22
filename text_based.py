import Deck
from cards import *
from character import *
from Deck import *
from Enemy import *
from combat import Combat

def main_menu():
    print("Welcome to Wizarding World")
    print("1. New Game")
    print("2. Load Game")
    print("3. Settings")
    print("4. Exit")

    choice = input("Enter the number of your choice: ")
    if choice == "1":
        new_game()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice. Try again.")
        main_menu()

def class_menu():
    print("Select a Character Class:")
    class_options = ["Storm", "Fire", "Ice", "Death", "Life", "Myth", "Balance"]
    for idx, cls in enumerate(class_options):
        print(f"{idx + 1}. {cls}")

    choice = int(input("Enter the number of your chosen class: ")) - 1
    if 0 <= choice < len(class_options):
        selected_class = class_options[choice]
        print(f"Selected {selected_class}")
        tutorial(selected_class)
    else:
        print("Invalid choice. Try again.")
        class_menu()

def tutorial(selected_class):
    print("Tutorial starting...")

    player = Character(name="Player", class_type=selected_class, max_health=1500, max_mana=50, deck=starter_deck)
    golem = Enemy("Golem", 1000, 0.5, golem_deck, "Myth")

    combat = Combat(player, golem)
    combat.start()

    print("Tutorial complete!")


def new_game():
    print("New game starting...")
    class_menu()

main_menu()
