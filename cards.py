import random

class Card:
    def __init__(self, name, image_path, school, cost, accuracy):
        self.name = name
        self.image_path = image_path
        self.school = school
        self.cost = cost
        #self.effect = effect
        self.accuracy = accuracy

    def get_cost(self):
        return self.cost

    def get_accuracy(self):
        return self.accuracy

    def check_accuracy(self):
        return random.random() <= self.accuracy

    def apply_effect(self, caster, target):
        raise NotImplementedError('apply_effect method should be implemented in derived class')

    def __str__(self):
        return f"{self.name} ({self.school}): Cost={self.cost}, Accuracy={self.accuracy}"

    # def apply_effect(self, caster, target):
    #     # Check accuracy before applying the effect
    #     if self.check_accuracy():
    #         self.apply_effect(caster, target)
    #     else:
    #         print(f"{self.name} fizzles!")





class Spell(Card):
    def __init__(self, name, school, cost, accuracy, damage, description, image_path, card_type, effect):
        super().__init__(name, image_path, school, cost, accuracy)
        self.effect = effect
        self.damage = damage
        self.description = description
        self.card_type = card_type

    # @staticmethod
    # def apply_effect(caster, target, damage):
    #     if caster.class_type in caster.damage_boosts:
    #         #damage += damage * caster.damage_boosts[caster.class_type] / 100
    #         caster.use_damage_boost(caster.class_type, damage)  # Use the damage boost
    #     target.take_damage(damage)  # Apply damage to the target
    #
    # def damage_effect(self, caster, target):
    #     damage = self.damage
    #     # Apply damage boost if it exists for the spell's school
    #     if self.school in caster.damage_boosts:
    #         damage += damage * caster.damage_boosts[self.school] / 100
    #         caster.use_damage_boost(self.school)  # Use the damage boost
    #     target.take_damage(damage)  # Apply damage to the target
    def apply_effect(self, caster, target=None, boosted_damage=None):
        damage = self.damage
        if self.school in caster.damage_boosts:
            damage += damage * caster.damage_boosts[self.school] / 100
            caster.use_damage_boost(self.school, damage)  # Use the damage boost
        target.take_damage(damage)  # Apply damage to the target


    def __str__(self):
        return f"{self.name} ({self.school}): Cost={self.cost}, Damage={self.damage}, Accuracy={self.accuracy}"

    # not sure if this is needed
    # def effect(self, caster, target):
    #     if self.check_accuracy():
    #         damage = self.damage
    #         # Apply damage boost if it exists for the spell's school
    #         if self.school in caster.damage_boosts:
    #             damage += damage * caster.damage_boosts[self.school] / 100
    #             caster.use_damage_boost(self.school)  # Use the damage boost
    #         caster.target.take_damage(damage)  # Apply damage to the target
    #     else:
    #         print(f"{self.name} fizzles!")





class Blade(Card):
    def __init__(self, name, image_path, school, cost, damage_boost, accuracy):
        super().__init__(name, image_path, school, cost, accuracy)
        self.damage_boost = damage_boost

    def __str__(self):
        return f"{self.name}: Cost={self.cost}, Damage Boost={self.damage_boost}%, Accuracy={self.accuracy}"

    def apply_effect(self, caster, target=None):
        if self.check_accuracy():
            caster.add_damage_boost(self.school, self.damage_boost)
        else:
            print(f"{self.name} fizzles!")





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
fire_cat = Spell("Fire Cat", "Fire", 1, .75, 80, "Deals 80 Fire damage", "images/Fire_Cat.png", "single target", None)
fire_elf = Spell("Fire Elf", "Fire", 2, .75, 225, "Deals 225 Fire damage over 3 rounds [WIP]", "images/Fire_Elf.png",
                 "single target", None)
sunbird = Spell("Sunbird", "Fire", 3, .75, 335, "Deals 335 Fire damage", "images/Sunbird.png", "single target", None)
helephant = Spell("Helephant", "Fire", 6, .75, 660, "Deals 660 Fire damage", "images/Helephant.png", "single target",
                  None)
# dragon = Spell("Dragon", "Fire", 10, 100, 510, "Deals 510 Fire damage", "images/Dragon.png", "single target", None)

# Spells for Ice class
frost_beetle = Spell("Frost Beetle", "Ice", 1, .80, 65, "Deals 65 Ice damage", "images/(Spell)_Frost_Beetle.png",
                     "single target", None)
