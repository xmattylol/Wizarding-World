import random
import cards
from cards import *
from Animation import Animation

class Enemy:
    def __init__(self, name, max_health, attack_power, deck, class_type, sprite_sheet_path, sprite_size, num_frames):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack_power = attack_power
        self.deck = deck
        self.class_type = class_type
        self.hand = deck.current_hand
        self.pips = 0

        # Animation attributes
        self.sprite_sheet_path = sprite_sheet_path
        self.sprite_size = sprite_size
        self.num_frames = num_frames
        self.animation = Animation(
            sprite_sheet_path=self.sprite_sheet_path,
            sprite_size=self.sprite_size,
            num_frames=self.num_frames,
            loop=True
        )

        self.damage_boosts = {
            'Storm': 0,
            'Ice': 0,
            'Fire': 0,
            'Death': 0,
            'Myth': 0,
            'Life': 0,
            'Balance': 0
        }


    def __str__(self):
        return f"{self.name} ({self.class_type}): Health={self.health}, Pips={self.pips}"

    def attack(self, target):
        target.take_damage(self.attack_power)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def add_damage_boost(self, school, boost):
        if school == 'Balance':
            for school in self.damage_boosts.keys():
                self.damage_boosts[school] += boost
        else:
            self.damage_boosts[school] += boost

    def use_damage_boost(self, school, base_damage):
        boost = self.damage_boosts[school]
        boosted_damage = base_damage * (1 + boost/100)
        # Consume the damage boost
        self.damage_boosts[school] = 0
        return boosted_damage

    def display_stats(self, screen, font):
        # Display enemy health
        health_text = font.render("Health: {}/{}".format(self.health, self.max_health), True, (255, 255, 255))
        health_pos = (20, 20)
        screen.blit(health_text, health_pos)

    def display(self, screen, position):
        """ Display the enemy on the screen with the current frame of the animation """
        self.animation.draw(screen, position)

    def update_animation(self, dt):
        """ Update the animation frame as per the delta time """
        self.animation.update(dt)


    def choose_card(self, available_pips):
        valid_card_names = [card_name for card_name in self.hand if
                            cards.get_card(card_name).cost <= available_pips and self.hand.count(card_name) > 0]
        if valid_card_names:
            return random.choice(valid_card_names)
        else:
            return None

    def play_card(self, card, combat_instance):
        if self.pips >= card.cost:
            if card.check_accuracy():  # If card doesn't fizzle:
                # print(f"Accuracy tested against: {accuracy} | Card accuracy: {card.get_accuracy()}") # for debug

                if isinstance(card, Spell):  # If Spell
                    # Use and consume any applicable damage boost
                    boosted_damage = self.use_damage_boost(card.school, card.damage)
                    print(f"{self.name} used {card.name} and dealt {boosted_damage} damage!")
                    card.apply_effect(self, combat_instance.target, boosted_damage)  # Pass the card's damage to the effect

                elif isinstance(card, Blade):  # If Blade
                    print(f"{self.name} used {card.name} and applied a blade!")
                    card.apply_effect(self)  # Pass only the caster to blade's effect

                self.pips -= card.cost
            else:
                print(f"{self.name} fizzled!")
            self.hand.remove(card.name)  # Use card.name instead of card
            new_card = self.deck.draw()  # Draw a new card
            if new_card:
                self.hand.append(new_card)  # Add the new card to the hand
            return True
        else:
            print(f"{self.name} does not have enough pips to use {card.name}.")
            return False

    def is_defeated(self):
        return self.health <= 0
