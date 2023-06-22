class Card:
    def __init__(self, name, image_path, school, cost, effect):
        self.name = name
        self.image_path = image_path
        self.school = school
        self.cost = cost
        self.effect = effect




class Spell(Card):
    def __init__(self, name, school, cost, accuracy, damage, description, image_path, card_type, effect):
        super().__init__(name, image_path, school, cost, effect)
        self.name = name
        self.school = school
        self.cost = cost
        self.accuracy = accuracy
        self.damage = damage
        self.description = description
        self.image_path = image_path
        self.card_type = card_type
        self.effect = effect

    @staticmethod
    def damage_effect(target, damage):
       target.take_damage(damage)

    def apply_effect(self, target):
        target.take_damage(self.damage)

    def __str__(self):
        return f"{self.name} ({self.school}): Cost={self.cost}, Damage={self.damage}, Accuracy={self.accuracy}"



    def get_cost(self):
        return self.cost


class Item:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def use(self, target):
        self.effect(target)


class Treasure(Card):
    def __init__(self, name, description, value, damage_bonus=15):
        super().__init__(name, "Treasure", description)
        self.value = value
        self.damage_bonus = damage_bonus  # bonus damage compared to regular cards

    def use(self, target):
        """
        Use the treasure card, dealing damage to the target and then removing it from the player's hand.
        """
        target.take_damage(self.value + self.damage_bonus)
        # TODO: remove the card from the player's hand


class Pet(Card):
    def __init__(self, name, description, pet_type):
        super().__init__(name, "Pet", description)
        self.pet_type = pet_type
        # WIP


class Minion(Card):
    def __init__(self, name, description, minion_type):
        super().__init__(name, "Minion", description)
        self.minion_type = minion_type
        # WIP


class Blade(Card):
    def __init__(self, name, description, damage_boost):
        super().__init__(name, "Blade", description)
        self.damage_boost = damage_boost

    def use(self, player, enemy):
        player.add_damage_boost(self.damage_boost)


class Trap(Card):
    def __init__(self, name, description, damage_multiplier):
        super().__init__(name, "Trap", description)
        self.damage_multiplier = damage_multiplier
        self.target = None

    def set_target(self, target):
        self.target = target

    def use(self):
        if self.target:
            self.target.take_damage(self.damage_multiplier * self.player.damage)
            self.target = None


class Aura(Card):
    def __init__(self, name, description, effect):
        super().__init__(name, "Aura", description)
        self.effect = effect
        # WIP


# # Define the card templates
# templates = [
#     Card('Firebolt', 'firebolt.png', 'spell', 2, 'Deal 100 damage to target'),
#     Card('Ice Shield', 'iceshield.png', 'spell', 1, 'Give the caster a shield that blocks 100 damage'),
#     Card('Stormblade', 'stormblade.png', 'blade', 0, 'Increase next attack by 30%'),
#     Card('Trap', 'trap.png', 'trap', 1, 'Reduce target enemy\'s resistance by 30%'),
#     # Add more card templates here
#
#
# ]
#
# # Generate many instances of the card templates
# cards = []
# for i in range(10):
#     for template in templates:
#         card = Card(template.name + str(i), template.image_path, template.school, template.cost, template.effect)
#         cards.append(card)
#
# # Print the generated cards
# for card in cards:
#     print(card.name, card.school, card.cost, card.effect)

# Spells for Fire class
fire_cat = Spell("Fire Cat", "Fire", 1, 100, 80, "Deals 80 Fire damage", "images/Fire_Cat.png", "single target", Spell.damage_effect)
fire_elf = Spell("Fire Elf", "Fire", 2, 100, 225, "Deals 225 Fire damage over 3 rounds", "images/Fire_Elf.png",
                 "single target", Spell.damage_effect)
sunbird = Spell("Sunbird", "Fire", 3, 100, 335, "Deals 335 Fire damage", "images/Sunbird.png", "single target", Spell.damage_effect)
helephant = Spell("Helephant", "Fire", 6, 100, 415, "Deals 660 Fire damage", "images/Helephant.png", "single target",
                  Spell.damage_effect)
