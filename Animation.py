import pygame
import warnings


class Animation:
    def __init__(self, sprite_sheet_path, sprite_size, num_frames, frame_durations=None, loop=True, end_callback=None):
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.sprite_size = sprite_size
        self.num_frames = num_frames
        self.frame_durations = frame_durations if frame_durations else [100] * num_frames
        self.loop = loop
        self.end_callback = end_callback
        self.current_frame = 0
        self.current_frame_duration = self.frame_durations[self.current_frame]
        self.last_update_time = 0
        self.is_playing = False
        self.is_paused = False

        self.frames = self.load_frames()  # Just load the frames once, directions are handled with flipping
        self.flip = False  # Add a flag to know whether to flip image horizontally

    def load_frames(self):
        frames = []
        for i in range(self.num_frames):
            frame_left = i * self.sprite_size[0]
            frame_top = 0  # Only one row is considered, adjust if needed
            frame = self.sprite_sheet.subsurface((frame_left, frame_top, *self.sprite_size))
            frame = pygame.transform.scale(frame, (self.sprite_size[0] * 4, self.sprite_size[1] * 4))  # Upscaling
            frames.append(frame)
        return frames

    def set_frame_durations(self, new_durations):
        if len(new_durations) == self.num_frames:
            self.frame_durations = new_durations
        else:
            print(f"Error: Expected {self.num_frames} durations, but got {len(new_durations)}")

    def draw(self, screen, position):
        frame = self.get_current_frame()
        if self.flip:  # Flip the frame if self.flip is True
            frame = pygame.transform.flip(frame, True, False)
        screen.blit(frame, position)

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
                    #print(f"Updating animation frame to: {self.current_frame}")  # Debug print
                self.current_frame_duration = self.frame_durations[self.current_frame]
                #print(f"Frame Updated to: {self.current_frame}")


    def get_current_frame(self):
        return self.frames[self.current_frame]

    def set_direction(self, new_direction):
        # Simplify to just handle flipping, not changing frame sets
        if new_direction == 'left':
            self.flip = True
        elif new_direction == 'right':
            self.flip = False
        else:
            warnings.warn(f"Invalid direction: {new_direction}.")

    def pause(self):
        if self.is_playing and not self.is_paused:
            self.is_paused = True
            self.is_playing = False

    def resume(self):
        if not self.is_playing and self.is_paused:
            self.is_playing = True
            self.is_paused = False

    def play_from_start(self):
        self.reset()
        self.play()

    def set_frame(self, frame_index):
        if 0 <= frame_index < self.num_frames:
            self.current_frame = frame_index
        else:
            print(f"Error: Frame {frame_index} does not exist.")


