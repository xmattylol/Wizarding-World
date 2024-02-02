import random
from Enemy import *
import Deck


class EnemyManager:
    def __init__(self, screen, enemy_templates):
        self.enemies = []
        self.screen = screen  # Store a reference to the screen where enemies will be drawn
        self.enemy_templates = enemy_templates  # Templates for spawning new enemies

    def spawn_enemy(self, template_name, x, y):
        template = self.enemy_templates[template_name]
        new_enemy = Enemy(
            name=template['name'],
            max_health=template['max_health'],
            attack_power=template['attack_power'],
            deck=template['deck'],
            class_type=template['class_type'],
            sprite_sheet_path=template['sprite_sheet_path'],
            sprite_size=template['sprite_size'],
            num_frames=template['num_frames'],
            frame_durations=template['frame_durations']
        )
        new_enemy.set_position(x, y)
        self.enemies.append(new_enemy)

    def remove_defeated(self):
        self.enemies = [enemy for enemy in self.enemies if not enemy.is_defeated()]

    def update_animation(self, dt):
        for enemy in self.enemies:
            if not enemy.is_defeated():
                enemy.update_animation(dt)

    def display_enemies(self, camera=None):
        for enemy in self.enemies:
            if not enemy.is_defeated():
                # Check if a camera is provided and adjust the enemy's position accordingly
                if not enemy.is_defeated():
                    #adjusted_rect = camera.apply(enemy.rect) if camera else enemy.rect
                    enemy.display(self.screen, enemy.rect.topleft)
                    #enemy.adjusted_rect = adjusted_rect  # Store for collision detection
    def get_active_enemies(self):
        """Get a list of all enemies that have not been defeated"""
        return [enemy for enemy in self.enemies if not enemy.is_defeated()]

    # Enemy templates example (you may expand this with actual data)
    enemy_templates = {
        'golem': {
            'name': 'Golem',
            'max_health': 100,
            'attack_power': 1,
            'deck': Deck.golem_deck,  # you need to define this
            'class_type': 'Myth',
            'sprite_sheet_path': 'images/SoliderAutomatonIdleSide.png',
            'sprite_size': (16, 16),
            'num_frames': 4,
            'frame_durations': [500, 500, 250, 500]
        },
        # ... additional enemy templates
    }

# Example of usage:
# (integrate this into main game loop and event handling structure)
# screen = None  # This should be your Pygame screen object
# enemy_manager = EnemyManager(screen, enemy_templates)
#
# # To spawn enemies:
# enemy_manager.spawn_enemy('golem', x=100, y=200)
# enemy_manager.spawn_enemy('golem', x=300, y=400)
#
# # In game loop, you would call:
# enemy_manager.update_animation(dt)
# enemy_manager.display_enemies()
