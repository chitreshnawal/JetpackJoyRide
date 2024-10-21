import numpy as np
from colorama import Fore,Back,Style
from person import *
class bullet:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__arr = np.full((1,1),5)
        self.__hit = False
    def move(self,obj):
        if(self.__y < 200):
            # if boss:
            #     if(len(np.where(obj.arr[self.__x: self.__x + 1 , self.__y + 1 : self.__y+2] == 6 )[1].tolist()) == 0):
            #         obj.arr[self.__x,self.__y] = 1
            #         self.__y += 1
            #         obj.arr[self.__x,self.__y] = 5
            #     else:
            #         obj.arr[self.__x,self.__y] = 1
            #         return -1
            if(len(np.where(obj.arr[self.__x: self.__x + 1 , self.__y + 1 : self.__y+2] == 2 )[1].tolist()) == 0):
                obj.arr[self.__x,self.__y] = 1
                self.__y += 1
                obj.arr[self.__x,self.__y] = 5
            else:
                return -1                
        else:
            self.__arr = np.full((1,1),1)
            self.__hit = True
        return
    def bullet_hit(self):
        self.__hit = True
    def reset(self,obj):
        obj.arr[self.__x,self.__y] = 1
        return
class bossbullet(bullet):
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__arr = np.full((1,1),5)
        self.__hit = False
        
    def move(self,obj):
        if(self.__y < 200):
            if(len(np.where(obj.arr[self.__x: self.__x + 1 , self.__y + 1 : self.__y+2] == 6 )[1].tolist()) == 0):
                obj.arr[self.__x,self.__y] = 1
                self.__y += 1
                obj.arr[self.__x,self.__y] = 5
            else:
                obj.arr[self.__x,self.__y] = 1
                return -1
     
class enemybullet:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__arr = np.full((1,1),7)
        self.__hit = False
    def move(self,obj):
        if(self.__y >17):
            if(len(np.where(obj.arr[self.__x - 1 : self.__x + 1 , self.__y - 1 : self.__y] == 0 )[1].tolist()) == 0):
                obj.arr[self.__x,self.__y] = 1
                self.__y -= 1
                obj.arr[self.__x,self.__y] = 7
            else:
                obj.arr[self.__x,self.__y] = 1
                return -6                
        else:
            self.__arr = np.full((1,1),1)
            self.__hit = True
        return
        
class topbar:
    def __init__(self):
        self.__score = 0
        self.__coins = 0
        self.__speeedBoost = 0
        self.__Shield = 0
        self.__timer = -1
        self.__Shieldactive = False
        self.__firstlife = 5
    def default_timer(self):
        self.__timer = -1
    def set_timer(self):
        self.__timer = 167
    def update_timer(self):
        if self.__timer > 0 :
            self.__timer -= 1
    def updateShield(self):
        b = not(self.__Shieldactive)
        self.__Shieldactive =  b
    def setShieldTime(self):
        self.__Shield = 1000
    def updateShieldTime(self):
        if(self.__Shield > 0):
            self.__Shield -= 1
    def updateboost(self):
        if(self.__speeedBoost > 0):
            self.__speeedBoost -= 1
    def assignboost(self):
        self.__speeedBoost = 150
    def updatescore(self):
        self.__score += 1
    def updatecoins(self):
        self.__coins += 1
    def getShield(self):
        return self.__Shield
    def getscore(self):
        return self.__score
    def getcoins(self):
        return self.__coins
    def getboost(self):
        return self.__speeedBoost
    def gettimer(self):
        return self.__timer
    def updatefirstLife(self):
        self.__firstlife -= 1
        if(self.__firstlife < 0):
            return -1
    def getlife(self):
        return self.__firstlife

class backgroud:
    
    def __init__(self):
        self.arr = np.full((39,213),1)
        self.shield = False 
    def sky(self):
        arr = np.full((5, 213),'+')
        return arr
    def ground(self):
        arr = np.full((5, 213),'$')
        return arr
    def body(self):
        return self.arr
    def reallocate(self):
        self.arr = np.full((39,213),1)
        self.shield = False 
    
class enemyallotment:
    def __init__(self):
        self.__allot = []
        self.__flag = 0
    def moveall(self,obj,Top,person,boss):
        if(boss):
            removelist = []
            enemy = 0
            hero = 0
            for i in self.__allot:
                v = i.move(obj)
                if(v == -1):
                    enemy += 1
                    removelist.append(i)
                if(v == -6):
                    hero += 1
                    removelist.append(i)
            for i in removelist:
                self.__allot.remove(i)
            return [enemy,hero]                
        v = 0
        removelist = []
        resetlist = []
        magnetx = np.where(obj.arr == 4)[0].tolist()
        magnety = np.where(obj.arr == 4)[1].tolist()
        if(len(magnetx) > 0 and self.__flag % 2 == 0):
            if(person.get_current_y() < magnety[1]):
                person.moveR(obj)
            else:
                person.moveL(obj)
            # if(person.get_current_x() > magnetx[1]):
            #     person.moveU(obj)
        for i in self.__allot :
            v = i.move(obj)
            if(v == -1):
                if(type(i) == bullet):
                    removelist.append(i)
                    resetlist.append(i)
                elif(obj.shield):
                    removelist.append(i)
                else:
                    return -1
            if v == -2 :
                resetlist.append(i)
                removelist.append(i)
            if(v == 2):
                Top.updatecoins()
                removelist.append(i)
            if(v == 3):
                removelist.append(i)
        for i in resetlist:
            i.reset(obj)
        for i in removelist:
            self.__allot.remove(i)
        self.__flag += 1    

    def addobstacle(self,obj):
        self.__allot.append(obj) 
    
# def printarr(arr):
#     for i in arr:
#         for j in i[18:191]:
#             print(j, end="")
#         print()    
# # code to print the background
# print("\033[0;0H", end="")
# obj = backgroud()
# skyarr = obj.sky()
# groundarr = obj.ground()
# bodyarr = obj.body()
# print(Fore.BLUE,end="")
# printarr(skyarr)
# print(Style.RESET_ALL,end="")
# # print(Fore.RED + Back.RED,end="")
# printarr(bodyarr)
# print(Style.RESET_ALL,end="")
# print(Fore.GREEN,end="")
# printarr(groundarr)
# print(Style.RESET_ALL,end="")
# # print("\033[5;0H This is just to test cursor movement", end="")



 
        