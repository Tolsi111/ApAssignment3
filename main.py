#I CHANGED THIS
from Class import myPoint
import functions
import ui

def start():
    l = [myPoint(1,1,"red"),myPoint(2,2,"green"),myPoint(3,3,"blue"),
    myPoint(5,1,"yellow"),myPoint(3,-1,"green"),myPoint(1,-2,"red"),
    myPoint(2,-4,"magenta"),myPoint(-2,-1,"red"),myPoint(-4,-2,"yellow"),
    myPoint(-2,1,"magenta")]#initial list of points given as an example and for testing purposes

    ui.displayNotes()
    print("Start...")

    while True:
        ui.displayMenu()
        option = input("Your option: ")
        if option == "1":#Add and update points
            while True:
                ui.option1()
                op = input("Your operation: ")
                if op == "a":#Add a point to the repository
                    x = functions.validNumber(input("x coordinate: "))
                    y = functions.validNumber(input("y coordinate: "))
                    c = input("colour: ")
                    functions.addPoint(l,x,y,c)
                    break
                elif op == "b":#Update a point at a given index
                    i = input("index: ")
                    i = functions.validIndex(l,i)
                    x = input("new x coordinate: ")
                    y = input("new y coordinate: ")
                    c = input("new colour: ")
                    try:
                        functions.updatePoint(l,int(i),x,y,c)
                    except ValueError as e:
                        print(str(e))
                    break
                elif op == "c":#Update the colour of a point given its coordinates
                    x = input("x coordinate: ")
                    y = input("y coordinate: ")
                    c = input("new colour: ")
                    try:
                        myPoint(x,y,c)
                        functions.updateColour(l,x,y,c)
                    except ValueError as e:
                        print(str(e))
                    break
                elif op == "0":#Back to menu
                    print("back")
                    break
                else:
                    print("Please insert a valid operation :( \n")
        elif option == "2":#Get points
            while True:
                ui.option2()
                op = input("Your operation: ")
                if op == "a":#Get all points
                    functions.getAllPoints(l)
                    break
                elif op == "b":#Get a point at a given index
                    i = input("index: ")
                    i = functions.validIndex(l,i)
                    functions.getPointGivenIndex(l,i)
                    break
                elif op == "c":#Get all points of a given colour
                    c = input("colour: ")
                    try:
                        myPoint(0,0,c)#to check if the colour is a valid one'''
                        functions.getAllColour(l,c)
                    except ValueError as e:
                        print(str(e))
                    break
                elif op == "d":#Get all points that are inside a given square (up-left corner and length given)
                    x = input("x coordinate: ")
                    y = input("y coordinate: ")
                    length = functions.validNumber(input("length: "))
                    try:
                        myPoint(x,y,"red")#to check if the coordinates are valid
                        functions.getPointsSquare(l,x,y,length)
                    except ValueError as e:
                        print(str(e))
                    break
                elif op == "e":#Get the minimum distance between two points
                    print("Minimum distance is " + str(functions.getMinDistance(l)))
                    break
                elif op == "f":#Get all points that are inside a given rectangle (up-left corner, length and width given)
                    x = input("x coordinate: ")
                    y = input("y coordinate: ")
                    length = functions.validNumber(input("length: "))
                    width = functions.validNumber(input("width: "))
                    try:
                        myPoint(x,y,"red")#to check if the coordinates are valid
                        functions.getPointsRectangle(l,x,y,length,width)
                    except ValueError as e:
                        print(str(e))
                    break
                elif op == "g":#Get all points that are inside a given circle (centre of circle, radius given)
                    x = functions.validNumber(input("x: "))
                    y = functions.validNumber(input("y: "))
                    r = functions.validNumber(input("r: "))
                    functions.getPointsCircle(l,x,y,r)
                    break
                elif op == "h":#Get the maximum distance between two points
                    print("Maximum distance is " + str(functions.getMaxDistance(l)))
                    break
                elif op == "i":#Get the number of points of a given colour
                    c = input("colour: ")
                    try:
                        myPoint(0,0,c)
                        print("The number of points of this colour is " + str(functions.getColourNumber(l,c)))
                    except ValueError as e:
                        print(str(e))
                    break
                elif op == "0":#Back to menu
                    print("back")
                    break
                else:
                    print("Please insert a valid operation :( \n")
        elif option == "3":#Delete points
            while True:
                ui.option3()
                op = input("Your operation: ")
                if op == "a":#Delete a point by index
                    i = functions.validIndex(l,input("index: "))
                    functions.deletePoint(l,i)
                    break
                elif op == "b":#Delete all points that are inside a given square (up-left corner and length given)
                    x = input("x coordinate: ")
                    y = input("y coordinate: ")
                    length = functions.validNumber(input("length: "))
                    try:
                        myPoint(x,y,"red")#to check if the coordinates are valid
                        functions.deleteFromSquare(l,int(x),int(y),length)
                    except ValueError as e:
                        print(str(e))
                    break
                elif op == "c":#Delete a point by coordinates
                    x = input("x coordinate: ")
                    y = input("y coordinate: ")
                    try:
                        myPoint(x,y,"red")#to check if the coordinates are valid
                        functions.deleteByCoord(l,int(x),int(y))
                    except ValueError as e:
                        print(str(e))
                    break
                elif op == "d":#Delete all points that are inside a given circle
                    x = input("x coordinate: ")
                    y = input("y coordinate: ")
                    r = functions.validNumber(input("r:"))
                    try:
                        myPoint(x,y,"red")#to check if the coordinates are valid
                        functions.deleteInCircle(l,int(x),int(y),int(r))
                    except ValueError as e:
                        print(str(e))
                    break
                elif op == "e":#Delete all points within a certain distance from a given point
                    x = input("x coordinate: ")
                    y = input("y coordinate: ")
                    d = functions.validNumber(input("distance:"))
                    try:
                        myPoint(x,y,"red")#to check if the coordinates are valid
                        functions.deleteWithinDistance(l,int(x),int(y),int(d))
                    except ValueError as e:
                        print(str(e))
                    break
                elif op == "0":#Back to menu
                    print("back")
                    break
                else:
                    print("Please insert a valid operation :( \n")
        elif option == "4":#Shift the points
            while True:
                ui.option4()
                op = input("Your operation: ")
                if op == "a":#Shift all points on the x axis to the right
                    functions.shiftOnXRight(l)
                    break
                elif op == "b":#Shift all points on the y axis upwards
                    functions.shiftOnYUp(l)
                    break
                elif op == "0":#back to menu
                    print("back")
                    break
                else:
                    print("Please insert a valid operation :( \n")
        elif option == "5":#Plot the points
            ui.option5()
            functions.plotPoints(l)
        elif option == "0":
            print("Exit...")
            break
        else:
            print("Invalid option, please insert a valid option :( \n")


    print("End...")