#AND THIS CHANGE
import functions
from Class import myPoint
def test_addPoint():
    l = []
    functions.addPoint(l,1,2,"red")
    assert l[0].getColour() == "red"
    assert l[0].getX() == 1
    assert l[0].getY() == 2
    
def test_getAllPoints():
    print("\t test_getAllPoints...")
    l = []
    l.append(myPoint(1,2,"red"))
    functions.addPoint(l,0,0,"")
    functions.getAllPoints(l)

def test_getPointGivenIndex():
    print("\t test_getPointGivenIndex...")
    l = []
    l.append(myPoint(1,2,"red"))
    functions.addPoint(l,0,0,"")
    functions.getPointGivenIndex(l,0)

def test_isInSquare():
    assert functions.isInSquare(1,4,2,3,2) == True
    assert functions.isInSquare(10,10,2,3,200) == False

def test_getPointsSquare():
    print("\t test_getPointsSquare...")
    l = []
    l.append(myPoint(2,3,"red"))
    functions.addPoint(l,-4,-1,"blue")
    functions.getPointsSquare(l,1,4,1)

def test_getMinDistance():
    l = [myPoint(1,1,"red"),myPoint(1,5,"green"),myPoint(1,2,"green")]
    assert functions.getMinDistance(l) == 1
    l = [myPoint(1,1,"red"),myPoint(1,5,"green")]
    assert functions.getMinDistance(l) == 4

def test_getDistance():
    l = [myPoint(1,1,"red"),myPoint(1,5,"green")]
    assert functions.getDistance(l,0,1) == 4

def test_updatePoint():
    l = [myPoint(1,1,"red"),myPoint(1,5,"green")]
    assert l[0].getX() == 1
    functions.updatePoint(l,0,2,3,"blue")
    assert l[0].getX() == 2
    assert l[0].getY() == 3
    assert l[0].getColour() == "blue"

def test_deletePoint():
    l = [myPoint(1,1,"red"),myPoint(2,5,"green")]
    functions.deletePoint(l,0)
    assert l[0].getX() == 2
    assert l[0].getY() == 5
    assert l[0].getColour() == "green"

def test_deleteFromSquare():
    l = [myPoint(1,1,"red"),myPoint(2,2,"green"),myPoint(3,3,"blue"),myPoint(5,1,"yellow")]
    #functions.getAllPoints(l)
    assert l[1].getX() == 2
    assert l[1].getY() == 2
    assert l[1].getColour() == "green"
    functions.deleteFromSquare(l,2,3,1)

    #functions.getAllPoints(l)
    assert l[1].getX() == 5
    assert l[1].getY() == 1
    assert l[1].getColour() == "yellow"

def test_plotPoints():
    l = [myPoint(1,1,"red"),myPoint(2,2,"green"),myPoint(3,3,"blue")]
    functions.plotPoints(l)

#ITERATION 2 TESTING FUNCTIONS START FROM HERE


def test_getPointsRectangle():
    print("\t test_getPointsRectangle")
    l = [myPoint(1,1,"red"),myPoint(2,2,"green"),myPoint(3,3,"blue"),myPoint(5,1,"yellow")]
    functions.getPointsRectangle(l,2,3,10,1)

def test_isInCircle():
    assert functions.isInCircle(0,0,4,0,4) == True
    assert functions.isInCircle(0,0,100,4,4) == True
    assert functions.isInCircle(0,0,4,4,4) == False

def test_getPointsCircle():
    l = [myPoint(1,1,"red"),myPoint(2,2,"green"),myPoint(3,3,"blue"),myPoint(5,1,"yellow")]
    functions.getPointsCircle(l,0,0,4)

def test_getMaxDistance():
    l = [myPoint(1,1,"red"),myPoint(1,5,"green"),myPoint(1,2,"green")]
    assert functions.getMaxDistance(l) == 4
    l = [myPoint(1,1,"red"),myPoint(1,2,"green")]
    assert functions.getMaxDistance(l) == 1

def test_getColourNumber():
    l = [myPoint(1,1,"red"),myPoint(1,5,"green"),myPoint(1,2,"green")]
    assert functions.getColourNumber(l,"red") == 1
    assert functions.getColourNumber(l,"green") == 2
    assert functions.getColourNumber(l,"blue") == 0

def test_updateColour():
    l = [myPoint(1,1,"red"),myPoint(1,5,"green"),myPoint(1,2,"green")]
    functions.updateColour(l,1,5,"magenta")
    assert l[1].getColour() == "magenta"

def test_deleteInCircle():
    l = [myPoint(1,1,"red"),myPoint(2,2,"green"),myPoint(3,3,"blue"),myPoint(5,1,"yellow")]
    functions.deleteInCircle(l,0,1,1.5)
    assert l[0].getColour() == "green"

def test_deleteWithinDistance():
    l = [myPoint(1,1,"red"),myPoint(2,2,"green"),myPoint(3,3,"blue"),myPoint(5,1,"yellow")]
    functions.deleteWithinDistance(l,0,0,2)
    assert l[0].getColour() == "red"
    functions.deleteWithinDistance(l,1,0,1)
    assert l[0].getColour() == "green"

def test_shiftOnXRight():
    l = [myPoint(1,1,"red"),myPoint(2,2,"green"),myPoint(3,3,"blue"),myPoint(5,1,"yellow")]
    functions.shiftOnXRight(l)
    assert l[0].getX() == 2
    assert l[3].getX() == 6

def test_shiftOnXLeft():
    l = [myPoint(1,1,"red"),myPoint(2,2,"green"),myPoint(3,3,"blue"),myPoint(5,1,"yellow")]
    functions.shiftOnXLeft(l)
    assert l[0].getX() == 0
    assert l[3].getX() == 4

def test_shiftOnYUp():
    l = [myPoint(1,1,"red"),myPoint(2,2,"green"),myPoint(3,3,"blue"),myPoint(5,1,"yellow")]
    functions.shiftOnYUp(l)
    assert l[0].getY() == 2
    assert l[3].getY() == 2

def test_shiftOnYDown():
    l = [myPoint(1,1,"red"),myPoint(2,2,"green"),myPoint(3,3,"blue"),myPoint(5,1,"yellow")]
    functions.shiftOnYDown(l)
    assert l[0].getY() == 0
    assert l[3].getY() == 0
#TESTING STARTS FROM HERE


'''
test_addPoint()
test_getAllPoints()
test_getPointGivenIndex()
test_getPointsSquare()
test_isInSquare()
test_getMinDistance()
test_getDistance()
test_updatePoint()
test_deletePoint()
test_deleteFromSquare()
#test_plotPoints()
'''

#ITERATION 2 TESTS START FROM HERE

'''
test_getPointsRectangle()
test_isInCircle()
test_getPointsCircle()
test_getMaxDistance()
test_getColourNumber()
test_updateColour()
test_deleteInCircle()
test_deleteWithinDistance()
test_shiftOnXRight()
test_shiftOnXLeft()
test_shiftOnYUp()
test_shiftOnYDown()
'''