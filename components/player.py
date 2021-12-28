class Player:
    options = ('l','r')

    def __init__(self,name,hands):
        self.name = name
        self.handL = 1
        self.handR = 1
        self.hands = hands

    def convertElementsToInt(self,arr):
        try:
            return list(map(lambda x: int(x),arr))
        except ValueError:
            pass

    def drawHands(self,reversed=0):
        self.hands.drawHands(self.handL,self.handR,reversed)

    def isDead(self):
        if sum((self.handL,self.handR)) == 0:
            return True
    
    def makeTurn(self,opponent,test_turn=None):
        while True:
            turn = input('split or hit?').lower() if not test_turn else test_turn

            if 'split' in turn and self.handL + self.handR > 1:
                self.split()
                break
            elif 'hit' in turn:
                self.hit(opponent)
                break
            else:
                print('incorrect move')

    def split(self,test_newSplit=None):
        while True:
            newSplit =  input('how many on each hand? (ex: 2 0): ') \
                        if not test_newSplit else test_newSplit

            newSplit = "".join(newSplit.split(' '))
            conversion = self.convertElementsToInt(newSplit)

            if self.isGoodSplit(conversion):
                self.handL, self.handR = conversion
                self.reduceHands()
                break

            if test_newSplit:
                raise Exception('Bad test_newSplit')
    
    def isGoodSplit(self,conversion):
        if not conversion or len(conversion) != 2:
            print('bad input')
            return

        newL,newR = conversion

        if newL == self.handL and newR == self.handR or \
            newR == self.handL and newL == self.handR:
            print('no change')
            return

        if newL + newR != self.handL + self.handR:
            print('bad split, try again')
            return
        
        return True

    def reduceHands(self):
        self.handL = self.handL % 5
        self.handR = self.handR % 5

    def hit(self,opponent,test_answer = None):
        while True:
            if test_answer:
                my_hand,opp_hand = test_answer
            else:
                my_hand = input(f'Which hand (L,R) hits {opponent.name}: ')
                opp_hand = input('Which hand do you hit (your left or right)? ')

            if self.isLegalHit(opponent,my_hand,opp_hand):
                my_hand, opp_hand = my_hand.lower(), opp_hand.lower()
                opp_hand =  Player.options[0] if opp_hand == Player.options[1] \
                            else Player.options[1]
                            
                my_hand_val = self.getHandVal(my_hand)
                opponent.takeHit(opp_hand,my_hand_val)
                break

    def isLegalHit(self,opponent,my_hand,opp_hand):
        if not (isinstance(my_hand,str) and isinstance(opp_hand,str)):
            print('not numbers')
            return

        my_hand, opp_hand = my_hand.lower(), opp_hand.lower()
        opp_hand =  Player.options[0] if opp_hand == Player.options[1] \
                    else Player.options[1]

        if not (my_hand in Player.options and opp_hand in Player.options):
            print('bad input')
            return

        if self.getHandVal(my_hand) == 0:
            print("can't hit with 0")
            return

        if opponent.getHandVal(opp_hand) == 0:
            print("can't hit a 0")
            return

        return True

    def getHandVal(self,hand):
        if hand == 'l':
            return self.handL
        elif hand == 'r':
            return self.handR
        else:
            raise Exception('hand not l or r')

    def takeHit(self,handLetter,value):
        if handLetter == 'l':
            self.handL += value
        elif handLetter == 'r':
            self.handR += value
        else:
            raise Exception('handLetter not l or r')

        self.reduceHands()

