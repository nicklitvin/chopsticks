import os

class Hands:
    def __init__(self):
        # self.hands key: U?[LR][0-4]
        self.hands = {}
        self.handWidth = self.getMaxWidth()
        self.spaceBetweenHands = 5

    def getMaxWidth(self):
        self.addHand('L0')
        return max(map(lambda x: len(str.rstrip(x)),self.hands['L0']))

    def addHand(self,hand):
        if hand[0:2] == 'UL':
            self.addUpsideDownLeftHand(hand)
        elif hand[0:2] == 'UR':
            self.addUpsideDownRightHand(hand)
        elif hand[0] == 'R':
            self.addRightHand(hand)
        else:
            self.addLeftHand(hand)

    def addRightHand(self,hand):
        left = 'L' + hand[1:]
        if left not in self.hands.keys():
            self.addHand(left)
        
        right_copy = []
        for a in range(len(self.hands[left])):
            line = self.hands[left][a].translate(str.maketrans('\\/<>','/\\><')) 
            right_copy.append(line[::-1])

        self.hands[hand] = right_copy

    def addLeftHand(self,hand):
        handfile = os.path.dirname(__file__) + f'/hands/{hand}.txt'
        with open(handfile,'r') as txt:
            lines = txt.readlines()
            lines = list(map(str.rstrip,lines))
            self.hands[hand] = lines

    def addUpsideDownLeftHand(self,hand):
        left = hand[1:]
        if left not in self.hands.keys():
            self.addLeftHand(left)
        
        copy = []
        for a in range(len(self.hands[left]))[::-1]:
            copy.append(self.hands[left][a].translate(str.maketrans('\\/<>','/\\><')))
        
        self.hands[hand] = copy
    
    def addUpsideDownRightHand(self,hand):
        right = hand[1:]
        if right not in self.hands.keys():
            self.addRightHand(right)
        
        copy = []
        for a in range(len(self.hands[right]))[::-1]:
            copy.append(self.hands[right][a].translate(str.maketrans('\\/<>','/\\><')))
        
        self.hands[hand] = copy

    def drawHands(self,left_count,right_count,upsideDown=0):
        my_left = f'L{left_count}' if not upsideDown else f'UL{right_count}'
        my_right = f'R{right_count}' if not upsideDown else f'UR{left_count}'
        for hand in [my_left,my_right]:
            if hand not in self.hands.keys():
                self.addHand(hand)
        
        for left,right in zip(self.hands[my_left],self.hands[my_right]):
            widthL = len(left)
            addSpacesL = self.handWidth - widthL + self.spaceBetweenHands
            
            widthR = len(right)
            addSpacesR = self.handWidth - widthR
            print(left + ' ' * (addSpacesL + addSpacesR) + right)
