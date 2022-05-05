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
        self.tv.change_channel(7)
        self.assertEqual(self.tv.channel_index, 3)

    def test_change_to_not_existing_channel(self):
        """
        Since channel_index is initialized as 0 and channel 15 doesn't exist.
        channel_index must keep as 0.
        """
        self.tv.change_channel(15)
        self.assertEqual(self.tv.channel_index, 0)

    def test_change_channel_up(self):
        """
        Since channel_index is intialized as 0.
        channel_index must return 1.
        """
        self.tv.change_channel_up()
        self.assertEqual(self.tv.channel_index, 1)

    def test_change_channel_up_when_channel_index_is_the_latest(self):
        """
        channel_index must return 0.
        """
        self.tv.channel_index = -1
        self.tv.change_channel_up()
        self.assertEqual(self.tv.channel_index, 0)

    def test_change_channel_down(self):
        """
        channel_index must return 0.
        """
        self.tv.channel_index = 1
        self.tv.change_channel_down()
        self.assertEqual(self.tv.channel_index, 0)

    def test_change_channel_down_when_channel_index_is_0(self):
        """
        channel_index must return len(self.tv.channels).
        """
        self.tv.channel_index = 0
        self.tv.change_channel_down()
        self.assertEqual(self.tv.channel_index, len(self.tv.channels))

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