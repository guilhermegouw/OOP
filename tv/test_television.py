import unittest
from television import TV


class TvTests(unittest.TestCase):
    def setUp(self):
        self.tv = TV()
    
    def test_turn_tv_on(self):
        """
        is_on must return True
        """
        self.tv.turn_tv_on()
        self.assertEqual(self.tv.is_on, True)

    def test_turn_tv_off(self):
        """
        is_on must return False
        """
        self.tv.turn_tv_on()
        self.tv.turn_tv_off()
        self.assertEqual(self.tv.is_on, False)

    def test_raise_the_volume(self):
        """
        Volume is initialized on level 1.
        So it must return 2.
        """
        self.tv.raise_volume()
        self.assertEqual(self.tv.current_volume, 2)

    def test_decrease_the_volume(self):
        """
        Volume is initialized on level 1.
        So it must return 1.
        """
        self.tv.decrease_volume()
        self.assertEqual(self.tv.current_volume, 1)

    def test_change_to_existing_channel(self):
        """
        current_channel must change to selected one.
        """
        self.tv.change_channel(5)
        self.assertEqual(self.tv.current_channel, 5)

    def test_change_to_not_existing_channel(self):
        """
        Since current_channel is initialized as 1 and channel 15 does exist.
        current_channel must keep as 1.
        """
        self.tv.change_channel(15)
        self.assertEqual(self.tv.current_channel, 1)

    def test_change_channel_up(self):
        """
        Since current_cannel is intialized as 1.
        current_channel must return 2.
        """
        self.tv.change_channel_up_and_down('up')
        self.assertEqual(self.tv.current_channel, 2)

    def test_change_channel_up_when_current_channel_is_10(self):
        """
        current_channel must return 10.
        """
        self.tv.current_channel = 10
        self.tv.change_channel_up_and_down('up')
        self.assertEqual(self.tv.current_channel, 10)

    def test_change_channel_down_when_current_channel_is_1(self):
        """
        current_channel must return 1.
        """
        self.tv.change_channel_up_and_down('down')
        self.assertEqual(self.tv.current_channel, 1)

    def test_change_channel_down(self):
        """
        when current_channel is 2
        current_channel must return 1.
        """
        self.tv.current_channel = 2
        self.tv.change_channel_up_and_down('down')
        self.assertEqual(self.tv.current_channel, 1)

    def test_mute_the_sound(self):
        """
        is_muted must return True
        """
        self.tv.mute_the_sound()
        self.assertEqual(self.tv.is_muted, True)

    def test_unmute_the_sound(self):
        """
        is_muted must return False
        """
        self.tv.mute_the_sound()
        self.tv.unmute_the_sound()
        self.assertEqual(self.tv.is_muted, False)


if __name__=='__main__':
    unittest.main()