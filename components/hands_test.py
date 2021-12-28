import unittest
from hands import Hands

class TestHands(unittest.TestCase):
    
    def test_getMaxWidth(self):
        hands = Hands()
        hands.getMaxWidth()
        self.assertEqual(hands.handWidth,21)

    def test_addHand(self):
        print('\n')
        hands = Hands()
        hands.addHand('L4')
        self.assertNotEqual(hands.hands['L4'][0][0],'.')

    def test_drawHands(self):
        print('\n')
        hands = Hands()
        hands.drawHands(2,3)
        self.assertNotEqual(hands.hands['L2'][0][0],'.')

    def test_drawUpsideDownHands(self):
        print('\n')
        hands = Hands()
        hands.drawHands(1,2,upsideDown=1)
        
    # def test_addAll(self):
    #     hands = Hands()
    #     for _ in range(10000):
    #         hands.drawHands(1,1)


if __name__ == '__main__':
    unittest.main()