# dragon = Spell("Dragon", "Fire", 10, 100, 510, "Deals 510 Fire damage", "images/Dragon.png", "single target", None)

# Spells for Ice class
frost_beetle = Spell("Frost Beetle", "Ice", 1, 100, 65, "Deals 65 Ice damage", "images/(Spell)_Frost_Beetle.png",
                     "single target", Spell.damage_effect)
snow_shield = Spell("Snow Shield", "Ice", 0, 100, 0, "Adds a 250 Ice shield to the caster",
                    "images/(Spell)_Snow_Shield.png", "self", None)
snow_serpent = Spell("Snow Serpent", "Ice", 2, 100, 160, "Deals 160 Ice damage", "images/(Spell)_Snow_Serpent.png",
                     "single target", Spell.damage_effect)
evil_snowman = Spell("Evil Snowman", "Ice", 3, 100, 265, "Deals 265 Ice damage", "images/(Spell)_Evil_Snowman.png",
                     "single target", Spell.damage_effect)
# frostbite = Spell("Frostbite", "Ice", 5, 100, 290, "Deals 290 Ice damage and reduces target's accuracy by 25%", "images/frostbite.png", "single target", None)
blizzard = Spell("Blizzard", "Ice", 4, 100, 290, "Deals 290 Ice damage to all enemies", "images/blizzard.png",
                 "all enemies", None)
# winters_revenge = Spell("Winter's Revenge", "Ice", 9, 100, 450, "Deals 450 Ice damage and stuns the target for 1 round", "images/winters_revenge.png", "single target", None)

# Spells for Storm class
thunder_snake = Spell("Thunder Snake", "Storm", 1, 100, 125, "Deals 125 Storm damage",
                      "images/(Spell)_Thunder_Snake.png", "single target", Spell.damage_effect)
storm_shield = Spell("Storm Shield", "Storm", 0, 100, 0, "Adds a 250 Storm shield to the caster",
                     "images/(Spell)_Storm_Shield.png", "self", None)
lightning_bats = Spell("Lightning Bats", "Storm", 2, 100, 250, "Deals 250 Storm damage",
                       "images/(Spell)_Lightning_Bats.png", "single target", Spell.damage_effect)
tempest = Spell("Tempest", "Storm", 4, 100, 345, "Deals 345 Storm damage to all enemies", "images/(Spell)_Tempest.png",
                "all enemies", None)
storm_shark = Spell("Storm Shark", "Storm", 3, 100, 400, "Deals 400 Storm damage", "images/(Spell)_Storm_Shark.png",
                    "single target", Spell.damage_effect)

# Spells for Myth class
# sprite = Spell("Sprite", "myth", 1, "Heals 300 health to the target", "single target")
# myth_shield = Spell("Myth Shield", "myth", 3, "Adds a 250 Myth shield to the caster", "self")
# minotaur = Spell("Minotaur", "myth", 5, "Deals 290 Myth damage and stuns the target for 1 round", "single target")
# orthrus = Spell("Orthrus", "myth", 7, "Deals 345 Myth damage to all enemies", "all enemies")
# medusa = Spell("Medusa", "myth", 9, "Deals 425 Myth damage and converts it to a healing effect for the caster",
#              "single target")


# Create a dictionary mapping card names to instances
card_instances = {
    "Fire Cat": fire_cat,
    "Fire Elf": fire_elf,
    "Sunbird": sunbird,
    "Helephant": helephant,
    "Frost Beetle": frost_beetle,
    "Snow Shield": snow_shield,
    "Snow Serpent": snow_serpent,
    "Evil Snowman": evil_snowman,
    "Blizzard": blizzard,
    "Thunder Snake": thunder_snake,
    "Storm Shield": storm_shield,
    "Lightning Bats": lightning_bats,
    "Tempest": tempest,
    "Storm Shark": storm_shark,
}

def get_card(card_name):
    return card_instances.get(card_name)