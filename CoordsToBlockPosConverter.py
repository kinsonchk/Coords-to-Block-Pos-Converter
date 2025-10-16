print("\n========================================")
print("-- Coords to Block Position Converter --")
print("========================================")

print("\n-- Coords (in real life) boundary info --\n")

print("Enter the boundary of the coords in this order: <westernmost>(LONG) <southernmost>(LAT) <easternmost>(LONG) <northernmost>(LAT)")
print("e.g. -74.0 45.4 -73.4 45.7")
coords = input("Enter coords boundary: ")

coordBounds = coords.split(' ')

minXstr = coordBounds[0]
minYstr = coordBounds[1]
maxXstr = coordBounds[2]
maxYstr = coordBounds[3]

print("")

minX = float(minXstr)
minY = float(minYstr)
maxX = float(maxXstr)
maxY = float(maxYstr)

print("[ Northwesternmost coords (LAT, LONG): " + maxYstr + ", " + minXstr + " ]")
print("[ Southeasternmost coords (LAT, LONG): " + minYstr + ", " + maxXstr + " ]")

print("\n==========")

print("\n-- Block (in Minecraft) boundary info --\n")

topLeft = input("Enter the top-left block of the boundary of the map (<x> <z>): ")
bottomRight = input("Enter the bottom-right block of the boundary of the map (<x> <z>): ")

topLeftStr = topLeft.split(' ')
leftStr = topLeftStr[0]
topStr = topLeftStr[1]

bottomRightStr = bottomRight.split(' ')
rightStr = bottomRightStr[0]
bottomStr = bottomRightStr[1]

print("")

leftBlock = float(leftStr)
topBlock = float(topStr)
rightBlock = float(rightStr)
bottomBlock = float(bottomStr)

print("[ Map boundary: top-left(" + leftStr + ", " + topStr + ") to bottom-right(" + rightStr + ", " + bottomStr + ") ]")

EWscale = (rightBlock - leftBlock) / (maxX - minX)
NSscale = (bottomBlock - topBlock) / (maxY - minY)

while True:
    print("\n==========")

    print("\n-- Desired block position in coords --\n")

    posYstr = input("Enter desired z-block position in Y-coords (LATITUDE, eg. 45.4): ")
    posXstr = input("Enter desired x-block position in X-coords (LONGITUDE, eg. -74.0): ")
    
    print("")

    posX = float(posXstr)
    posY = float(posYstr)

    print("[ Desired coords position (LAT, LONG): " + posYstr + ", " + posXstr + " ]")

    print("\n==========")

    print("\n-- RESULT --\n")

    blockX = EWscale * (posX - minX) + leftBlock
    blockZ = NSscale * (maxY - posY) + topBlock

    blockXstr = str(blockX)
    blockZstr = str(blockZ)

    print("----------------------------------------")
    print("DESIRED BLOCK POSITION (x, z):\n")
    print("( " + blockXstr + " , " + blockZstr + " )")
    print("\n----------------------------------------")
