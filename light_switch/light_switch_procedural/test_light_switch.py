import unittest
import light_switch


class LightSwitchTests(unittest.TestCase):
    def test_turn_on(self):
        light_switch.turn_on()
        self.assertEqual(light_switch.switch_is_on, True)

    def test_turn_off(self):
        light_switch.turn_off()
        self.assertEqual(light_switch.switch_is_on, False)

if __name__=='__main__':
    unittest.main()