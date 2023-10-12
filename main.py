#
# TODO: Card types: Spell, Item, Treasure, pet, minion, blade, trap, aura, (maybe shadow)
#
# TODO: Character classes: Storm, Fire, Ice, Death, Life, Myth, Balance
#
# TODO: Combat Rules: turn-based and involve playing cards from
# a player's hand to deal damage or other effects to enemies.
# include rules for blocking enemy attacks, dodging attacks,
# and using card effects to heal or buff allies.
#
# TODO: Leveling Up: As players progress through the game and win battles,
# they earn XP that allow them to level up their characters.
# Leveling up could provide players with new cards, abilities, and bonuses to their stats.
#
# TODO: Quests: include quests for players to complete that involve battling enemies
# and collecting items. Completing quests could provide players with rewards like new cards, or experience points.
#
# TODO: Customizable Decks: Players could build their own decks from a pool of available cards.
# They could also customize their decks between battles to optimize their strategy based on their opponents.
#
#
#
#

import pygame

from pygame.locals import *
import sys
from character import *
import Deck
from Enemy import *
from EnemyManager import *
import text_based
from combat import *

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Window Setup
WIN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Wizard101-Inspired Card Game")

# Clock object
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)

# Instance of player
selected_class = text_based.class_menu()  # Get the selected class before starting the game loop

player = Character(
    name="Necromancer",
    class_type=selected_class,
    max_health=100,
    max_mana=100,
    deck=Deck.starter_deck, # You might pass a proper deck object here
    power_pip_percentage=0.1,
    learned_spells=[],
    sprite_sheet="images/AdeptNecromancerIdle.png",  # Providing the path from the "images" folder
    sprite_size=(16, 16),  # Assume each frame is 16 pixels
    num_frames=4  # Assume there are 4 frames in the sprite_sheet
)
enemy_manager = EnemyManager(WIN, EnemyManager.enemy_templates)

# golem = Enemy(
#     name="Golem",
#     max_health=100,
#     attack_power=1,
#     deck=Deck.golem_deck,
#     class_type="Myth",
#     sprite_sheet_path="images/SoliderAutomatonIdleSide.png",
#     sprite_size=(16, 16),  # Example size, adjust accordingly
#     num_frames=4  # Example frame number, adjust according to your spritesheet
# )

#golem.animation.play()  # Starting the animation
enemy_manager.spawn_enemy('golem', x=100, y=200)
enemy_manager.spawn_enemy('golem', x=300, y=400)

# Main game loop
running = True
while running:
    dt = clock.tick(60) / 1000  # Amount of seconds between each loop
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[K_ESCAPE]:
        running = False
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.move(-player.speed, 0)
        player.animation.set_direction('left')
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.move(player.speed, 0)
        player.animation.set_direction('right')
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.move(0, -player.speed)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.move(0, player.speed)

    for enemy in enemy_manager.get_active_enemies():
        if player.rect.colliderect(enemy.rect):
            print("Combat initiated!")
            combat = Combat(player, enemy)  # Pass the specific enemy instance to Combat
            combat.start()

    # Update
    player.update(dt)  # Pass elapsed time in seconds to handle animations

    # Draw/render
    WIN.fill(WHITE)  # Filling screen with white color
    player.draw(WIN)  # Draw player on the window at position (100, 100)

    # golem.update_animation(dt)  # Update golem animation
    # golem.display(WIN, (400, 300))  # Display golem at x=400, y=300
    # golem.animation.set_frame_durations([150, 150, 150, 150])
    # golem.animation.set_direction('left')

    enemy_manager.update_animation(dt)
    enemy_manager.display_enemies()
    pygame.display.flip()  # Updating the screen

# Clean up
pygame.quit()
sys.exit()


