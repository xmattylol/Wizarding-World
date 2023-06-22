import Deck
from cards import *
from character import *
from Deck import *
from Enemy import *

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

    player_turn = True
    in_combat = True
    round_start = True
    while in_combat:
        if round_start:
            # Give pips
            player.pips += 1
            golem.pips += 1
            round_start = False

        if player_turn:

            print()
            print(player)
            print(golem)
            print("Your turn:")

            for idx, card_name in enumerate(player.hand):
                card = cards.get_card(card_name)
                print(f"{idx + 1}. {card}")

            card_to_play = None
            while card_to_play is None:
                user_input = input("Enter the number of the card you want to play or 'pass': ")
                if user_input.lower() == "pass":
                    print("You chose to pass your turn.")
                    player_turn = False
                    break
                #try:
                card_choice = int(user_input) - 1
                if 0 <= card_choice < len(player.hand):
                    card_name_to_play = player.hand[card_choice]
                    card_to_play = cards.get_card(card_name_to_play)
                    if player.deck.count_cards(
                            card_to_play.name) > 0:  # Check if the card is still available in the deck
                        if player.pips >= card_to_play.cost:
                            player.play_card(card_to_play, golem)
                            player_turn = False
                        else:
                            print(
                                f"{card_to_play.name} costs {card_to_play.cost} pips, you have {player.pips} pips. Choose another card or pass.")
                            card_to_play = None
                    else:
                        print(f"You have no more {card_to_play.name} cards in your deck.")
                        card_to_play = None
                else:
                    print("Invalid card number. Choose a valid card or pass.")
                #except ValueError:
                #    print("Invalid input. Enter a card number or 'pass'.")
            player_turn = False # May be trivial

        else:
            print("Enemy's turn.")
            card_name_to_play = golem.choose_card(golem.pips)
            card_to_play = cards.get_card(card_name_to_play)
            card_played = False
            while not card_played:
                if card_name_to_play:
                    card_to_play = cards.get_card(card_name_to_play)  # Get card object from name
                    if golem.pips >= card_to_play.cost:
                        golem.play_card(card_to_play, player)  # Pass card object, not name
                        card_played = True
                    else:
                        golem.hand.remove(card_to_play.name)
                        if golem.hand:
                            card_name_to_play = golem.choose_card(golem.pips)
                            if card_name_to_play:
                                card_to_play = cards.get_card(card_name_to_play)  # Get card object from name
                        else:
                            print("Enemy has no valid cards to play, skipping turn.")
                            break
                else:
                    print("Enemy has no valid cards to play, skipping turn.")
                    break
            player_turn = True
            round_start = True  # This sets the start of the next round as the enemy's turn ends.
            #     if card_to_play and golem.pips >= cards.get_card(card_to_play).cost:
            #         golem.play_card(card_to_play, player)
            #         card_played = True
            #     else:
            #         if card_to_play:
            #             golem.hand.remove(card_to_play.name)
            #         if golem.hand:
            #             card_to_play = golem.choose_card(golem.pips)
            #         else:
            #             print("Enemy has no valid cards to play, skipping turn.")
            #             break
            # player_turn = True
        if player.is_defeated():
            print("You have been defeated. Try again!")
            break

        if golem.is_defeated():
            print("You have defeated the Golem!")
            in_combat = False
            break

    print("Tutorial complete!")




# def tutorial(selected_class):
#     print("Tutorial starting...")
#
#     player = Character(name="Player", class_type=selected_class, max_health=1500, max_mana=50, deck=starter_deck)
#     golem = Enemy("Golem", 1000, 0.5, golem_deck, "Myth")
#
#     player_turn = True
#     in_combat = True
#
#     while in_combat:
#         # Give pips
#         player.pips += 1
#         golem.pips += 1
#
#         if player_turn:
#             print()
#             print(player)
#             print(golem)
#             print("Your turn:")
#
#             for idx, card_name in enumerate(player.hand):
#                 card = cards.get_card(card_name)
#                 print(f"{idx + 1}. {card}")
#
#             card_to_play = None
#             while card_to_play is None:
#                 user_input = input("Enter the number of the card you want to play or 'pass': ")
#                 if user_input.lower() == "pass":
#                     print("You chose to pass your turn.")
#                     player_turn = False
#                     break
#
#                 try:
#                     card_choice = int(user_input) - 1
#                     if 0 <= card_choice < len(player.hand):
#                         card_to_play = cards.get_card(player.hand[card_choice])
#                         if player.pips >= card_to_play.cost:
#                             player.play_card(card_to_play, golem)
#                             player_turn = False
#                         else:
#                             print(f"{card_to_play.name} costs {card_to_play.cost} pips, you have {player.pips} pips. Choose another card or pass.")
#                             card_to_play = None
#                     else:
#                         print("Invalid card number. Choose a valid card or pass.")
#                 except ValueError:
#                     print("Invalid input. Enter a card number or 'pass'.")
#         else:
#             print("\nEnemy's turn.")
#             card_to_play = golem.choose_card(golem.pips)
#             if card_to_play and golem.pips >= card_to_play.cost:
#                 golem.play_card(card_to_play, player)
#             else:
#                 print("Enemy has no valid cards to play, skipping turn.")
#             player_turn = True
#
#         if player.is_defeated():
#             print("You have been defeated. Try again!")
#             break
#
#         if golem.is_defeated():
#             print("You have defeated the Golem!")
#             in_combat = False
#             break
#
#     print("Tutorial complete!")



def new_game():
    print("New game starting...")
    class_menu()

main_menu()
