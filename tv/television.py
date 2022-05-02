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
- Get information about the current settings
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
        self.in_on = True
    
    def raise_volume(self):
        self.current_volume += 1
    
    def change_channel(self, channel):
        if channel not in self.channels:
            print('Channel not available')
        self.current_channel = channel

    def change_channel_up_and_down(self):
        pass