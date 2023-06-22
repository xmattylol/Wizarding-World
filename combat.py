# combat.py
from cards import *
from character import * 

class Turn:
    def __init__(self, player):
        self.player = player
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

class Action:
    def __init__(self, card, target):
        self.card = card
        self.target = target

class Board:
    def __init__(self):
        self.characters = []
        self.enemies = []
        self.obstacles = []

    def add_character(self, character):
        self.characters.append(character)

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

class Combat:
    def __init__(self, board):
        self.board = board
        self.current_turn = None
        self.is_over = False

    def start_turn(self, player):
        self.current_turn = Turn(player)

    def end_turn(self):
        self.current_turn = None

    def play_card(self, card, target):
        action = Action(card, target)
        self.current_turn.add_action(action)

    def use_ability(self, ability, target):
        action = Action(ability, target)
        self.current_turn.add_action(action)

    def resolve_turn(self):
        for action in self.current_turn.actions:
            if isinstance(action.card, Card):
                # Apply card effects
                target = action.target
                spell = action.spell
                damage = spell.damage
                damage_type = spell.damage_type
                target.take_damage(damage, damage_type)
                for effect in spell.effects:
                    effect.apply(target)
            #elif isinstance(action.card, Ability):
                # Apply ability effects
            #    pass

        # Resolve enemy actions
        for enemy in self.enemies:
            action = enemy.choose_action()
            if isinstance(action.card, Card):
                # Apply card effects
                target = action.target
                card = action.card
                damage = card.damage
                damage_type = card.damage_type
                target.take_damage(damage, damage_type)
                for effect in card.effects:
                    effect.apply(target)
            #elif isinstance(action.card, Ability):
            #    # Apply ability effects
            #    pass

        # Check for game over conditions
        if self.player.is_defeated():
            print("Game over: Player is defeated")
        elif all(enemy.is_defeated() for enemy in self.enemies):
            print("Game over: All enemies are defeated")

