from math import sqrt
speedpersecond = (3)
A = (3)
B = (1)
a = (2)
b = (2)
xDistance = (a-A)
yDistance = (b-B)
diagonalDistanceSquared = (yDistance*yDistance+xDistance*xDistance) 
diagonalDistance = sqrt(diagonalDistanceSquared)
timeToGetThere = (diagonalDistance/speedpersecond)
print (f" Going at a velocity of {speedpersecond} meters per second, it will take you {timeToGetThere} seconds to get from A to B, traversing a distance of {diagonalDistance} meters")
