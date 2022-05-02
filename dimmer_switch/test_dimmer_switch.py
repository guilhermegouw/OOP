from tkinter import OFF
import unittest
from dimmer_switch import DimmerSwitch


class DimmerSwitchTests(unittest.TestCase):
    def setUp(self):
        self.dimmer = DimmerSwitch()

    def test_turn_on(self):
        """
        switch_state must return True.
        """
        self.dimmer.turn_on()
        self.assertEqual(self.dimmer.switch_state, True)

    def test_turn_off(self):
        """
        switch_state must return False.
        """
        self.dimmer.turn_on
        self.dimmer.turn_off()
        self.assertEqual(self.dimmer.switch_state, False)
    
    def test_raise_level(self):
        """
        Raise level must raise brightness level by one.
        """
        self.dimmer.raise_level()
        self.assertEqual(self.dimmer.brightness_level, 1)
    
    def test_raise_level_above_ten(self):
        """
        If brightness level already is 10.
        It must keep on 10 when raise_level is called.
        """
        self.dimmer.brightness_level = 10
        self.dimmer.raise_level()
        self.assertEqual(self.dimmer.brightness_level, 10)
    
    def test_lower_level(self):
        """
        lower_level must reduce brightness level by 1.
        """
        self.dimmer.raise_level()
        self.dimmer.lower_level()
        self.assertEqual(self.dimmer.brightness_level, 0)

    def test_lower_level_below_zero(self):
        """
        If brightness already is 0. 
        It must keep on zero when lower_velvel is called.
        """
        self.dimmer.lower_level()
        self.assertEqual(self.dimmer.brightness_level, 0)



if __name__=='__main__':
    unittest.main()