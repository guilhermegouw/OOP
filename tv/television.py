"""
We can determine that to keep track of its state, a TV class would have to 
maintain the following data:

- Power state (on or off)
- Mute state (is it muted?)
- List of channels available
- Current channel setting
- Current volume setting
- Range of volume levels available

And the actions that the TV must provide include:

- Turn the power on and off
- Raise and lower the volume
- Change the channel up and down
- Mute and unmute the sound
- Go to a specified channel
"""
class TV:
    def __init__(self):
        self.is_on = False
        self.is_muted = False
        self.channels = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12]
        self.current_channel = 1
        self.current_volume = 1
    
    def turn_tv_on(self):
        self.is_on = True
    
    def turn_tv_off(self):
        self.is_on = False
    
    def raise_volume(self):
        if self.current_volume < 10:
            self.current_volume += 1
    
    def decrease_volume(self):
        if self.current_volume > 1:
            self.current_volume -= 1
    
    def change_channel(self, channel):
        if channel in self.channels:
            self.current_channel = channel

    def change_channel_up_and_down(self, direction):
        if direction == 'up' and self.current_channel < 10:
            self.current_channel += 1
        if direction == 'down' and self.current_channel > 1:
            self.current_channel -= 1
    
    def mute_the_sound(self):
        self.is_muted = True
    
    def unmute_the_sound(self):
        self.is_muted = False