snow_shield = Spell("Snow Shield", "Ice", 0, .100, 0, "Adds a 250 Ice shield to the caster",
                    "images/(Spell)_Snow_Shield.png", "self", None)
snow_serpent = Spell("Snow Serpent", "Ice", 2, .80, 160, "Deals 160 Ice damage", "images/(Spell)_Snow_Serpent.png",
                     "single target", None)
evil_snowman = Spell("Evil Snowman", "Ice", 3, .80, 265, "Deals 265 Ice damage", "images/(Spell)_Evil_Snowman.png",
                     "single target", None)
# frostbite = Spell("Frostbite", "Ice", 5, 100, 290, "Deals 290 Ice damage and reduces target's accuracy by 25%", "images/frostbite.png", "single target", None)
blizzard = Spell("Blizzard", "Ice", 4, .80, 290, "Deals 290 Ice damage to all enemies", "images/blizzard.png",
                 "all enemies", None)
# winters_revenge = Spell("Winter's Revenge", "Ice", 9, 100, 450, "Deals 450 Ice damage and stuns the target for 1 round", "images/winters_revenge.png", "single target", None)

# Spells for Storm class
thunder_snake = Spell("Thunder Snake", "Storm", 1, .70, 125, "Deals 125 Storm damage",
                      "images/(Spell)_Thunder_Snake.png", "single target", None)
storm_shield = Spell("Storm Shield", "Storm", 0, .100, 0, "Adds a 250 Storm shield to the caster",
                     "images/(Spell)_Storm_Shield.png", "self", None)
lightning_bats = Spell("Lightning Bats", "Storm", 2, .70, 250, "Deals 250 Storm damage",
                       "images/(Spell)_Lightning_Bats.png", "single target", None)
tempest = Spell("Tempest", "Storm", 4, .70, 345, "Deals 345 Storm damage to all enemies", "images/(Spell)_Tempest.png",
                "all enemies", None)
storm_shark = Spell("Storm Shark", "Storm", 3, .70, 400, "Deals 400 Storm damage", "images/(Spell)_Storm_Shark.png",
                    "single target", None)

# Spells for Myth class
#sprite = Spell("Sprite", "myth", 1, "Heals 300 health to the target", "single target")
# myth_shield = Spell("Myth Shield", "myth", 3, "Adds a 250 Myth shield to the caster", "self")
blood_bat = Spell("Blood Bat", "Myth", 1, .80, 110, "Deals 110 Myth damage", "images/(Spell)_Blood_Bat.png",
                  "single target", None)
troll = Spell("Troll", "Myth", 2, .80, 210, "Deals 210 Myth damage", "images/(Spell)_Troll.png",
                  "single target", None)
cyclops = Spell("Troll", "Myth", 3, .80, 325, "Deals 325 Myth damage", "images/(Spell)_Cyclops.png",
                  "single target", None)
humongofrog = Spell("Humongofrog", "Myth", 4, .80, 325, "Deals 325 Myth damage to all enemies", "images/(Spell)_Humongofrog.png",
                  "all enemies", None)
# orthrus = Spell("Orthrus", "myth", 7, "Deals 345 Myth damage to all enemies", "all enemies")
# medusa = Spell("Medusa", "myth", 9, "Deals 425 Myth damage and converts it to a healing effect for the caster",
#              "single target")


# Spells for Death class
dark_sprite = Spell("Dark Sprite", "Death", 1, .85, 105, "Deals 105 Death damage", "images/(Spell)_Dark_Sprite.png",
                  "single target", None)
ghoul = Spell("Ghoul", "Death", 2, .85, 160, "Deals 160 Death drain damage and heals the caster for half the Damage dealt", "images/(Spell)_Ghoul.png",
                  "single target", None)
banshee = Spell("Banshee", "Death", 3, .85, 305, "Deals 305 Death damage", "images/(Spell)_Banshee.png",
                  "single target", None)
vampire = Spell("Vampire", "Death", 3, .85, 335, "Deals 335 Death drain damage", "images/(Spell)_Vampire.png",
                  "single target", None)
skeletal_pirate = Spell("Skeletal Pirate", "Death", 5, .85, 510, "Deals 510 Death damage", "images/(Spell)_Skeletal_Pirate.png",
                  "single target", None)

# Spells for Life class
imp = Spell("Imp", "Life", 1, .90, 105, "Deals 105 Life damage", "images/(Spell)_Imp.png",
                  "single target", None)
