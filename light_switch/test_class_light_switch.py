import unittest
from class_light_switch import LightSwitch


class LightSwitchTests(unittest.TestCase):
    def test_light_switch_instance(self):
        assert LightSwitch()

    def test_switch_is_on_start_False(self):
        switch = LightSwitch()
        self.assertEqual(switch.switch_is_on, False)

    def test_turn_on(self):
        switch = LightSwitch()
        switch.turn_on()
        self.assertEqual(switch.switch_is_on, True)

    def test_turn_off(self):
        switch = LightSwitch()
        switch.turn_on()
        switch.turn_off()
        self.assertEqual(switch.switch_is_on, False)



if __name__=='__main__':
    unittest.main()