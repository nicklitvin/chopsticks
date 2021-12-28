import unittest
from player import Player
from hands import Hands
hands = Hands()

class TestPlayer(unittest.TestCase):

    def test_draw(self):
        p = Player('a',hands)
        p.drawHands(reversed=1)
        p.drawHands()
    
    def test_reduce(self):    
        p = Player('a',hands)
        p.handR = 3
        p.handL = 9
        p.reduceHands()
        self.assertEqual(p.handL,4)
        self.assertEqual(p.handR,3)
    
    def test_getHandVal(self):
        p = Player('a',hands)
        p.handL = 3
        self.assertEqual(p.getHandVal('l'),3)
        self.assertEqual(p.getHandVal('r'),1)

    def test_takeHit(self):
        p = Player('a',hands)
        p.takeHit('r',2)
        self.assertEqual(p.handL,1)
        self.assertEqual(p.handR,3)

    def test_convertElementsToArr(self):
        p = Player('a',hands)
        self.assertEqual(p.convertElementsToInt(['1','2']),[1,2])
        self.assertEqual(p.convertElementsToInt(['1','2b']),None)

    def test_hit(self):
        p1 = Player('a',hands)
        p2 = Player('b',hands)
        p1.hit(p2,('l','r'))
        self.assertEqual(p2.handL,2)

    def test_isGoodHit(self):
        p1 = Player('a',hands)
        p2 = Player('b',hands)

        p2.handL, p2.handR = 3,0
        self.assertEqual(p1.isLegalHit(p2,'l','l'),None)

    def test_split(self):
        p1 = Player('a',hands)
        p1.handL = 4
        p1.handR = 3
        p1.split('52')
        self.assertEqual(p1.handL,0)
        self.assertEqual(p1.handR,2)

    def test_isGoodSplit(self):
        p1 = Player('a',hands)
        self.assertEqual(p1.isGoodSplit((2,0)),True)
        self.assertEqual(p1.isGoodSplit((2,1)),None)
        self.assertEqual(p1.isGoodSplit((2,0,0)),None)
        self.assertEqual(p1.isGoodSplit((1,1)),None)


    # def test_addManyHands(self):
    #     p = Player('a',hands)
    #     for _ in range(10000):
    #         p.drawHands()

if __name__ == '__main__':
    unittest.main()