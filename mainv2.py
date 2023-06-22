# import pygame
# from pygame.locals import *
# import sys
# from cards import *
# from character import *
# from Deck import *
# from Enemy import *
# pygame.init()
#
#
# # Clock
# clock = pygame.time.Clock()
#
#
# # Setting up the window
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Wizarding World")
#
# # Color scheme
# background_color = (10, 10, 10)
# button_color = (65, 105, 225)
# button_hover_color = (135, 206, 235)
# text_color = (255, 255, 255)
#
# # Wizard font
# font_path = "fonts/HARRYP__.TTF"
# font = pygame.font.Font(font_path, 36)
# font_small = pygame.font.Font("fonts/HARRYP__.TTF", 30)
# font_medium = pygame.font.Font("fonts/HARRYP__.TTF", 48)
# font_large = pygame.font.Font("fonts/HARRYP__.TTF", 72)
#
# # Class options
# class_options = [
#         {"text": "Storm", "class": "Storm"},
#         {"text": "Fire", "class": "Fire"},
#         {"text": "Ice", "class": "Ice"},
#         {"text": "Life", "class": "Life"},
#         {"text": "Myth", "class": "Myth"},
#         {"text": "Death", "class": "Death"},
#         {"text": "Balance", "class": "Balance"}
#     ]
#
#
# # Main menu
# def main_menu():
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
#         # Background
#         screen.fill(background_color)
#
#         # Title
#         title_text = font_large.render("Wizarding World", True, text_color)
#         title_rect = title_text.get_rect(center=(400, 150))
#         screen.blit(title_text, title_rect)
#
#         # New game button
#         new_game_text = font_small.render("New Game", True, text_color)
#         new_game_rect = new_game_text.get_rect(center=(400, 300))
#         pygame.draw.rect(screen, button_color, (new_game_rect.left - 10, new_game_rect.top - 10,
#                                                  new_game_rect.width + 20, new_game_rect.height + 20))
#         screen.blit(new_game_text, new_game_rect)
#
#         # Load game button
#         load_game_text = font_small.render("Load Game", True, text_color)
#         load_game_rect = load_game_text.get_rect(center=(400, 365))
#         pygame.draw.rect(screen, button_color, (load_game_rect.left - 10, load_game_rect.top - 10,
#                                                  load_game_rect.width + 20, load_game_rect.height + 20))
#         screen.blit(load_game_text, load_game_rect)
#
#         # Settings button
#         settings_text = font_small.render("Settings", True, text_color)
#         settings_rect = settings_text.get_rect(center=(400, 430))
#         pygame.draw.rect(screen, button_color, (settings_rect.left - 10, settings_rect.top - 10,
#                                                  settings_rect.width + 20, settings_rect.height + 20))
#         screen.blit(settings_text, settings_rect)
#
#         # Exit button
#         exit_text = font_small.render("Exit", True, text_color)
#         exit_rect = exit_text.get_rect(center=(400, 495))
#         pygame.draw.rect(screen, button_color, (exit_rect.left - 10, exit_rect.top - 10,
#                                                  exit_rect.width + 20, exit_rect.height + 20))
#         screen.blit(exit_text, exit_rect)
#
#         # Button hover effect
#         mouse_pos = pygame.mouse.get_pos()
#         if new_game_rect.collidepoint(mouse_pos):
#             pygame.draw.rect(screen, button_hover_color, (new_game_rect.left - 10, new_game_rect.top - 10,
#                                                           new_game_rect.width + 20, new_game_rect.height + 20))
#             screen.blit(new_game_text, new_game_rect)
#             if pygame.mouse.get_pressed()[0]:
#                 new_game()
#         if load_game_rect.collidepoint(mouse_pos):
#             pygame.draw.rect(screen, button_hover_color, (load_game_rect.left - 10, load_game_rect.top - 10,
#                                                           load_game_rect.width + 20, load_game_rect.height + 20))
#             screen.blit(load_game_text, load_game_rect)
#             if pygame.mouse.get_pressed()[0]:
#                 pass#load_game()
#
#         if settings_rect.collidepoint(mouse_pos):
#             pygame.draw.rect(screen, button_hover_color, (settings_rect.left - 10, settings_rect.top - 10,
#                                                           settings_rect.width + 20, settings_rect.height + 20))
#             screen.blit(settings_text, settings_rect)
#             if pygame.mouse.get_pressed()[0]:
#                 pass#settings()
#         elif exit_rect.collidepoint(mouse_pos):
#             pygame.draw.rect(screen, button_hover_color, (exit_rect.left - 10, exit_rect.top - 10,
#                                                           exit_rect.width + 20, exit_rect.height + 20))
#             screen.blit(exit_text, exit_rect)
#             if pygame.mouse.get_pressed()[0]:
#                 pygame.quit()
#                 quit()
#
#         pygame.display.update()
#
#
# def class_menu():
#     # Start a new game and choose a character class
#     screen.fill(background_color)
#     current_class = 0
#
#     # Set up class options
#     class_options = ["Storm", "Fire", "Ice", "Death", "Life", "Myth", "Balance"]
#
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
#     selected_pos = selected_text.get_rect(center=(screen_width / 2, 550))
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
#                 pygame.draw.rect(screen, background_color, selected_pos)
#                 if event.key == K_ESCAPE:
#                     return current_class
#                 elif event.key == K_UP:
#                     current_class = (current_class - 1) % len(class_options)
#                 elif event.key == K_DOWN:
#                     current_class = (current_class + 1) % len(class_options)
#                 #elif event.key == K_RETURN:
#                 #    return current_class
#                 elif event.key == (K_SPACE or K_RETURN):
#                     selected_class = class_options[current_class]
#                     print("Selected " + selected_class)
#                     tutorial(selected_class)
#
#         # Update the selected class text
#         selected_text = font.render("Selected Class: {}".format(class_options[current_class]), True, (255, 255, 255))
#         screen.blit(selected_text, selected_pos)
#         pygame.display.update()
#         clock.tick(60)
#
# def tutorial(selected_class):
#     print("Tutorial starting...")
#     # Create the player character with the selected class and a starter deck
#     player = Character(name="Player", class_type=selected_class, max_health=500, max_mana=50, deck=starter_deck)
#
#     # Create a Golem enemy for the tutorial
#     golem = Enemy("Golem", 250, 0.5, golem_deck, "Myth")
#
#     # Initialize game state
#     player_turn = True
#     in_combat = True
#
#     # Combat loop
#     while in_combat:
#         screen.fill(background_color)
#
#         # Display player and enemy stats
#         player.display_stats(screen, font_small)
#         golem.display_stats(screen, font_small)
#
#         for event in pygame.event.get():
#             if event.type == QUIT:
#             pass# ...
#             if event.type == KEYDOWN:
#             pass# ...
#             if event.type == MOUSEBUTTONDOWN:
#                 # Get the mouse position when clicked
#                 mouse_pos = pygame.mouse.get_pos()
#                 if player_turn:
#                     card_to_play = player.choose_card(mouse_pos)
#                     if card_to_play is not None:
#                         # Play the chosen card and apply its effect
#                         player.play_card(card_to_play, golem)
#                         player_turn = False
#                 else:
#                     # Enemy's turn
#                     card_to_play = golem.choose_card()
#
#                     if card_to_play is not None:
#                         # Play the chosen card and apply its effect
#                         golem.play_card(card_to_play, player)
#                         player_turn = True
#                 # Player's turn
#                 #if player_turn:
#                 #    player.choose_card(mouse_pos)
#
#         # Check if player or enemy is defeated
#         if player.is_defeated():
#             print("You have been defeated. Try again!")
#             break
#         if golem.is_defeated():
#             print("You have defeated the Golem!")
#             in_combat = False
#             break
#
#         # Player's turn
#         if player_turn:
#             player.display_hand(screen, player.hand)
#             #card_to_play = player.choose_card(mouse_pos)
#
#             if card_to_play is not None:
#                 # Play the chosen card and apply its effect
#                 player.play_card(card_to_play, golem)
#                 player_turn = False
#         else:
#             # Enemy's turn
#             card_to_play = golem.choose_card()
#
#             if card_to_play is not None:
#                 # Play the chosen card and apply its effect
#                 golem.play_card(card_to_play, player)
#                 player_turn = True
#
#         pygame.display.update()
#         clock.tick(60)
#
#     # End the tutorial
#     print("Tutorial complete!")
#
#
#
# # New game function
# def new_game():
#     print("New game starting...")
#     class_menu()
#
#
# # Start the main menu
# main_menu()
