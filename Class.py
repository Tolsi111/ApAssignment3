class myPoint:#PointRepository
    '''
    myPoint is a structure with 3 elements: the x coordinate (number), the y coordinate (number) and the colour of the 
    point (string)
    '''
    def __init__(self,x,y,c):
        '''
        creates a new instance of a point
        '''
        self.__coord_x = x
        self.__coord_y = y
        if c == "red" or c == "green" or c == "blue" or c == "yellow" or c == "magenta":
            self.__colour = c
        else:
            raise ValueError("the color must be one from the list:‘red’, ‘green’, ‘blue’, ‘yellow’ and ‘magenta’")
        self.__colour = c
    def setX(self,x):
        if type(x) != int and not x.isnumeric():
            raise ValueError("x coordinate must be a number")
        self.__coord_x = x
    def getX(self):
        return self.__coord_x
    def setY(self,y):
        if type(y) != int and not y.isnumeric():
            raise ValueError("y coordinate must be a number")
        self.__coord_y = y
    def getY(self):
        return self.__coord_y
    def setColour(self,c):
        if c == "red" or c == "green" or c == "blue" or c == "yellow" or c == "magenta":
            self.__colour = c
        else:
            raise ValueError("the color must be one from the list:‘red’, ‘green’, ‘blue’, ‘yellow’ and ‘magenta’")
    def getColour(self):
        return self.__colour
    def __str__(self):
        #returns a string representation of the point
        P = "Point (" + str(self.__coord_x) + "," + str(self.__coord_y) + ") of color " + self.__colour
        return P