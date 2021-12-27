import os

def convertElementsToInt(arr):
    """
    >>> convertElementsToInt(['1','2'])
    [1, 2]
    >>> convertElementsToInt(['1','2b'])
    """
    try:
        return list(map(lambda x: int(x),arr))
    except:
        pass

class Player:
    def __init__(self,name):
        self.name = name
        self.handL = 4
        self.handR = 3
        self.handWidth = self.getMaxWidth()
        self.space = 5

    def getMaxWidth(self):
        hand = os.path.dirname(__file__) + f'\L{self.handL}.txt'
        with open(hand,'r') as txt:
            line = txt.readlines()
            return len(max(line,key=len))

    def drawHands(self):
        handL = os.path.dirname(__file__) + f'\L{self.handL}.txt'
        handR = os.path.dirname(__file__) + f'\L{self.handR}.txt'
        with open(handL,'r') as left, open(handR,'r') as right:
            leftLines = left.readlines()
            rightLines = right.readlines()
            for a in range(len(leftLines)):
                lineL = leftLines[a].rstrip() 
                widthL = len(lineL)
                addSpacesL = self.handWidth - widthL + self.space

                lineR = rightLines[a].rstrip().translate(
                    str.maketrans('\\/<>','/\\><'))
                widthR = len(lineR)
                addSpacesR = self.handWidth - widthR
                print(lineL + ' ' * (addSpacesL + addSpacesR) + lineR[::-1])

    def isDead(self):
        if sum((self.handL,self.handR)) == 0:
            return True
    
    def makeTurn(self,opponent):
        while True:
            turn = input('split or hit?')
            
            if turn == 'split' and self.handL + self.handR > 1:
                self.split()
                break
            elif turn == 'hit':
                self.hit(opponent)
                break
            else:
                print('incorrect move')

    def split(self):
        while True:
            newSplit = input('how many on each hand? ')
            newSplit = newSplit.split(' ')
            conversion = convertElementsToInt(newSplit)

            if not conversion or len(conversion) != 2:
                print('bad input')
                continue

            newL = conversion[0]
            newR = conversion[1] 

            if newL == self.handL and newR == self.handR or \
               newR == self.handL and newL == self.handR:
                print('no change')
                continue

            if newL + newR == self.handL + self.handR:
                self.handL = newL
                self.handR = newR
                self.reduceHands()
                break

            else:
                print('bad split, try again')

    def reduceHands(self):
        """
        >>> p1 = Player('p1')
        >>> p1.handR = 3
        >>> p1.handL = 9
        >>> p1.reduceHands()
        >>> p1.handL
        4
        >>> p1.handR
        3
        """
        self.handL = self.handL % 5
        self.handR = self.handR % 5

    def hit(self,opponent):
        while True:
            my_hand = input(f'Which hand (L,R) hits {opponent.name}: ')
            opp_hand = input('Which hand do you hit? ')
            options = ('l','r')
            
            if not isinstance(my_hand,str) or not isinstance(opp_hand,str):
                print('not numbers')
                continue

            my_hand = my_hand.lower()
            opp_hand = opp_hand.lower()

            if self.getHandVal(my_hand) == 0:
                print("can't hit with 0")
                continue

            if opponent.getHandVal(opp_hand) == 0:
                print("can't hit a 0")
                continue

            if not my_hand in options or not opp_hand in options:
                print('bad input')
                continue
            else:
                my_hand_val = self.getHandVal(my_hand)
                opponent.takeHit(opp_hand,my_hand_val)
                break

    def getHandVal(self,hand):
        """
        >>> p1 = Player('p1')
        >>> p1.handL = 3
        >>> p1.getHandVal('l')
        3
        >>> p1.getHandVal('r')
        1
        """
        if hand == 'l':
            return self.handL
        elif hand == 'r':
            return self.handR
        else:
            AssertionError('hand:',hand)

    def takeHit(self,handLetter,value):
        """
        >>> p1 = Player('p1')
        >>> p1.takeHit('r',2)
        >>> p1.handL
        1
        >>> p1.handR
        3
        """
        if handLetter == 'l':
            self.handL += value
        elif handLetter == 'r':
            self.handR += value
        else:
            raise AssertionError('handLetter error')
        self.reduceHands()

import doctest
doctest.testmod()
