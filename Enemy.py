import random
import cards
class Enemy:
    def __init__(self, name, max_health, attack_power, deck, class_type):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack_power = attack_power
        self.deck = deck
        self.class_type = class_type
        self.hand = deck.current_hand
        self.pips = 0

    def __str__(self):
        return f"{self.name} ({self.class_type}): Health={self.health}, Pips={self.pips}"

    def attack(self, target):
        target.take_damage(self.attack_power)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def display_stats(self, screen, font):
        # Display enemy health
        health_text = font.render("Health: {}/{}".format(self.health, self.max_health), True, (255, 255, 255))
        health_pos = (20, 20)
        screen.blit(health_text, health_pos)

    def choose_card(self, available_pips):
        valid_card_names = [card_name for card_name in self.hand if
                            cards.get_card(card_name).cost <= available_pips and self.hand.count(card_name) > 0]
        if valid_card_names:
            return random.choice(valid_card_names)
        else:
            return None

    def play_card(self, card, target):
        if self.pips >= card.cost:
            self.pips -= card.cost
            card.effect(target, card.damage)
            self.hand.remove(card.name)  # Use card.name instead of card
            print(f"{self.name} used {card.name} and dealt {card.damage} damage!")
            new_card = self.deck.draw()  # Draw a new card
            if new_card:
                self.hand.append(new_card)  # Add the new card to the hand
            return True
        else:
            print(f"{self.name} does not have enough pips to use {card.name}.")
            return False

    def is_defeated(self):
        return self.health <= 0
