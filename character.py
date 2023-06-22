import random
#import main
from cards import *


class Character:
    def __init__(self, name, max_health, max_mana, deck, power_pip_percentage, learned_spells):
        self.name = name
        #self.class_type = class_type
        self.max_health = max_health
        self.health = max_health
        self.max_mana = max_mana
        self.mana = max_mana
        self.deck = deck
        self.hand = deck.current_hand
        self.pips = 0
        self.power_pip_percentage = power_pip_percentage
        self.learned_spells = learned_spells

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

    # def play_card(self, card, target):
    #     card_cost = card.get_cost()
    #     if self.pips >= card_cost:
    #         self.pips -= card_cost
    #         self.mana -= card_cost
    #         print(f"Card played: {card.name}")
    #         print(f"{self.name} used {card.name} and dealt {card.damage} damage!")
    #         card.effect(target, card.damage)  # Pass the card's damage to the effect
    #         self.deck.discard_card(card)  # Discard the played card
    #         self.hand.remove(card.name)  # Remove the played card from the hand
    #         new_card = self.deck.draw()  # Draw a new card
    #         if new_card:
    #             self.hand.append(new_card)  # Add the new card to the hand
    #     else:
    #         print("Not enough pips to play this card!")
    def play_card(self, card, target):
        card_cost = card.get_cost()
        if self.pips >= card_cost:
            self.mana -= card_cost
            print(f"Card played: {card.name}")
            accuracy = random.random()  # Returns a random float between 0 and 1
            if accuracy <= card.get_accuracy():  # Assuming card has an accuracy attribute
                print(f"Accuracy tested against: {accuracy} | Card accuracy: {card.get_accuracy()}")
                print(f"{self.name} used {card.name} and dealt {card.damage} damage!")
                self.pips -= card_cost
                card.effect(target, card.damage)  # Pass the card's damage to the effect
            else:
                print(f"{self.name} fizzled!")
            self.deck.discard_card(card)  # Discard the played card
            self.hand.remove(card.name)  # Remove the played card from the hand
            new_card = self.deck.draw()  # Draw a new card
            if new_card:
                self.hand.append(new_card)  # Add the new card to the hand
        else:
            print("Not enough pips to play this card!")


    def discard_card(self, card):
        self.deck.append(card)

    def generate_power_pip(self):
        return random.random(0, 1) < self.power_pip_percentage

    def learn_spell(self, spell):
        self.learned_spells.append(spell)

    def forget_spell(self, spell):
        self.learned_spells.remove(spell)

    def cast_spell(accuracy):
        return random.random() <= accuracy / 100

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




    def __str__(self):
        return f"{self.name} ({self.class_type}): Health={self.health}, Mana={self.mana}, Pips={self.pips}"

class Storm(Character):
    def __init__(self, name, max_health, max_mana, deck, power_pip_percentage, learned_spells):
        super().__init__(name, max_health, max_mana, deck, power_pip_percentage, learned_spells)
        self.learned_spells.append('Thunder Snake')  # Example starter spell for Storm
    class_type = 'Storm'

class Fire(Character):
    def __init__(self, name, max_health, max_mana, deck, power_pip_percentage, learned_spells):
        super().__init__(name, max_health, max_mana, deck, power_pip_percentage, learned_spells)
        self.learned_spells.append('Fire Cat')  # Example starter spell for Fire
    class_type = 'Fire'

class Ice(Character):
    def __init__(self, name, max_health, max_mana, deck, power_pip_percentage, learned_spells):
        super().__init__(name, max_health, max_mana, deck, power_pip_percentage, learned_spells)
        self.learned_spells.append('Frost Beetle')
    class_type = 'Ice'

class Myth(Character):
    def __init__(self, name, max_health, max_mana, deck, power_pip_percentage, learned_spells):
        super().__init__(name, max_health, max_mana, deck, power_pip_percentage, learned_spells)
        self.learned_spells.append('Blood Bat')
    class_type = 'Myth'

class Death(Character):
    def __init__(self, name, max_health, max_mana, deck, power_pip_percentage, learned_spells):
        super().__init__(name, max_health, max_mana, deck, power_pip_percentage, learned_spells)
        self.learned_spells.append('Dark Sprite')
    class_type = 'Death'

class Life(Character):
    def __init__(self, name, max_health, max_mana, deck, power_pip_percentage, learned_spells):
        super().__init__(name, max_health, max_mana, deck, power_pip_percentage, learned_spells)
        self.learned_spells.append('Imp')
    class_type = 'Life'

class Balance(Character):
    def __init__(self, name, max_health, max_mana, deck, power_pip_percentage, learned_spells):
        super().__init__(name, max_health, max_mana, deck, power_pip_percentage, learned_spells)
        self.learned_spells.append('Scarab')
    class_type = 'Balance'
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


