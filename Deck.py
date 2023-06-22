import random

import cards
from cards import *


class Deck:
    HAND_SIZE = 7

    def __init__(self, max_size, max_copies):
        self.cards = {}
        self.treasure_cards = []
        self.current_hand = []
        self.discard_pile = []
        self.max_size = max_size
        self.max_copies = max_copies

    def add_card(self, card):
        total_cards = sum(self.cards.values())
        if total_cards < self.max_size:
            # Check if the card has not exceeded max copy count
            copy_count = self.cards.get(card.name, 0)
            if copy_count < self.max_copies:
                self.cards[card.name] = copy_count + 1
                return True
        return False

    def remove_card(self, card):
        if card.name in self.cards:
            self.cards[card.name] -= 1
            if self.cards[card.name] == 0:
                del self.cards[card.name]
            return True
        return False

    def add_treasure_card(self, card):
        self.treasure_cards.append(card)

    def remove_treasure_card(self, card):
        if card in self.treasure_cards:
            self.treasure_cards.remove(card)
            return True
        return False

    def equip(self):
        # Shuffle the deck
        self.shuffle()
        # Draw the initial hand
        self.draw_cards(self.HAND_SIZE)

    def draw_cards(self, count):
        for _ in range(count):
            if not self.shuffled_cards:
                self.shuffled_cards, self.discard_pile = self.discard_pile, []
                self.shuffle()
                if not self.shuffled_cards:
                    return False
            card = self.shuffled_cards.pop(0)
            self.current_hand.append(card)
        return True

    def discard_card(self, card):
        if card in self.current_hand:
            self.current_hand.remove(card)
            self.discard_pile.append(card)
            # Draw card after discarding a card
            self.draw_cards(1)
            return True
        return False

    def draw_treasure_card(self):
        if self.treasure_cards:
            treasure_card = self.treasure_cards.pop(0)
            self.current_hand.append(treasure_card)

    def refresh_hand(self):
        # Discard the current hand
        self.discard_pile.extend(self.current_hand)
        self.current_hand = []
        # Refill the deck with the discard pile
        self.cards.extend(self.discard_pile)
        self.discard_pile = []
        # Shuffle the deck
        self.shuffle()
        # Draw a new hand
        self.draw_cards(self.HAND_SIZE)

    def count_cards(self, card):
        return sum(1 for c in self.cards if c == card)

    def shuffle(self):
        card_pool = [card for card, count in self.cards.items() for _ in range(count)]
        random.shuffle(card_pool)
        self.shuffled_cards = card_pool

    def draw(self):
        if not self.shuffled_cards:
            return None

        drawn_card_name = self.shuffled_cards.pop(0)
        self.cards[drawn_card_name] -= 1
        if self.cards[drawn_card_name] == 0:
            del self.cards[drawn_card_name]
        self.discard_pile.append(drawn_card_name)  # Add the drawn card name to the discard pile

        return drawn_card_name

    def __len__(self):
        return len(self.cards)

    def get_card_by_name(self, name):
        for card in self.cards:
            if card.name == name:
                return card
        return None


def create_deck(deck_data, max_size, max_copies):
    deck = Deck(max_size=max_size, max_copies=max_copies)
    for card_name, quantity in deck_data.items():
        card = cards.__dict__[card_name]
        for _ in range(quantity):
            deck.add_card(card)
    deck.equip()
    return deck




starter_deck_data = {
    'fire_cat': 3,
    'sunbird': 1,
    'frost_beetle': 1,
    'thunder_snake': 2,
    'lightning_bats': 1,
    'storm_shark': 1,
    'tempest': 1,

}
golem_deck_data = {
    'frost_beetle': 2,
    'snow_serpent': 1,
    'evil_snowman': 1,
    'fire_cat': 2,
    'fire_elf': 1,
    'sunbird': 1,
    'thunder_snake': 2,
}

starter_deck = create_deck(starter_deck_data, max_size=30, max_copies=4)
golem_deck = create_deck(golem_deck_data, max_size=30, max_copies=4)

for card, count in starter_deck_data.items():
    for _ in range(count):
        starter_deck.add_card(cards.__dict__[card])