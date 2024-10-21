import numpy as np
        
        

class verticle:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__arr = np.full((15,1), 2)
    def move(self,obj):
        if(self.__y > 0):
            unslice = np.full((15,1), 1)
            if(len(np.where(obj.arr[self.__x : self.__x + 15 , self.__y - 1 : self.__y ] == 5 )[1].tolist()) != 0 ):
                return -2
            if(len(np.where(obj.arr[self.__x : self.__x + 15 , self.__y - 1 : self.__y ] == 0 )[1].tolist()) == 0 ):
                obj.arr[self.__x : self.__x + 15, self.__y : self.__y + 1] = unslice
                self.__y -= 1
                obj.arr[self.__x : self.__x + 15, self.__y : self.__y + 1] = self.__arr
                return 1
            else:
                obj.arr[self.__x : self.__x + 15, self.__y : self.__y + 1] = unslice
                return -1
        return 0
    def reset(self,obj):
        obj.arr[self.__x : self.__x + 15 , self.__y: self.__y+1] = np.full((15,1), 1)
        

class horizontal:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__arr = np.full((1,15), 2)
    def move(self,obj):
        if(self.__y > 0):
            unslice = np.full((1,15), 1)
            if(len(np.where(obj.arr[self.__x : self.__x + 1 , self.__y -1 : self.__y + 14 ] == 5 )[1].tolist()) != 0 ):
                return -2  
            if(len(np.where(obj.arr[self.__x : self.__x + 1 , self.__y -1 : self.__y + 14 ] == 0 )[1].tolist()) == 0 ):
                obj.arr[self.__x : self.__x + 1, self.__y : self.__y + 15] = unslice
                self.__y -= 1
                obj.arr[self.__x : self.__x + 1, self.__y : self.__y + 15] = self.__arr
                return 1
            else:
                obj.arr[self.__x : self.__x + 1, self.__y : self.__y + 15] = unslice
                return -1
        return 0
    def reset(self,obj):
        obj.arr[self.__x : self.__x + 1 , self.__y : self.__y + 15 ] = np.full((1,15), 1)
        
    
class diagonaldown:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__arr = np.full((15,15), 1)
        for i in range(15):
            self.__arr[i,i] = 2
        
    def move(self,obj):
        if(self.__y > 0):
            unslice = np.full((15,15), 1)
            newarr = obj.arr[self.__x : self.__x + 15, self.__y -1  : self.__y + 14]
            flag = 0
            for i in range(15):
                if(newarr[i,i] == 0):
                    flag = 1
            for i in range(15):
                if(newarr[i,i] == 5):
                    flag = 2
            if flag == 2:
                return -2
            if(flag == 0):
                for i in range(15):
                    obj.arr[self.__x + i, self.__y + i] = 1
                self.__y -= 1
                for i in range(15):
                    obj.arr[self.__x + i, self.__y + i] = 2
                return 1
            else:
                for i in range(15):
                    obj.arr[self.__x + i, self.__y + i] = 1
                return -1
        return 0
    def reset(self,obj):
        for i in range(15):
            obj.arr[self.__x + i, self.__y + i] = 1
        
            
class Magnet:
    def __init__(self, y):
        self.__x = 0
        self.__y = y
        self.__flag = 0
        self.__arr = np.full((1,5),4)
        
    def move(self,obj):
        if(self.__y > 18):
            unslice = np.full((1,5), 1)
            obj.arr[self.__x : self.__x + 1, self.__y : self.__y + 5] = unslice
            self.__y -= 1
            obj.arr[self.__x : self.__x + 1, self.__y : self.__y + 5] = self.__arr
        else:
            unslice = np.full((1,5), 1)
            self.__arr = np.full((1,5),1)
            obj.arr[self.__x : self.__x +1, self.__y : self.__y + 5] = unslice 
        self.__flag += 1
    def getflag(self):
        return self.__flag
        return 0
        