#
# To use this class, create an instance for each animation you want to use,
# passing in the sprite sheet, sprite size, number of frames, and animation speed as
# parameters. You would then call the play() method to start the animation and stop()
# method to stop it. You would also call the update() method each frame to update the
# current frame based on the elapsed time since the last update, and the
# get_current_frame() method to get the current frame to display.
#
#

class Animation:
    def __init__(self, sprite_sheet, sprite_size, num_frames, animation_speed):
        self.sprite_sheet = sprite_sheet
        self.sprite_size = sprite_size
        self.num_frames = num_frames
        self.animation_speed = animation_speed
        self.frames = self.load_frames()
        self.current_frame = 0
        self.last_update_time = 0
        self.is_playing = False

    def load_frames(self):
        frames = []
        for i in range(self.num_frames):
            frame = self.sprite_sheet.subsurface((i * self.sprite_size[0], 0, *self.sprite_size))
            frames.append(frame)
        return frames

    def play(self):
        self.is_playing = True

    def stop(self):
        self.is_playing = False

    def update(self, dt):
        if self.is_playing:
            self.last_update_time += dt
            if self.last_update_time > self.animation_speed:
                self.current_frame += 1
                if self.current_frame >= self.num_frames:
                    self.current_frame = 0
                self.last_update_time = 0

    def get_current_frame(self):
        return self.frames[self.current_frame]
