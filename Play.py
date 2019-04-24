from time import sleep
### to show the errors!
from pyfiglet import figlet_format
### to show theme more beautiful.
from random import randint, choice
### we need random to develope the cpu section!

class Player(object):

    """
    We have to have players to play! this class will do that for us!
    so use it to create a player. it includes the player's character and
    the game that the player is playing on.
    """

    def __init__(self, char, game):
        self.CHAR = char[0]
        self._game = game

    @property
    def GAME(self):
        return self._game
        ### now you have access to the orriginal table whenever it changes.

    def play(self):

        """
        When you have your game and your players, just run it! it asks for the
        point you want to change and simply just does that for you!
        """

        is_done = False
        while not is_done:
            self.GAME.display_table()
            tmp = input('{}s turn: '.format(self.CHAR))
            try:
                if self.GAME.TABLE[int(tmp[0])-1][int(tmp[1]) - 1] == '-' and len(tmp) == 2:
                    self.GAME.TABLE[int(tmp[0])-1][int(tmp[1]) -1] = self.CHAR
                    self.GAME.COUNTER += 1
                    is_done = True
                else:
                    print(figlet_format('-ERROR-'))
                    sleep(2)
            except:
                print(figlet_format('-ERROR-'))
                sleep(2)


class Cpu(object):

    """
    Create a virtual player by using this class! :)
    """

    def __init__(self, char, game, playerchar):
        self.CHAR = char
        self._game = game
        self.ENEMY = playerchar

    @property
    def GAME(self):
        return self._game
        ### getting access to the orriginal table

    def play(self):

        """
        Analizes the game table and decides by some conditions...
        """
        
        played = False
        while not played:
            ### first step, first move!
            if self.GAME.COUNTER <= 1:
                if choice([0, 1]):
                    ### trying for the center point:
                    if self.GAME.TABLE[1][1] == '-':
                        self.GAME.TABLE[1][1] = self.CHAR
                        self.GAME.COUNTER += 1
                        played = True
                else:
                    while True:
                        tmp = choice(['00', '02', '20', '22'])
                        ### trying for the corner points:
                        if self.GAME.TABLE[int(tmp[0])][int(tmp[1])] == '-':
                            self.GAME.TABLE[int(tmp[0])][int(tmp[1])] = self.CHAR
                            self.GAME.COUNTER += 1
                            played = True
                            break
            ### I wanna win! xD
            if self.GAME.COUNTER >= 3:
                ### Horizontal lines:
                for i in self.GAME.TABLE:
                    if i.count(self.CHAR) == 2 and i.count('-') == 1:
                        self.GAME.TABLE[self.GAME.TABLE.index(i)][i.index('-')] = self.CHAR
                        self.GAME.COUNTER += 1
                        played = True
                        break
                ### vertical lines:
                if not played:
                    for i in range(3):
                        tmp = list()
                        for j in self.GAME.TABLE:
                            tmp.append(j[i])
                        if tmp.count(self.CHAR) == 2 and tmp.count('-') == 1:
                            self.GAME.TABLE[tmp.index('-')][i] = self.CHAR
                            self.GAME.COUNTER += 1
                            played = True
                            break
                ### diagonal lines:
                if not played:
                    tmp = [self.GAME.TABLE[i][i] for i in range(3)]
                    if tmp.count(self.CHAR) == 2 and tmp.count('-') == 1:
                        self.GAME.TABLE[tmp.index('-')][tmp.index('-')] = self.CHAR
                        self.GAME.COUNTER += 1
                        played = True
                if not played:
                    ### sorry, I had to do it like that!
                    tmp = ['02', '11', '20']
                    temp = [self.GAME.TABLE[int(i[0])][int(i[1])] for i in tmp]
                    if temp.count(self.CHAR) == 2 and temp.count('-') == 1:
                        self.GAME.TABLE[temp.index('-')][int(tmp[temp.index('-')][1])] = self.CHAR
                        self.GAME.COUNTER += 1
                        played = True
                ### couldn't I win?! that's ok but I won't lose. :)
                if not played:
                    ### the same code up there; but this time I'm trying to not lose!
                    for i in self.GAME.TABLE:
                        if i.count(self.ENEMY) == 2 and i.count('-') == 1:
                            self.GAME.TABLE[self.GAME.TABLE.index(i)][i.index('-')] = self.CHAR
                            self.GAME.COUNTER += 1
                            played = True
                            break
                    if not played:
                        for i in range(3):
                            tmp = list()
                            for j in self.GAME.TABLE:
                                tmp.append(j[i])
                            if tmp.count(self.ENEMY) == 2 and tmp.count('-') == 1:
                                self.GAME.TABLE[tmp.index('-')][i] = self.CHAR
                                self.GAME.COUNTER += 1
                                played = True
                                break
                    if not played:
                        tmp = [self.GAME.TABLE[i][i] for i in range(3)]
                        if tmp.count(self.ENEMY) == 2 and tmp.count('-') == 1:
                            self.GAME.TABLE[tmp.index('-')][tmp.index('-')] = self.CHAR
                            self.GAME.COUNTER += 1
                            played = True
                    if not played:
                        tmp = ['02', '11', '20']
                        temp = [self.GAME.TABLE[int(i[0])][int(i[1])] for i in tmp]
                        if temp.count(self.ENEMY) == 2 and temp.count('-') == 1:
                            self.GAME.TABLE[temp.index('-')][int(tmp[temp.index('-')][1])] = self.CHAR
                            self.GAME.COUNTER += 1
                            played = True
            if not played:
                is_done = False
                for i in self.GAME.TABLE:
                    for j in i:
                        if j == '-':
                            self.GAME.TABLE[self.GAME.TABLE.index(i)][i.index(j)] = self.CHAR
                            self.GAME.COUNTER += 1
                            played = True
                            is_done = True
                            break
                    if is_done:
                        break

