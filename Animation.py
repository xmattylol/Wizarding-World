import pygame

class Animation:
    def __init__(self, sprite_sheet_path, sprite_size, num_frames, frame_durations=None, loop=True, end_callback=None):
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.sprite_size = sprite_size
        self.num_frames = num_frames
        self.frame_durations = frame_durations if frame_durations else [100] * num_frames
        self.loop = loop
        self.end_callback = end_callback
        self.frames = self.load_frames()
        self.current_frame = 0
        self.current_frame_duration = self.frame_durations[self.current_frame]
        self.last_update_time = 0
        self.is_playing = False
        assert len(self.frames) == self.num_frames, "Mismatched frame count!"


    def load_frames(self):
        frames = []
        sheet_width, sheet_height = self.sprite_sheet.get_size()
        for i in range(self.num_frames):
            frame_left = i * self.sprite_size[0]
            if frame_left + self.sprite_size[0] > sheet_width or self.sprite_size[1] > sheet_height:
                raise ValueError(
                    f"Frame {i} is outside of sprite sheet bounds! Sprite size might be too large or num_frames too high.")

            frame = self.sprite_sheet.subsurface((frame_left, 0, *self.sprite_size))
            frame = pygame.transform.scale(frame, (self.sprite_size[0] * 4, self.sprite_size[1] * 4))  # Upscaling here
            frames.append(frame)
        return frames

    def draw(self, screen, position):
        screen.blit(self.get_current_frame(), position)

    def play(self):
        self.is_playing = True

    def stop(self):
        self.is_playing = False

    def reset(self):
        self.current_frame = 0
        self.last_update_time = 0

    def update(self, dt):
        if self.is_playing:
            self.last_update_time += dt * 1000  # Convert to ms if dt is in seconds
            while self.last_update_time >= self.current_frame_duration:
                self.last_update_time -= self.current_frame_duration  # Subtract before updating the frame
                self.current_frame += 1  # Increment current frame here, not outside the while loop

                if self.current_frame >= self.num_frames:
                    if self.loop:
                        self.current_frame = 0
                        self.last_update_time = 0  # You might want to reset this too
                    else:
                        self.stop()
                        if self.end_callback:
                            self.end_callback()
                        return  # Exit the method after stopping animation to avoid possible index error

                self.current_frame_duration = self.frame_durations[self.current_frame]
                print(f"Frame Updated to: {self.current_frame}")


    def get_current_frame(self):
        try:
            return self.frames[self.current_frame]
        except IndexError:
            print(
                f"Error: Trying to access frame {self.current_frame}, but only {len(self.frames)} frames are available.")
            return self.frames[0]  # Return the first frame or a placeholder to avoid crash


