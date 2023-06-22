from cards import *
class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.current_turn = None  # Represents who's turn it is. None represents the start of a new round
        self.in_combat = True

    def start(self):
        print("Battle starting...")

        while self.in_combat:
            if self.current_turn is None:
                self.start_round()
                continue

            if self.current_turn == self.player:
                self.player_turn()
            else:
                self.enemy_turn()

            if self.player.is_defeated():
                print("You have been defeated. Try again!")
                self.in_combat = False

            if self.enemy.is_defeated():
                print("You have defeated the enemy!")
                self.in_combat = False

        print("Battle complete!")

    def start_round(self):
        # Give pips
        self.player.pips += 1
        self.enemy.pips += 1
        self.current_turn = self.player

    def player_turn(self):
        print()
        print(self.player)
        print(self.enemy)
        print("Your turn:")

        for idx, card_name in enumerate(self.player.hand):
            card = get_card(card_name)

            print(f"{idx + 1}. {card}")

        card_to_play = None
        while card_to_play is None:
            user_input = input("Enter the number of the card you want to play or 'pass': ")
            if user_input.lower() == "pass":
                print("You chose to pass your turn.")
                self.current_turn = self.enemy
                break

            card_choice = int(user_input) - 1
            if 0 <= card_choice < len(self.player.hand):
                card_name_to_play = self.player.hand[card_choice]
                card_to_play = get_card(card_name_to_play)
                if self.player.deck.count_cards(card_to_play.name) > 0:  # Check if the card is still available in the deck
                    if self.player.pips >= card_to_play.cost:
                        self.player.play_card(card_to_play, self.enemy)
                        self.current_turn = self.enemy
                    else:
                        print(
                            f"{card_to_play.name} costs {card_to_play.cost} pips, you have {self.player.pips} pips. Choose another card or pass.")
                        card_to_play = None
                else:
                    print(f"You have no more {card_to_play.name} cards in your deck.")
                    card_to_play = None
            else:
                print("Invalid card number. Choose a valid card or pass.")

    def enemy_turn(self):
        print("Enemy's turn.")
        card_name_to_play = self.enemy.choose_card(self.enemy.pips)
        card_played = False
        while not card_played:
            if card_name_to_play:
                card_to_play = get_card(card_name_to_play)  # Get card object from name
                if self.enemy.pips >= card_to_play.cost:
                    self.enemy.play_card(card_to_play, self.player)  # Pass card object, not name
                    card_played = True
                else:
                    self.enemy.hand.remove(card_to_play.name)
                    if self.enemy.hand:
                        card_name_to_play = self.enemy.choose_card(self.enemy.pips)
                        if card_name_to_play:
                            card_to_play = get_card(card_name_to_play)  # Get card object from name
                    else:
                        print("Enemy has no valid cards to play, skipping turn.")
                        break
            else:
                print("Enemy has no valid cards to play, skipping turn.")
                break
        self.current_turn = None  # This sets the start of the next round as the enemy's turn ends.








# class Turn:
#     def __init__(self, player):
#         self.player = player
#         self.actions = []
#
#     def add_action(self, action):
#         self.actions.append(action)
#
# class Action:
#     def __init__(self, card, target):
#         self.card = card
#         self.target = target
#
# class Board:
#     def __init__(self):
#         self.characters = []
#         self.enemies = []
#         self.obstacles = []
#
#     def add_character(self, character):
#         self.characters.append(character)
#
#     def add_enemy(self, enemy):
#         self.enemies.append(enemy)
#
#     def add_obstacle(self, obstacle):
#         self.obstacles.append(obstacle)
