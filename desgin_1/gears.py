class Gear:
    def __init__(self, chainring, cog, rim, tire):
        self.chainring = chainring
        self.cog = cog
        self.rim = rim
        self.tire = tire

    def ratio(self):
        """Calculate the gear ratio."""
        return self.chainring / self.cog

    def inches(self):
        """Calculate the gear inches."""
        return self.ratio() * (self.rim + (self.tire * 2))
