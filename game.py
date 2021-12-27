from components.player import Player

class Game:
    def __init__(self):
        self.mainPlayer = None
        self.otherPlayer = None
        self.p1 = None
        self.p2 = None
        self.linebreak = '--------'
        self.gaming = True
        self.winner = None

        self.assignNames()
        self.run()
    
    def assignNames(self):
        p1_name = input('name of player1?')
        p2_name = input('name of player2?')

        self.p1 = Player(p1_name)
        self.p2 = Player(p2_name)
        self.mainPlayer = self.p1
        self.otherPlayer = self.p2

    def draw(self):
        print(self.linebreak)
        print(f'{self.mainPlayer.name}\'s turn')
        self.p1.drawHands()
        self.p2.drawHands()

    def isGameOver(self):
        if self.p1.isDead() or self.p2.isDead():
            return True

    def endScreen(self):
        self.winner = self.p1 if self.p2.isDead() else self.p2


        print(self.linebreak)
        self.draw()
        print(f'winner:{self.winner.name}')
        print(self.linebreak)

        end = input('keep going?')

        if not end:
            self.gaming = False

    def run(self):
        while self.gaming:
            self.draw()
            self.mainPlayer.makeTurn(self.otherPlayer)
            self.mainPlayer = self.p1 if self.mainPlayer == self.p2 else self.p2
            self.otherPlayer = self.p1 if self.mainPlayer == self.p2 else self.p2
            
            if self.isGameOver():
                self.endScreen()

        print('closing terminal')

import doctest
doctest.testmod()
Game()
