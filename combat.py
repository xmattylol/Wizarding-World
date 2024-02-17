from cards import *
class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.current_turn = None  # Represents who's turn it is. None represents the start of a new round
        self.in_combat = True
        self.target = None  # Initialize the target to None. We will update this during each turn.


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

    def update_hand(self):
        """Remove cards from the player's hand if they have been used up."""
        # Loop over the cards in the player's hand in reverse order
        # We loop in reverse so that we can remove cards while iterating
        for i in reversed(range(len(self.player.hand))):
            # Check if the player has any of this card left in their deck
            card_name = self.player.hand[i]
            card = get_card(card_name)
            if self.player.deck.count_cards(card.name) == 0:
                # If not, remove it from their hand
                del self.player.hand[i]


    def player_turn(self):
        #self.update_hand()
        self.player.draw_up_to_seven_cards()

        print("----------------------------")
        print(self.player)
        print(self.enemy)
        print("Your turn:")

        for idx, card_name in enumerate(self.player.hand):
            card = get_card(card_name)

            print(f"{idx + 1}. {card}")

        card_to_play = None
        while card_to_play is None:
            user_input = input("Enter the number of the card you want to play, 'discard', or 'pass': ")
            if user_input.lower() == "pass":
                print("You chose to pass your turn.")
                self.current_turn = self.enemy
                break
            elif user_input.lower() == 'discard':
                self.discard_card_prompt()
                continue
            try:
                card_choice = int(user_input) - 1
                if 0 <= card_choice < len(self.player.hand):
                    card_name_to_play = self.player.hand[card_choice]
                    card_to_play = get_card(card_name_to_play)
                    if self.player.deck.count_cards(card_to_play.name) > 0:  # Check if the card is still available in the deck
                        if self.player.pips >= card_to_play.cost:
                            self.target = self.enemy  # Sets the players target to the enemy | Needs updating for multiple enemies
                            self.player.play_card(card_to_play, self)
                            self.current_turn = self.enemy
                        else:
                            print(
                                f"{card_to_play.name} costs {card_to_play.cost} pips, you have {self.player.pips} pips. Choose another card or pass.")
                            card_to_play = None
                    else:
                        print(f"You have no more {card_to_play.name} cards in your deck.")
                        card_to_play = None
            except ValueError:
                print("Invalid card number. Choose a valid card or pass.")


    def enemy_turn(self):
        print("Enemy's turn.")
        card_name_to_play = self.enemy.choose_card(self.enemy.pips)
        card_played = False
        while not card_played:
            if card_name_to_play:
                card_to_play = get_card(card_name_to_play)  # Get card object from name
                if self.enemy.pips >= card_to_play.cost:
                    self.target = self.player  # The target during the enemy's turn is the player.
                    self.enemy.play_card(card_to_play, self)  # Pass card object, not name
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

    def discard_card_prompt(self):
        print("\nSelect a card to discard:")
        for idx, card_name in enumerate(self.player.hand):
            card = get_card(card_name)
            print(f"{idx + 1}. {card}")


        while True:
            discard_choice = input("Enter the number of the card to discard or 'cancel' to return: ")
            if discard_choice.lower() == 'cancel':
                break
            discard_index = int(discard_choice) - 1
            if 0 <= discard_index < len(self.player.hand):
                card_name_to_discard = self.player.hand[discard_index]
                self.player.discard_card(card_name_to_discard)  # Assuming this method only removes the card
                for idx, card_name in enumerate(self.player.hand):
                    card = get_card(card_name)
                    print(f"{idx + 1}. {card}")
                break
            else:
                print("Invalid choice. Please select a valid card number or 'cancel'.")

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
