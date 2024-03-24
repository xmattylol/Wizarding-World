import random

from Animation import *
from cards import *


class Character:
    def __init__(self, name, class_type, max_health, max_mana, deck, power_pip_percentage, learned_spells, sprite_sheet, sprite_size, num_frames):
        self.name = name
        self.class_type = class_type
        self.max_health = max_health
        self.health = max_health
        self.max_mana = max_mana
        self.mana = max_mana
        self.deck = deck
        self.hand = deck.current_hand
        self.pips = 0
        self.power_pip_percentage = power_pip_percentage
        self.learned_spells = learned_spells
        # Animation
        # Note: You would replace these parameter values as needed
        self.animation = Animation(sprite_sheet, sprite_size, num_frames, [200] * num_frames, loop=True)
        self.rect = pygame.Rect(100, 100, sprite_size[0], sprite_size[1])
        self.speed = 1

        self.damage_boosts = {
            'Storm': 0,
            'Ice': 0,
            'Fire': 0,
            'Death': 0,
            'Myth': 0,
            'Life': 0,
            'Balance': 0
        }

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

    def add_damage_boost(self, school, boost):
        self.damage_boosts[school] += boost

    def use_damage_boost(self, school, base_damage):
        boost = self.damage_boosts[school]
        boosted_damage = base_damage * (1 + boost/100)
        # Consume the damage boost
        self.damage_boosts[school] = 0
        return boosted_damage

    def draw_card(self):
        return self.deck.draw()


    def shuffle_deck(self):
        self.deck.shuffle()

    def is_defeated(self):
        return self.health <= 0

    def play_card(self, card, combat_instance):
        card_cost = card.get_cost()
        if self.pips >= card_cost:
            self.mana -= card_cost
            print(f"Card played: {card.name}")
            if card.check_accuracy():  # If card doesn't fizzle:
                #print(f"Accuracy tested against: {accuracy} | Card accuracy: {card.get_accuracy()}") # for debug

                if isinstance(card, Spell):  # If Spell
                    # Use and consume any applicable damage boost
                    boosted_damage = self.use_damage_boost(card.school, card.damage)
                    print(f"{self.name} used {card.name} and dealt {boosted_damage} damage!")
                    card.apply_effect(self, combat_instance.target, boosted_damage)  # Pass the card's damage to the effect

                elif isinstance(card, Blade):  # If Blade
                    print(f"{self.name} used {card.name} and applied a blade!")
                    card.apply_effect(self)  # Pass only the caster to blade's effect

                self.pips -= card_cost
            else:
                print(f"{self.name} fizzled!")
            self.deck.discard_card(card.name)  # Discard the played card
            self.hand.remove(card.name)  # Remove the played card from the hand
            new_card = self.deck.draw()  # Draw a new card
            if new_card:
                self.hand.append(new_card)  # Add the new card to the hand
            else:
                print(f"{self.name} does not have enough pips to use {card.name}.")


    def discard_card(self, card_name):
        """Discards a card from the character's hand."""
        if card_name in self.hand:
            self.hand.remove(card_name)  # Remove the card from the hand
            self.deck.discard_pile.append(card_name)  # Add the card to the discard pile
            print(f"Discarded card: {card_name}")
        else:
            print(f"Card '{card_name}' not found in hand.")

    def draw_up_to_seven_cards(self):
        while len(self.hand) < 7:
            new_card = self.deck.draw()
            if new_card:
                self.hand.append(new_card)
            else:
                break  # Break if no more cards can be drawn

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

    def update(self, dt):
        # Update animation
        self.animation.update(dt)

        # Check for player's stop state (e.g., no key presses)
        keys = pygame.key.get_pressed()
        if not (keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[
            pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s]):
            self.animation.stop()

    def draw(self, screen):
        self.animation.draw(screen, self.rect.topleft)

    def move(self, dx, dy):
        if dx > 0:  # Moving right
            self.animation.set_direction('right')
        elif dx < 0:  # Moving left
            self.animation.set_direction('left')

        # Assuming vertical movement doesn't require sprite flipping, but adjust as needed.
        # Update the character's position
        self.rect.x += dx
        self.rect.y += dy

        # If moving, play the animation
        if dx != 0 or dy != 0:
            self.animation.play()
        else:
            self.animation.stop()

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
        super().__init__(name, 'Storm', max_health, max_mana, deck, power_pip_percentage, learned_spells)
        self.learned_spells.append('Thunder Snake')  # Example starter spell for Storm

class Fire(Character):
    def __init__(self, name, max_health, max_mana, deck, power_pip_percentage, learned_spells):
        super().__init__(name, 'Fire', max_health, max_mana, deck, power_pip_percentage, learned_spells)
        self.learned_spells.append('Fire Cat')  # Example starter spell for Fire

class Ice(Character):
    def __init__(self, name, max_health, max_mana, deck, power_pip_percentage, learned_spells):
        super().__init__(name, 'Ice', max_health, max_mana, deck, power_pip_percentage, learned_spells)
        self.learned_spells.append('Frost Beetle')
#    class_type = 'Ice'

class Myth(Character):
    def __init__(self, name, max_health, max_mana, deck, power_pip_percentage, learned_spells):
        super().__init__(name, 'Myth', max_health, max_mana, deck, power_pip_percentage, learned_spells)
        self.learned_spells.append('Blood Bat')

class Death(Character):
    def __init__(self, name, max_health, max_mana, deck, power_pip_percentage, learned_spells):
        super().__init__(name, 'Death', max_health, max_mana, deck, power_pip_percentage, learned_spells)
        self.learned_spells.append('Dark Sprite')

class Life(Character):
    def __init__(self, name, max_health, max_mana, deck, power_pip_percentage, learned_spells):
        super().__init__(name, 'Life', max_health, max_mana, deck, power_pip_percentage, learned_spells)
        self.learned_spells.append('Imp')

class Balance(Character):
    def __init__(self, name, max_health, max_mana, deck, power_pip_percentage, learned_spells):
        super().__init__(name, 'Balance', max_health, max_mana, deck, power_pip_percentage, learned_spells)
        self.learned_spells.append('Scarab')


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


