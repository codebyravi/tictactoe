import Game, Play
### inintial moudles!
from pyfiglet import Figlet
### have some UI! :)
from subprocess import call
### we'll have to clean the terminal!
from time import sleep
### I just wanna introduce my self! :/
from argparse import ArgumentParser
from sys import stdout
### for the arguments

### introducing :)
painter = Figlet(font='graffiti')
print(painter.renderText('tictactoe'))
print('https://github.com/codebyravi/tictactoe.git')
sleep(4)


def r(args):
        if args.mode == 'multi':
                call('clear', shell=True)
                print(painter.renderText('1st player!'))
                Xchar = input('enter your favorit character: ')

                call('clear', shell=True)
                print(painter.renderText('2nd player!'))
                Ochar = input('enter your favorit character: ')

                game = Game.Game(X=Xchar, O=Ochar)
                game.set_table()
                Xplayer = Play.Player(Xchar, game)
                Oplayer = Play.Player(Ochar, game)
                
                while True:
                        Xplayer.play()
                        game.check_the_table()
                        Oplayer.play()
                        game.check_the_table()

        elif args.mode == 'single':
                call('clear', shell=True)
                print(painter.renderText('let\'s play!'))
                Pchar = input('enter your favorit character :')

                game = Game.Game(X=Pchar, O='X' if Pchar != 'X' else 'O')
                game.set_table()
                player = Play.Player(Pchar, game)
                cpu = Play.Cpu('X' if Pchar != 'X' else 'O', game, Pchar)

                while True:
                        player.play()
                        game.check_the_table()
                        cpu.play()
                        game.check_the_table()


def main():
        p = ArgumentParser()
        p.add_argument('--mode', type=str, default='single',
                       help='which mode do you wnat me to run in?! (single, multi)')
        args = p.parse_args()
        stdout.write(str(r(args)))

if __name__ == '__main__':
        main()
