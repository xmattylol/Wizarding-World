import random
#import main
from cards import *


class Character:
    def __init__(self, name, class_type, max_health, max_mana, deck):
        self.name = name
        self.class_type = class_type
        self.max_health = max_health
        self.health = max_health
        self.max_mana = max_mana
        self.mana = max_mana
        self.deck = deck
        self.hand = deck.current_hand
        self.pips = 0

    def __str__(self):
        return f"{self.name} ({self.class_type}): Health={self.health}, Mana={self.mana}, Pips={self.pips}"

    def take_damage(self, damage):
        self.health -= damage
        self.health = max(0, self.health)  # Health should not go below 0

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def restore_mana(self, amount):
        self.mana += amount
        if self.mana > self.max_mana:
            self.mana = self.max_mana

    def draw_card(self):
        if len(self.deck) > 0:
            return self.deck.pop(0)
        else:
            return None

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def is_defeated(self):
        return self.health == 0

    def play_card(self, card, target):
        card_cost = card.get_cost()
        if self.pips >= card_cost:
            self.pips -= card_cost
            self.mana -= card_cost
            print(f"Card played: {card.name}")
            print(f"{self.name} used {card.name} and dealt {card.damage} damage!")
            card.effect(target, card.damage)  # Pass the card's damage to the effect
            self.deck.discard_card(card)  # Discard the played card
            self.hand.remove(card.name)  # Remove the played card from the hand
            new_card = self.deck.draw()  # Draw a new card
            if new_card:
                self.hand.append(new_card)  # Add the new card to the hand
        else:
            print("Not enough pips to play this card!")


    def discard_card(self, card):
        self.deck.append(card)

    def get_info(self):
        info = "Name: {}\nClass: {}\nHealth: {}/{}\nMana: {}/{}\n".format(
            self.name, self.class_type, self.health, self.max_health, self.mana, self.max_mana)
        return info

    # def display_stats(self, screen, font):
    #     # Display character health
    #     health_text = font.render("Health: {}/{}".format(self.health, self.max_health), True, (255, 255, 255))
    #     health_pos = (20, screen.get_height() - 50)
    #     screen.blit(health_text, health_pos)
    #
    #     # Display character mana
    #     mana_text = font.render("Mana: {}/{}".format(self.mana, self.max_mana), True, (255, 255, 255))
    #     mana_pos = (20, screen.get_height() - 30)
    #     screen.blit(mana_text, mana_pos)


    # def display_hand(self, screen, hand):
    #
    #     padding = 10
    #     x = padding
    #     y = screen.get_height() - card_height - padding
    #
    #     for card in hand:
    #         card_image = pygame.image.load(card.image_path)
    #         card_image = pygame.transform.scale(card_image, (card_width, card_height))
    #         screen.blit(card_image, (x, y))
    #         x += card_width + padding
    #
    # def is_mouse_over_card(self, mouse_pos, card_rect):
    #     return card_rect.collidepoint(mouse_pos)
    #
    # def choose_card(self, mouse_pos):
    #     for idx, card in enumerate(self.hand):
    #         card_rect = card.image.get_rect()
    #         card_rect.topleft = (50 + idx * (card_width + 20), main.screen_height - card_height - 50)
    #
    #         if self.is_mouse_over_card(mouse_pos, card_rect):
    #             return card
    #
    #     return None



#
# class StormCharacter(Character):
#     def __init__(self, name):
#         super().__init__(name, max_health=100, max_mana=50)
#         self.storm_damage = 20
#         self.deck = [cards.Spell("Lightning Bolt", "Deals {} storm damage".format(self.storm_damage), self.storm_damage)]
#
#
# class FireCharacter(Character):
#     def __init__(self, name):
#         super().__init__(name, max_health=120, max_mana=40)
#         self.fire_damage = 15
#         self.deck = [cards.Spell("Fireball", "Deals {} fire damage".format(self.fire_damage), self.fire_damage)]


# class Party:
#     def __init__(self):
#         self.characters = []
#
#     def add_character(self, character):
#         self.characters.append(character)
#
#     def remove_character(self, character):
#         self.characters.remove(character)
#
#     def get_character_names(self):
#         return [c.name for c in self.characters]


