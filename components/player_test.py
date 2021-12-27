import unittest
from player import Player

class TestPlayer(unittest.TestCase):

    def test_upper(self):
        player = Player('a')
        self.assertEqual(player.handWidth,22)
        player.drawHands()

if __name__ == '__main__':
    unittest.main()