#I MADE THIS CHANGE TOO
def displayNotes():
    msg = "Hi and welcome to my second app"
    msg +="A math teacher needs a program that helps students perform simple operations \n with points in two-dimensional space. \n"
    msg +="To facilitate the usage and testing of the app, i divided it into 5 operations: \n"
    msg +="Add and update points, Get points, Delete points, Shift the points and Plot the points \n"
    print(msg)
def displayMenu():
    msg = "Menu: \n"
    msg +="\t 1 - Add and update points \n"
    msg +="\t 2 - Get points \n"
    msg +="\t 3 - Delete points \n"
    msg +="\t 4 - Shift the points \n"
    msg +="\t 5 - Plot the points \n"
    msg +="\t 0 - Exit \n"
    print(msg)
def option1():
    msg = "You have chosen option 1, now choose an operation: \n"
    msg +="\t a) - Add a point to the repository \n"
    msg +="\t b) - Update a point at a given index \n"
    msg +="\t c) - Update the colour of a point given its coordinates \n"
    msg +="\t 0 - Back to menu \n"
    print(msg)
def option2():
    msg = "You have chosen option 2, now choose an operation: \n"
    msg +="\t a) - Get all points \n"
    msg +="\t b) - Get a point at a given index \n"
    msg +="\t c) - Get all points of a given colour \n"
    msg +="\t d) - Get all points that are inside a given square (up-left corner and length given) \n"
    msg +="\t e) - Get the minimum distance between two points \n"
    msg +="\t f) - Get all points that are inside a given rectangle (up-left corner, length and width given) \n"
    msg +="\t g) - Get all points that are inside a given circle (centre of circle, radius given) \n"
    msg +="\t h) - Get the maximum distance between two points \n"
    msg +="\t i) - Get the number of points of a given colour \n"
    msg +="\t 0 - Back to menu \n"
    print(msg)
def option3():
    msg = "You have chosen option 3, now choose an operation: \n"
    msg +="\t a) - Delete a point by index \n"
    msg +="\t b) - Delete all points that are inside a given square (up-left corner and length given) \n"
    msg +="\t c) - Delete a point by coordinates \n"
    msg +="\t d) - Delete all points that are inside a given circle \n"
    msg +="\t e) - Delete all points within a certain distance from a given point \n"
    msg +="\t 0 - Back to menu \n"
    print(msg)
def option4():
    msg = "You have chosen option 4, now choose an operation: \n"
    msg +="\t a) - Shift all points on the x axis to the \n"
    msg +="\t b) - Shift all points on the y axis \n"
    msg +="\t 0 - Back to menu \n"
    print(msg)
def option5():
    msg = "You have chosen option 5, plotting all the points from the repository... \n"
    print(msg)