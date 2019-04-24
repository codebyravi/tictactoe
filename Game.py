from subprocess import call
### to clean the terminal.
from time import sleep
### too show the winner.
from pyfiglet import figlet_format
### display more beautiful!

class Game(object):

    """
    This is a class that that can basically initialize the game!
    it includes the table and some methods to work with.
    """

    def __init__(self, X='X', O='O'):
        self.OCHAR = O
        self.XCHAR = X
        ### maybe the players wanted to know about their score!
        self.SCOREBOARD = {self.XCHAR: int(), self.OCHAR: int()}

    def set_table(self):

        """
        by running this method, you'v just created a table that players
        can play on it!
        """

        self.TABLE = [['-' for i in range(3)] for j in range(3)]
        self.COUNTER = 0

    def display_table(self):

        """
        yeah it just prints the table you created before!
        """

        call('clear', shell=True)
        ### now the terimnal is clean af!
        print(figlet_format('{}: {}, {}: {}'.format(self.XCHAR, self.SCOREBOARD[self.XCHAR], self.OCHAR, self.SCOREBOARD[self.OCHAR])))
        print('\n')
        tmp = str()
        for i in self.TABLE:
            for j in i:
                tmp += j
                tmp += '     '
            tmp += '\n'
        print(figlet_format(tmp))

    def check_the_table(self):

        """
        one of the most important methods of the hole class;
        by running this method, you will analyze the table and
        look for the winner.
        """

        win = False
        ### did anybody win?!
        ### analyzing horizontal & vertical lines: {
        if not win:
            for i in self.TABLE:
                if i.count(i[0]) == 3:
                    if i[0] != '-':
                        win = True
                        self.SCOREBOARD[i[0]] += 1
                        self.display_table()
                        print(figlet_format('{} won the game!'.format(i[0])))
                        self.set_table()
                        sleep(2)
        if not win:
            for i in range(3):
                tmp = list()
                for j in self.TABLE:
                    tmp.append(j[i])
                    if tmp.count(tmp[0]) == 3:
                        if tmp[0] != '-':
                            win = True
                            self.SCOREBOARD[tmp[0]] += 1
                            self.display_table()
                            print(figlet_format('{} won the game!'.format(tmp[0])))
                            self.set_table()
                            sleep(2)
        ### }
        ### analyzing diagonal lines{
        if not win:
            tmp = [self.TABLE[i][i] for i in range(3)]
            if tmp.count(tmp[0]) == 3:
                if tmp[0] != '-':
                    win = True
                    self.SCOREBOARD[tmp[0]] += 1
                    self.display_table()
                    print(figlet_format('{} won the game!'.format(tmp[0])))
                    self.set_table()
                    sleep(2)
        if not win:
            tmp = [self.TABLE[0][2], self.TABLE[1][1], self.TABLE[2][0]]
            if tmp.count(tmp[0]) == 3:
                if tmp[0] != '-':
                    win = True
                    self.SCOREBOARD[tmp[0]] += 1
                    self.display_table()
                    print(figlet_format('{} won the game!'.format(tmp[0])))
                    self.set_table()
                    sleep(2)
        ### }
        ### what if nobody couldn't win!?
        if not win:
            if self.COUNTER >= 9:
                win = True
                self.display_table()
                print(figlet_format('no one won!'))
                self.set_table()
                sleep(2)
