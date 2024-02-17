import pytmx
import pygame

class Camera:
    def __init__(self, screen, tmx_data, map_width, map_height, zoom=1):
        self.screen = screen
        self.tmx_data = tmx_data
        self.screen_rect = screen.get_rect()
        self.map_width = map_width
        self.map_height = map_height
        self.zoom = zoom
        self.offset = pygame.math.Vector2()

    def update(self, target):
        # Center the camera on the target
        self.offset.x = target.rect.centerx - self.screen_rect.width / 2
        self.offset.y = target.rect.centery - self.screen_rect.height / 2

        # Clamp the camera to prevent showing areas outside the map
        self.offset.x = max(0, min(self.map_width - self.screen_rect.width, self.offset.x))
        self.offset.y = max(0, min(self.map_height - self.screen_rect.height, self.offset.y))

    def apply(self, rect):
        # Apply camera transformations to the entity rect
        return rect.move(-self.offset.x, -self.offset.y)

    def draw_entities(self, entities):
        # Sort entities by their Y position to handle drawing order (Y-sort)
        for entity in sorted(entities, key=lambda e: e.rect.bottom):
            # Apply camera transformation and zoom to entity's current frame for rendering
            frame = entity.animation.get_current_frame()
            scaled_frame = pygame.transform.scale(frame, (
            int(2 * entity.rect.width * self.zoom), int(2 * entity.rect.height * self.zoom)))
            scaled_frame_rect = self.apply(entity.rect)
            self.screen.blit(scaled_frame,scaled_frame_rect.topleft)

    def draw_map(self):
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        tile_rect = pygame.Rect(
                            x * self.tmx_data.tilewidth,
                            y * self.tmx_data.tileheight,
                            self.tmx_data.tilewidth,
                            self.tmx_data.tileheight)
                        tile_rect = self.apply(tile_rect)
                        self.screen.blit(tile, tile_rect)

    # def draw_entities(self, entities):
    #     for entity in entities:
    #         # Adjust drawing to use the animation's current frame and apply camera zoom and positioning
    #         entity_rect = self.apply(entity.rect)
    #         frame = entity.animation.get_current_frame()
    #         scaled_frame = pygame.transform.scale(frame, (int(entity_rect.width), int(entity_rect.height)))
    #         self.screen.blit(scaled_frame, entity_rect.topleft)