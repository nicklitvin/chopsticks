import os

class Player:
    def __init__(self,name):
        self.name = name
        self.handL = 1
        self.handR = 1
        self.handWidth = self.getMaxWidth()
        self.space = 5

    def convertElementsToInt(self,arr):
        try:
            return list(map(lambda x: int(x),arr))
        except:
            pass

    def getMaxWidth(self):
        hand = os.path.dirname(__file__) + f'\L{self.handL}.txt'
        with open(hand,'r') as txt:
            line = txt.readlines()
            return len(max(map(str.rstrip,line),key=len))

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

    def drawUpsideDownHands(self):
        # handR is left hand but when upside down is on the right
        handR = os.path.dirname(__file__) + f'\L{self.handL}.txt'
        handL = os.path.dirname(__file__) + f'\L{self.handR}.txt'
        with open(handL,'r') as left, open(handR,'r') as right:
            leftLines = left.readlines()
            rightLines = right.readlines()
            for a in range(len(leftLines))[::-1]:
                lineL = leftLines[a].rstrip().translate(
                    str.maketrans('\\/<>','/\\><'))
                widthL = len(lineL)
                addSpacesL = self.handWidth - widthL + self.space

                lineR = rightLines[a].rstrip()
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
            conversion = self.convertElementsToInt(newSplit)

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
        if hand == 'l':
            return self.handL
        elif hand == 'r':
            return self.handR
        else:
            raise AssertionError('hand:',hand)

    def takeHit(self,handLetter,value):
        if handLetter == 'l':
            self.handL += value
        elif handLetter == 'r':
            self.handR += value
        else:
            raise AssertionError('handLetter error')

        self.reduceHands()

