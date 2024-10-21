import numpy as np

class coins:
    
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__arr = np.full((1,1),3)
    def move(self,obj):
        if(self.__y > 0):
            unslice = np.full((1,1), 1)
            if(len(np.where(obj.arr[self.__x : self.__x + 1 , self.__y - 1 : self.__y ] == 2 )[1].tolist()) != 0 ):
                return 3
            if(len(np.where(obj.arr[self.__x - 1 : self.__x + 2 , self.__y - 1 : self.__y ] == 0 )[1].tolist()) == 0 ):
                obj.arr[self.__x : self.__x + 1, self.__y : self.__y + 1] = unslice
                self.__y -= 1
                obj.arr[self.__x : self.__x + 1, self.__y : self.__y + 1] = self.__arr
                return 1
            else:
                obj.arr[self.__x : self.__x + 1, self.__y : self.__y + 1] = unslice
                return 2
        return 0
        