leprechaun = Spell("Leprechaun", "Life", 2, .90, 195, "Deals 195 Life damage", "images/(Spell)_Leprechaun.png",
                  "single target", None)
seraph = Spell("Seraph", "Life", 4, .90, 395, "Deals 395 Life damage", "images/(Spell)_Seraph.png",
                  "single target", None)
earth_walker = Spell("Earth Walker", "Life", 5, .90, 500, "Deals 500 Life damage", "images/(Spell)_Earth_Walker.png",
                  "single target", None)

# Spells for Balance class
scarab = Spell("Scarab", "Balance", 1, .85, 105, "Deals 105 Balance damage", "images/(Spell)_Scarab.png",
               "single target", None)
scorpion = Spell("Scorpion", "Balance", 2, .85, 200, "Deals 200 Balance damage", "images/(Spell)_Scorpion.png",
               "single target", None)
locust_swarm = Spell("Locust Swarm", "Balance", 3, .85, 305, "Deals 305 Balance damage", "images/(Spell)_Locust_Swarm.png",
               "single target", None)
sandstorm = Spell("Sandstorm", "Balance", 4, .85, 295, "Deals 295 Balance damage to all enemies", "images/(Spell)_Sandstorm.png",
               "single target", None)


# Blades & Traps
storm_blade = Blade(name="Storm Blade",
                    image_path="images/(Spell)_Stormblade)",
                    school="Storm",
                    cost=0,
                    damage_boost=0.30,
                    #effect=Blade.effect,
                    accuracy=1)

fire_blade = Blade(name="Fire Blade",
                   image_path="images/(Spell)_Fireblade.png",
                   school="Fire",
                   cost=0,
                   damage_boost=0.35,
                   #effect=Blade.effect,
                   accuracy=1)

ice_blade = Blade(name="Ice Blade",
                  image_path="images/(Spell)_Iceblade",
                  school="Ice",
                  cost=0,
                  damage_boost=0.35,
                  #effect=Blade.effect,
                  accuracy=1)

life_blade = Blade(name="Life Blade",
                  image_path="images/(Spell)_Lifeblade",
                  school="Life",
                  cost=0,
                  damage_boost=0.35,
                  #effect=Blade.effect,
                  accuracy=1)

myth_blade = Blade(name="Myth Blade",
                  image_path="images/(Spell)_Myth",
                  school="Myth",
                  cost=0,
                  damage_boost=0.35,
                  #effect=Blade.effect,
                  accuracy=1)

death_blade = Blade(name="Death Blade",
                  image_path="images/(Spell)_Deathblade",
                  school="Death",
                  cost=0,
                  damage_boost=0.35,
                  #effect=Blade.effect,
                  accuracy=1)


# Create a dictionary mapping card names to instances
card_instances = {
    # Fire Cards:
    "Fire Cat": fire_cat,
    "Fire Elf": fire_elf,
    "Sunbird": sunbird,
    "Helephant": helephant,

    # Ice Cards:
    "Frost Beetle": frost_beetle,
    "Snow Shield": snow_shield,
    "Snow Serpent": snow_serpent,
    "Evil Snowman": evil_snowman,
    "Blizzard": blizzard,

    # Storm Cards:
    "Thunder Snake": thunder_snake,
    "Storm Shield": storm_shield,
    "Lightning Bats": lightning_bats,
    "Tempest": tempest,
    "Storm Shark": storm_shark,

    # Myth Cards:
    "Blood Bat": blood_bat,
    "Troll": troll,
    "Cyclops": cyclops,
    "Humongofrog": humongofrog,

    # Death Cards:
    "Dark Sprite": dark_sprite,
    "Ghoul": ghoul,
    "Banshee": banshee,
    "Vampire": vampire,
    "Skeletal Pirate": skeletal_pirate,

    # Life Cards:
    "Imp": imp,
    "Leprechaun": leprechaun,
    "Seraph": seraph,
    "Earth Walker": earth_walker,

    # Balance Cards:
    "Scarab": scarab,
    "Scorpion": scorpion,
    "Locust Swarm": locust_swarm,
    "Sandstorm": sandstorm,

    # Blade & Trap Cards:
    "Storm Blade": storm_blade,
    "Ice Blade": ice_blade,
    "Fire Blade": fire_blade,
    "Life Blade": life_blade,
    "Myth Blade": myth_blade,
    "Death Blade": death_blade

}

def get_card(card_name):
    return card_instances.get(card_name)


