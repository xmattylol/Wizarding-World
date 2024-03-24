import pytmx
import pygame

class Camera:
    def __init__(self, screen, tmx_data, map_width, map_height, zoom):
        self.screen = screen
        self.tmx_data = tmx_data
        self.screen_rect = screen.get_rect()
        self.map_width = map_width * zoom
        self.map_height = map_height * zoom
        self.zoom = zoom
        self.offset = pygame.math.Vector2()

    def update(self, target):
        target_center = pygame.math.Vector2(target.rect.center) * self.zoom
        self.offset = target_center - pygame.math.Vector2(self.screen_rect.center)

        # Clamp the camera to the map size
        self.offset.x = max(0, min(self.map_width - self.screen_rect.width, self.offset.x))
        self.offset.y = max(0, min(self.map_height - self.screen_rect.height, self.offset.y))
    # def update(self, target):
    #     # Calculate the desired camera position to center on the target with smooth panning
    #     target_pos = pygame.math.Vector2(target.rect.centerx, target.rect.centery) - pygame.math.Vector2(
    #         self.screen_rect.width / (2 * self.zoom), self.screen_rect.height / (2 * self.zoom))
    #     self.offset += (target_pos - self.offset) * 0.1  # Adjust the factor (0.1) for smoother or quicker panning
    #
    #     # Clamp the camera to prevent showing areas outside the map, considering the zoom
    #     self.offset.x = max(0, min(self.map_width - self.screen_rect.width / self.zoom, self.offset.x))
    #     self.offset.y = max(0, min(self.map_height - self.screen_rect.height / self.zoom, self.offset.y))

    # def update(self, target):
    #     # Calculate the desired camera position to center on the target with smooth panning
    #     target_pos = pygame.math.Vector2(target.rect.centerx, target.rect.centery) - pygame.math.Vector2(
    #         self.screen_rect.width / (2 * self.zoom), self.screen_rect.height / (2 * self.zoom))
    #     self.offset += (target_pos - self.offset) * 0.1  # Adjust the factor (0.1) for smoother or quicker panning
    #
    #     # Clamp the camera to prevent showing areas outside the map, considering the zoom
    #     self.offset.x = max(0, min(self.map_width * self.zoom - self.screen_rect.width, self.offset.x))
    #     self.offset.y = max(0, min(self.map_height * self.zoom - self.screen_rect.height, self.offset.y))
    # def apply(self, entity):
    #     # Apply zoom and offset to the entity position
    #     return entity.rect.move(self.offset.x * -1, self.offset.y * -1).inflate(entity.rect.width * (self.zoom - 1),
    #                                                                             entity.rect.height * (self.zoom - 1))

    def apply(self, entity_or_rect):
        # Check if the argument is an entity with a 'rect' attribute or a pygame.Rect
        if hasattr(entity_or_rect, 'rect'):
            # It's an entity; use its 'rect' attribute
            rect = entity_or_rect.rect
        else:
            # It's already a pygame.Rect
            rect = entity_or_rect

        # Now 'rect' is always a pygame.Rect, so we can apply the transformation
        adjusted_rect = pygame.Rect(
            (rect.x - self.offset.x) * self.zoom,  # Apply offset and zoom to X position
            (rect.y - self.offset.y) * self.zoom,  # Apply offset and zoom to Y position
            rect.width * self.zoom,  # Scale width by zoom factor
            rect.height * self.zoom)  # Scale height by zoom factor
        return adjusted_rect


    # def apply(self, rect):
    #     # Apply camera transformations to the entity rect
    #     return rect.move(-self.offset.x * self.zoom, -self.offset.y * self.zoom)
    #
    # def draw_entities(self, entities):
    #     # Sort entities by their Y position to handle drawing order (Y-sort)
    #     for entity in sorted(entities, key=lambda e: e.rect.bottom):
    #         # Apply camera transformation and zoom to entity's current frame for rendering
    #         frame = entity.animation.get_current_frame()
    #         scaled_frame_size = (int(frame.get_width() * self.zoom), int(frame.get_height() * self.zoom))
    #         scaled_frame = pygame.transform.scale(frame, scaled_frame_size)
    #         scaled_frame_rect = self.apply(entity.rect.copy())
    #         scaled_frame_rect.size = scaled_frame_size
    #         self.screen.blit(scaled_frame, scaled_frame_rect.topleft)
    #         # scaled_frame = pygame.transform.scale(frame, (
    #         # int(2 * entity.rect.width * self.zoom), int(2 * entity.rect.height * self.zoom)))
    #         # scaled_frame_rect = self.apply(entity.rect)
    #         # self.screen.blit(scaled_frame,scaled_frame_rect.topleft)

    def draw_entities(self, entities):
        for entity in entities:
            rect = self.apply(entity)
            self.screen.blit(pygame.transform.scale(entity.animation.get_current_frame(), rect.size), rect.topleft)

    def draw_map(self):
        # Adjusted to correct tile positioning with zoom and offset
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        tile_rect = pygame.Rect(
                            x * self.tmx_data.tilewidth * self.zoom - self.offset.x,
                            y * self.tmx_data.tileheight * self.zoom - self.offset.y,
                            self.tmx_data.tilewidth * self.zoom,
                            self.tmx_data.tileheight * self.zoom)
                        self.screen.blit(pygame.transform.scale(tile, (tile_rect.width, tile_rect.height)),
                                         tile_rect.topleft)
    # def draw_map(self):
    #     # Adjust map drawing to apply camera zoom and transformations
    #     for layer in self.tmx_data.visible_layers:
    #         if isinstance(layer, pytmx.TiledTileLayer):
    #             for x, y, gid in layer:
    #                 tile = self.tmx_data.get_tile_image_by_gid(gid)
    #                 if tile:
    #                     tile_rect = pygame.Rect(
    #                         round(0.5 * x * self.tmx_data.tilewidth * self.zoom),
    #                         round(0.5 * y * self.tmx_data.tileheight * self.zoom),
    #                         round(0.5 * self.tmx_data.tilewidth * self.zoom),
    #                         round(0.5 * self.tmx_data.tileheight * self.zoom))
    #                     tile_rect = self.apply(tile_rect)
    #                     self.screen.blit(tile, tile_rect)

    # def draw_map(self):
    #     # Adjust map drawing to apply camera zoom and transformations
    #     for layer in self.tmx_data.visible_layers:
    #         if isinstance(layer, pytmx.TiledTileLayer):
    #             for x, y, gid in layer:
    #                 tile = self.tmx_data.get_tile_image_by_gid(gid)
    #                 if tile:
    #                     tile_rect = pygame.Rect(
    #                         x * self.tmx_data.tilewidth * self.zoom,
    #                         y * self.tmx_data.tileheight * self.zoom,
    #                         self.tmx_data.tilewidth * self.zoom,
    #                         self.tmx_data.tileheight * self.zoom)
    #                     tile_rect = self.apply(tile_rect)
    #                     self.screen.blit(tile, tile_rect)

    # def draw_entities(self, entities):
    #     for entity in entities:
    #         # Adjust drawing to use the animation's current frame and apply camera zoom and positioning
    #         entity_rect = self.apply(entity.rect)
    #         frame = entity.animation.get_current_frame()
    #         scaled_frame = pygame.transform.scale(frame, (int(entity_rect.width), int(entity_rect.height)))
    #         self.screen.blit(scaled_frame, entity_rect.topleft)