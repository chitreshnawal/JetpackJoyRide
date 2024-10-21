import numpy as np
from person import *
from Background import *
from obstacle import *
from colorama import Back,Fore,Style
from Background import *
import sys
class Game :
    def printarr(arr):
        for i in arr:
            for j in i[18:191]:
                if(j == 0 or j == 2 or j == 5 or j == 6):
                    print(Style.RESET_ALL,end="")
                    print(Fore.BLACK + Back.BLACK,end="")
                    print(j,end="")
                    print(Style.RESET_ALL,end="")
                    print(Fore.RED + Back.RED,end="")
                elif j == 3:
                    print(Style.RESET_ALL,end="")
                    print(Fore.LIGHTYELLOW_EX + Back.RED,end="")
                    print('$',end="")
                    print(Style.RESET_ALL,end="")
                    print(Fore.RED + Back.RED,end="")
                elif j == 7:
                    print(Style.RESET_ALL,end="")
                    print(Fore.LIGHTYELLOW_EX + Back.LIGHTYELLOW_EX,end="")
                    print(j,end="")
                    print(Style.RESET_ALL,end="")
                    print(Fore.RED + Back.RED,end="")
                elif j == 4:
                    print(Style.RESET_ALL,end="")
                    print(Fore.BLACK + Back.WHITE,end="")
                    print(j,end="")
                    print(Style.RESET_ALL,end="")
                    print(Fore.RED + Back.RED,end="")
                else:
                    print(j, end="")
            print()
        return 1
    def printBack(self,obj,Top):
        Top.updatescore()
        skyarr = obj.sky()
        groundarr = obj.ground()
        bodyarr = obj.body()
        print("\033[0;0H", end="")
        print("\033[0K",end="")
        Top.updateboost()
        print("SCORE : " + str(Top.getscore()) + "\t COINS: " + str(Top.getcoins()) + "\t Boost available after:" + str(Top.getboost()) + "\t Shield available after: "+str(Top.getShield()) + "\t Shield Timer : " + str(Top.gettimer()) + "\t Lives : " + str(Top.getlife()))
        print(Fore.BLUE,end="")
        Game.printarr(skyarr)
        print(Style.RESET_ALL,end="")
        print(Fore.RED + Back.RED,end="")
        Game.printarr(bodyarr)
        print(Style.RESET_ALL,end="")
        print(Fore.GREEN,end="")
        Game.printarr(groundarr)
        print(Style.RESET_ALL,end="")
        # print("\033[0;0H", end="")
            
    