#
#
# def main_menu(screen):
#     # Create the menu font and text objects
#     font = pygame.font.SysFont("Arial", 50)
#     title_text = font.render("My Wizard101-Inspired Card Game", True, (255, 255, 255))
#     new_game_text = font.render("New Game", True, (255, 255, 255))
#     load_game_text = font.render("Load Game", True, (255, 255, 255))
#     settings_text = font.render("Settings", True, (255, 255, 255))
#
#     # Set the text positions
#     title_pos = title_text.get_rect(center=(screen_width / 2, 100))
#     new_game_pos = new_game_text.get_rect(center=(screen_width / 2, 250))
#     load_game_pos = load_game_text.get_rect(center=(screen_width / 2, 350))
#     settings_pos = settings_text.get_rect(center=(screen_width / 2, 450))
#
#     # Draw the text objects on the screen
#     screen.blit(title_text, title_pos)
#     screen.blit(new_game_text, new_game_pos)
#     screen.blit(load_game_text, load_game_pos)
#     screen.blit(settings_text, settings_pos)
#
#     # Update the display
#     pygame.display.update()
#
#     # Set up some variables for the settings menu
#     settings_options = [
#         {"text": "800x600", "size": (800, 600)},
#         {"text": "1024x768", "size": (1024, 768)},
#         {"text": "1280x720", "size": (1280, 720)},
#         {"text": "1920x1080", "size": (1920, 1080)}
#     ]
#     current_option = 0
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == MOUSEBUTTONDOWN:
#                 mouse_pos = pygame.mouse.get_pos()
#                 if new_game_pos.collidepoint(mouse_pos):
#                     # Start a new game and choose a character class
#                     class_options = [
#                         {"text": "Storm", "class": "Storm"},
#                         {"text": "Fire", "class": "Fire"},
#                         {"text": "Ice", "class": "Ice"},
#                         {"text": "Life", "class": "Life"},
#                         {"text": "Myth", "class": "Myth"},
#                         {"text": "Death", "class": "Death"},
#                         {"text": "Balance", "class": "Balance"}
#                     ]
#                     current_class = 0
#                     class_menu(font, class_options, current_class)
#                 elif load_game_pos.collidepoint(mouse_pos):
#                     # Load a saved game
#                     print("Loading saved game...")
#                 elif settings_pos.collidepoint(mouse_pos):
#                     # Open the settings menu
#                     current_option = settings_menu(font, settings_options, current_option, screen, screen_width)
#                     # Update the screen size
#                     screen_size = settings_options[current_option]["size"]
#                     screen = pygame.display.set_mode(screen_size)
#
#         # Display the main menu
#         screen.blit(title_text, title_pos)
#         screen.blit(new_game_text, new_game_pos)
#         screen.blit(load_game_text, load_game_pos)
#         screen.blit(settings_text, settings_pos)
#         pygame.display.update()
#
#
# def settings_menu(font, settings_options, current_option):
#     # Create the menu font and text objects
#     screen_width = settings_options[current_option]["size"][0]
#     screen_height = settings_options[current_option]["size"][1]
#     screen = pygame.display.set_mode((screen_width, screen_height))
#     title_text = font.render("Settings", True, (255, 255, 255))
#     back_text = font.render("Back", True, (255, 255, 255))
#     screen_text = font.render("Screen Size", True, (255, 255, 255))
#     size1_text = font.render("800x600", True, (255, 255, 255))
#     size2_text = font.render("1024x768", True, (255, 255, 255))
#     size3_text = font.render("1280x720", True, (255, 255, 255))
#     size4_text = font.render("1920x1080", True, (255, 255, 255))
#
#     # Set the text positions
#     title_pos = title_text.get_rect(center=(screen_width / 2, 100))
#     back_pos = back_text.get_rect(topright=(screen_width - 20, 20))
#     screen_pos = screen_text.get_rect(center=(screen_width / 2, 250))
#     size1_pos = size1_text.get_rect(center=(screen_width / 2, 300))
#     size2_pos = size2_text.get_rect(center=(screen_width / 2, 350))
#     size3_pos = size3_text.get_rect(center=(screen_width / 2, 400))
#     size4_pos = size4_text.get_rect(center=(screen_width / 2, 450))
#
#     # Draw the text objects on the screen
#     screen.blit(title_text, title_pos)
#     screen.blit(back_text, back_pos)
#     screen.blit(screen_text, screen_pos)
#     screen.blit(size1_text, size1_pos)
#     screen.blit(size2_text, size2_pos)
#     screen.blit(size3_text, size3_pos)
#     screen.blit(size4_text, size4_pos)
#
#     # Update the display
#     pygame.display.update()
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == MOUSEBUTTONDOWN:
#                 mouse_pos = pygame.mouse.get_pos()
#                 if back_pos.collidepoint(mouse_pos):
#                     return current_option
#
#                 # Set the screen size based on the button clicked
#                 if size1_pos.collidepoint(mouse_pos):
#                     current_option = 0
#                     screen_width, screen_height = settings_options[current_option]["size"]
#                     screen = pygame.display.set_mode((screen_width, screen_height))
#                 elif size2_pos.collidepoint(mouse_pos):
#                     current_option = 1
#                     screen_width, screen_height = settings_options[current_option]["size"]
#                     screen = pygame.display.set_mode((screen_width, screen_height))
#                 elif size3_pos.collidepoint(mouse_pos):
#                     screen_width = 1280
#                     screen_height = 720
#                     screen = pygame.display.set_mode((screen_width, screen_height))
#
#                 # Update the screen
#                 screen.fill((0, 0, 0))
#                 settings_menu(screen, screen_width, current_option)
#
#
# def class_menu(font, class_options, current_class):
#     # Set up the text for the class selection menu
#     title_text = font.render("Select a Character Class", True, (255, 255, 255))
#     title_pos = title_text.get_rect(center=(screen_width / 2, 100))
#     screen.blit(title_text, title_pos)
#
#     # Set up the text for each class option
#     class_text = [font.render(cls, True, (255, 255, 255)) for cls in class_options]
#     class_pos = [class_text[i].get_rect(center=(screen_width / 2, 200 + 50 * i)) for i in range(len(class_options))]
#
#     # Set up the text for the selected class
#     selected_text = font.render("Selected Class: {}".format(class_options[current_class]), True, (255, 255, 255))
#     selected_pos = selected_text.get_rect(center=(screen_width / 2, 400))
#
#     # Draw the class selection menu on the screen
#     for i in range(len(class_options)):
#         screen.blit(class_text[i], class_pos[i])
#     screen.blit(selected_text, selected_pos)
#
#     # Update the display
#     pygame.display.update()
#
#     # Wait for user input
#     while True:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     return current_class
#                 elif event.key == K_UP:
#                     current_class = (current_class - 1) % len(class_options)
#                 elif event.key == K_DOWN:
#                     current_class = (current_class + 1) % len(class_options)
#                 elif event.key == K_RETURN:
#                     return current_class
#
#         # Update the selected class text
#         selected_text = font.render("Selected Class: {}".format(class_options[current_class]), True, (255, 255, 255))
#         screen.blit(selected_text, selected_pos)
#         pygame.display.update()
#         clock.tick(60)



