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
        self.channels = [1, 2, 4, 7, 11, 16, 22, 29, 38, 48]
        self.channel_index = 0
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
            self.channel_index = self.channels.index(channel)

    def change_channel_up(self):
        if self.channel_index < len(self.channels):
            self.channel_index += 1
        else:
            self.channel_index = 0

    def change_channel_down(self):
        if self.channel_index > 0:
            self.channel_index -= 1
        else:
            self.channel_index = len(self.channels)
    
    def mute_the_sound(self):
        self.is_muted = True
    
    def unmute_the_sound(self):
        self.is_muted = False


if __name__=='__main__':
    tv = TV()
    tv.change_channel(16)
