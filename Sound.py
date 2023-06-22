import pygame

class Sound:
    def __init__(self):
        # Initialize Pygame's sound mixer
        pygame.mixer.init()

        # Load sound effects
        self.sound_effects = {
            "card_draw": pygame.mixer.Sound("sounds/card_draw.wav"),
            "card_discard": pygame.mixer.Sound("sounds/card_discard.wav"),
            "card_play": pygame.mixer.Sound("sounds/card_play.wav"),
            "enemy_attack": pygame.mixer.Sound("sounds/enemy_attack.wav"),
            "player_attack": pygame.mixer.Sound("sounds/player_attack.wav"),
            "victory": pygame.mixer.Sound("sounds/victory.wav"),
            "defeat": pygame.mixer.Sound("sounds/defeat.wav")
        }

        # Load music
        self.music = {
            "menu": "music/menu.mp3",
            "combat": "music/combat.mp3",
            "victory": "music/victory.mp3",
            "defeat": "music/defeat.mp3"
        }

        # Set initial music volume
        pygame.mixer.music.set_volume(0.5)

    def play_sound_effect(self, sound_effect):
        """Plays a sound effect."""
        if sound_effect in self.sound_effects:
            self.sound_effects[sound_effect].play()

    def play_music(self, music):
        """Plays music."""
        if music in self.music:
            pygame.mixer.music.load(self.music[music])
            pygame.mixer.music.play(-1)

    def stop_music(self):
        """Stops playing music."""
        pygame.mixer.music.stop()

    def set_music_volume(self, volume):
        """Sets the volume for music."""
        pygame.mixer.music.set_volume(volume)

    def set_sound_effect_volume(self, volume):
        """Sets the volume for sound effects."""
        for sound_effect in self.sound_effects.values():
            sound_effect.set_volume(volume)
