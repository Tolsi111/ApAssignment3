from Class import myPoint
import math
import matplotlib.pyplot as plt

def validNumber(x):
    '''
    Forces the user to insert a number
    '''
    while not x.isnumeric() and not x[1:].isnumeric():
        x = input("please insert a number: ")
    return int(x)

def validIndex(l,i):
    '''
    Forces the user to input a valid index "i" for the list "l"
    '''
    while True:
        if i.isnumeric():
            if 0 <= int(i) and int(i) < len(l):
                break
        i = input("invalid index, please insert a valid one: ")
    return int(i)

def addPoint(l,x,y,c):
    '''
    Adds a point to the repository l(list)
    '''
    try:
        p = myPoint(x,y,c)
        l.append(p)
    except ValueError as msg:
        print(str(msg))

def getAllPoints(l):
    '''
    Prints the string representation of all the points from the list "l"
    '''
    for elem in l:
        print(elem.__str__())

def getPointGivenIndex(l,i):
    '''
    Prints the string representation of the point at the index "i" from the list "l"
    '''
    print(l[i].__str__())

def isInSquare(x,y,a,b,length):
    '''
    checks if a point (a,b) is situated inside the square with the up-left corner (x,y) and the length "len"
    '''
    if (x <= a and a <= x+length) and (y >= b and b >= y-length):
        return True
    else:
        return False

def getPointsSquare(l,x,y,length):
    '''
    Prints all points that are inside a given square: up-left corner (x,y) and "length" given from the list "l"
    '''
    for elem in l:
        if isInSquare(int(x),int(y),elem.getX(),elem.getY(),length):
            print(elem.__str__())

def getMinDistance(l):
    '''
    Returns the minimum distance between two points from the list "l"
    '''
    mini = -1
    for i in range (len(l)-1):
        for j in range(i+1,len(l)):
            d = getDistance(l,i,j)
            if d < mini or mini == -1:
                mini = d
    return mini

def getDistance(l,a,b):
    '''
    Returns the value of the distance between the points "a" and "b" from the list of points "l"
    a,b - index of the points
    '''
    return math.sqrt((l[b].getX()-l[a].getX())*(l[b].getX()-l[a].getX())+(l[b].getY()-l[a].getY())*(l[b].getY()-l[a].getY()))

def updatePoint(l,i,x,y,c):
    '''
    Updates the values of a point at a given index "i" from the list "l"
    x - new x coordinate
    y - new y coordinate
    c - new color
    '''
    l[i].setX(x)
    l[i].setY(y)
    l[i].setColour(c)

def deletePoint(l,i):
    '''
    Deletes the point with the index "i" from the list "l"
    '''
    del l[i]

def deleteByCoord(l,x,y):
    '''
    Deletes the point with the index "i" from the list "l"
    '''
    for i in range(len(l)):
        if l[i].getX() == x and l[i].getY() == y:
            del l[i]
            break

def deleteFromSquare(l,x,y,length):
    '''
    Deletes all the points situated inside a given square
    x - the x coordinate of the top-left vertex of the square
    y - the y coordinate of the top-left vertex of the square
    length - the length of one side of the square
    '''
    for i in range(len(l)-1,-1,-1):
        if isInSquare(x,y,l[i].getX(),l[i].getY(),length):
            deletePoint(l,i)

def plotPoints(l):
    x = []
    y = []
    col = []
    for elem in l:
        x.append(elem.getX())
        y.append(elem.getY())
        col.append(elem.getColour())
    plt.scatter(x, y, c = col)
    plt.show()

def getAllColour(l,c):
    '''
    Prints all the points form the list "l" with the colour "c"
    '''
    for elem in l:
        if elem.getColour() == c:
            print(elem.__str__())

#ITERATION 2 STARTS FROM HERE!


def getPointsRectangle(l,x,y,length,width):
    '''
    Prints all points that are inside a given rectangle: up-left corner (x,y), "length" and "width" given, from the list "l"
    '''
    for elem in l:
        a = int(elem.getX())
        b = int(elem.getY())
        if (int(x) <= a and a <= int(x)+length) and (int(y) >= b and b >= int(y)-width):
            print(elem.__str__())

def isInCircle(x,y,r,a,b):
    '''
    Checks if a point (a,b) is situated inside the circle of center (x,y) and radius "r"
    '''
    distance = math.sqrt((a-x)*(a-x)+(b-y)*(b-y))
    if distance <= r:
        return True
    else:
        return False

def getPointsCircle(l,x,y,r):
    '''
    Prints all points that are inside a given circle: of center (x,y) and radius "r" given, from the list "l"
    '''
    for elem in l:
        if isInCircle(x,y,r,elem.getX(),elem.getY()):
            print(elem.__str__())

def getMaxDistance(l):
    '''
    Returns the maximum distance between two points from the list "l"
    '''
    maxi = 0
    for i in range (len(l)-1):
        for j in range(i+1,len(l)):
            d = getDistance(l,i,j)
            if d > maxi:
                maxi = d
    return maxi

def getColourNumber(l,c):
    '''
    Returns the number of points from the list "l" that have the same color "c" given as a string
    '''
    count = 0
    for elem in l:
        if elem.getColour() == c:
            count +=1
    return count

def updateColour(l,x,y,c):
    '''
    Updates the colour of the point of coordinates(x,y) from the list "l" or prints a msg in case there is no such point
    c = new colour
    '''
    x = int(x)
    y = int(y)
    found = False
    for elem in l:
        if elem.getX() == x and elem.getY() == y:
            elem.setColour(c)
            found = True
            break
    if not found:
        print("There is no such point")

def shiftOnXRight(l):
    for elem in l:
        elem.setX(elem.getX()+1)

def shiftOnXLeft(l):
    for elem in l:
        elem.setX(elem.getX()-1)

def shiftOnYUp(l):
    for elem in l:
        elem.setY(elem.getY()+1)

def shiftOnYDown(l):
    for elem in l:
        elem.setY(elem.getY()-1)

def deleteInCircle(l,x,y,r):
    '''
    Deletes all points that are inside a given circle: of center (x,y) and radius "r" given, from the list "l"
    '''
    for i in range(len(l)-1,-1,-1):
        if isInCircle(x,y,r,l[i].getX(),l[i].getY()):
            deletePoint(l,i)
            
def deleteWithinDistance(l,x,y,d):
    '''
    Deletes all points that are within a certain distance from a given point: of center (x,y) and distance "d" given, from the list "l"
    '''
    for i in range(len(l)-1,-1,-1):
        if math.sqrt((l[i].getX()-x)*(l[i].getX()-x)+(l[i].getY()-y)*(l[i].getY()-y)) == d:
            deletePoint(l,i)