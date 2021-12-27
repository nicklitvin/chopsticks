import unittest
from player import Player

class TestPlayer(unittest.TestCase):

    def test_draw(self):
        p = Player('a')
        self.assertEqual(p.handWidth,21)
        p.drawUpsideDownHands()
        p.drawHands()
    
    def test_reduce(self):    
        p = Player('a')
        p.handR = 3
        p.handL = 9
        p.reduceHands()
        self.assertEqual(p.handL,4)
        self.assertEqual(p.handR,3)
    
    def test_getHandVal(self):
        p = Player('a')
        p.handL = 3
        self.assertEqual(p.getHandVal('l'),3)
        self.assertEqual(p.getHandVal('r'),1)

    def test_takeHit(self):
        p = Player('a')
        p.takeHit('r',2)
        self.assertEqual(p.handL,1)
        self.assertEqual(p.handR,3)

    def test_convertElementsToArr(self):
        p = Player('a')
        self.assertEqual(p.convertElementsToInt(['1','2']),[1,2])
        self.assertEqual(p.convertElementsToInt(['1','2b']),None)

if __name__ == '__main__':
    unittest.main()