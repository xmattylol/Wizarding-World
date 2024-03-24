import pygame, sys, pytmx
from pytmx.util_pygame import load_pygame
from pygame.locals import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, obstacle=False):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.obstacle = obstacle  # Flag to mark tiles as obstacles

class Level:
    def __init__(self, tmx_file, screen):
        self.screen = screen
        self.tmx_data = load_pygame(tmx_file)
        self.sprite_group = pygame.sprite.Group()
        self.obstacles_group = pygame.sprite.Group()  # Separate group for obstacle tiles
        self.load_tiles()

    def load_tiles(self):
        # Load and create tiles for all visible layers
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'data'):  # Tile layers
                for x, y, surf in layer.tiles():
                    pos = (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight)
                    Tile(pos=pos, surf=surf, groups=self.sprite_group)
            elif isinstance(layer, pytmx.TiledObjectGroup):  # Object layers
                for obj in layer:
                    if obj.type in ('Obstacle',):  # Define more types as needed
                        if obj.image:  # Objects with an associated image
                            pos = (obj.x, obj.y)
                            Tile(pos=pos, surf=obj.image, groups=[self.sprite_group, self.obstacles_group], obstacle=True)

    # def draw(self):
    #     self.screen.fill('black')
    #     self.sprite_group.draw(self.screen)
    #
    #     # Optionally, visualize obstacles differently
    #     for obstacle in self.obstacles_group:
    #         pygame.draw.rect(self.screen, (255, 0, 0), obstacle.rect, 2)  # Draw red outlines for obstacles

    # def draw(self, camera):
    #     # Adjusted to apply camera transformations
    #     self.screen.fill('black')
    #     for sprite in self.sprite_group:
    #         # Apply the camera's offset and zoom to each tile
    #         rect = camera.apply(sprite.rect)
    #         self.screen.blit(pygame.transform.scale(sprite.image, rect.size), rect.topleft)
    #
    #     # Draw obstacles with camera adjustments (if needed)
    #     for obstacle in self.obstacles_group:
    #         rect = camera.apply(obstacle.rect)
    #         pygame.draw.rect(self.screen, (255, 0, 0), rect, 2)  # Adjust rect based on camera

    def draw(self, camera):
        self.screen.fill('black')
        for sprite in self.sprite_group:
            rect = camera.apply(sprite.rect)
            self.screen.blit(pygame.transform.scale(sprite.image, (rect.width, rect.height)), rect.topleft)

    def update(self):
        # This method can be expanded to include level-specific update logic
        pass
