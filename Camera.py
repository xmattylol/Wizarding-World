# import pygame
#
# class Camera:
#     def __init__(self, width, height, zoom=16):
#         self.camera = pygame.Rect(0, 0, width, height)
#         self.width = width
#         self.height = height
#         self.zoom = zoom
#
#
#     def apply(self, entity):
#     # Apply the camera's offset to the entity's position without zoom
#         return entity.move(-self.camera.topleft[0], -self.camera.topleft[1])
#
#
#     def update(self, target):
#         x = -target.rect.centerx + int(self.width / 2)
#         y = -target.rect.centery + int(self.height / 2)
#
#         # Limit scrolling to map size
#         x = min(0, x)  # Left
#         y = min(0, y)  # Top
#         x = max(-(self.width - self.camera.width), x)  # Right
#         y = max(-(self.height - self.camera.height), y)  # Bottom
#
#         self.camera = pygame.Rect(x, y, self.width, self.height)
