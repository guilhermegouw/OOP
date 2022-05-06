class DimmerSwitch:
    def __init__(self, label):
        self.label = label
        self.switch_state = False
        self.brightness_level = 0

    def turn_on(self):
        self.switch_state = True
    
    def turn_off(self):
        self.switch_state = False

    def raise_level(self):
        if self.brightness_level < 10:
            self.brightness_level += 1

    def lower_level(self):
        if self.brightness_level > 0:
            self.brightness_level -= 1