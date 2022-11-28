def checkIfNextToSolution(matriz, ycoordinate, xcoordinate):
    """
    Check if the current position is next to the solution
    :param matriz: any 2D matrix of any size
    :param xcoordinate: the x coordinate of the current position
    :param ycoordinate: the y coordinate of the current position
    :return: True if the current position is next to the solution, False otherwise
    """
    if matriz[xcoordinate][ycoordinate - 1] == 'S' or \
            matriz[xcoordinate - 1][ycoordinate] == 'S' or \
            matriz[xcoordinate][ycoordinate + 1] == 'S' or \
            matriz[xcoordinate + 1][ycoordinate] == 'S':
        return True
    else:
        return False

lab = [['x','x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x','x', 'x', 'x', ' ', ' ',' ', 'x'], ['x','x', 'x', 'x', ' ', 'x',' ', 'x'], ['x','x', 'x', 'x', ' ', 'x',' ', 'x'], ['x','x', 'x', 'x', ' ', 'x',' ', 'x'], ['x','E', ' ', ' ', ' ', 'x','S', 'x'], ['x','x', 'x', 'x', 'x', 'x','x', 'x']]
print (lab[0][0], lab[0][1], lab[0][2], lab[0][3], lab[0][4], lab[0][5], lab[0][6], lab[0][7])
print (lab[1][0], lab[1][1], lab[1][2], lab[1][3], lab[1][4], lab[1][5], lab[1][6], lab[1][7])
print (lab[2][0], lab[2][1], lab[2][2], lab[2][3], lab[2][4], lab[2][5], lab[2][6], lab[2][7])
print (lab[3][0], lab[3][1], lab[3][2], lab[3][3], lab[3][4], lab[3][5], lab[3][6], lab[3][7])
print (lab[4][0], lab[4][1], lab[4][2], lab[4][3], lab[4][4], lab[4][5], lab[4][6], lab[4][7])
print (lab[5][0], lab[5][1], lab[5][2], lab[5][3], lab[5][4], lab[5][5], lab[5][6], lab[5][7])
print (lab[6][0], lab[6][1], lab[6][2], lab[6][3], lab[6][4], lab[6][5], lab[6][6], lab[6][7])
            

PathLeft = False
PathRight = False
PathUp = False
PathDown = False

numberOfpaths = 0

row= 0
while row < len(lab):
    column = 0
    while column < len(lab[0]):
        if lab[row][column] == 'E':
            entrancerow = row
            entrancecolumn = column
        column += 1
    row += 1

currentlocationx = entrancecolumn 
currentlocationy = entrancerow

while checkIfNextToSolution (lab, currentlocationx, currentlocationy) is False:
    if lab[currentlocationy][currentlocationx -1] == " ":
        PathLeft = True
        numberOfpaths += 1
    lab[currentlocationy][currentlocation -1] = "." (?)
    if lab[currentlocationy][currentlocationx +1] == " ":
        PathRight = True
        numberOfpaths += 1
    if lab[currentlocationy-1][currentlocationx] == " ":
        PathUp = True
        numberOfpaths += 1
    if lab[currentlocationy+1][currentlocationx] == " ":
        PathDown = True
        numberOfpaths += 1
    if PathLeft is True:
        lab[currentlocationy][currentlocationx-1] = "x"
        currentlocationx -=1
    if PathRight is True:
        lab[currentlocationy][currentlocationx+1] = "x"
        currentlocationx +=1
    if PathUp is True:
        lab[currentlocationy-1][currentlocationx] = "x"
        currentlocationy -=1
    if PathDown is True:
        lab[currentlocationy+1][currentlocationx] = "x"
        currentlocationy +=1
    
    
 
if checkIfNextToSolution (lab, currentlocationx, currentlocationy) is True:
    print ("you made it to the end")
    print ("It took", numberOfpaths, "steps to reach the end.")
    