import sys 
from os import system
import select 
import tty 
import termios
from termios import tcflush,TCIFLUSH
import time
from game import *
from Background import *
from person import *
from obstacle import *
import random
def isData():
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

old_settings = termios.tcgetattr(sys.stdin)
try:
    tty.setcbreak(sys.stdin.fileno())
    system('clear')
    objback = backgroud()
    objper = Hero(5,5)
    mainobj = Game()
    obstacle = enemyallotment()
    flag = 0
    while 1:
        mainobj.printBack(objback)
        sys.stdout.flush()
        if isData():
            tcflush(sys.stdin, TCIFLUSH)
            obst = list(range(3))
            if(flag % 35 == 0):
                s = random.choice(obst)
                if s == 0 :
                    obstacle.addobstacle(verticle(random.choice(list(range(0,9))),181))
                if s == 1 :
                    obstacle.addobstacle(horizontal(random.choice(list(range(0,30))),181))
                if s == 2 :
                    obstacle.addobstacle(diagonaldown(random.choice(list(range(0,9))),181))
            if(flag%2 == 0):
                obstacle.moveall(objback)
            c = sys.stdin.read(1)
            if c == 'q':         # x1b is ESC
                break
            if c == 'd' :
                objper.moveR(objback)
            if c == 'a' :
                objper.moveL(objback)
        flag += 1
        time.sleep(0.0334)
finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)