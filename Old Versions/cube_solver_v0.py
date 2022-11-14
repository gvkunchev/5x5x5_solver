#
#
## Piece parts are defined as follows
## 1 2 3 4
##     5
#
#
## Orientation of a piece part is defined as follows (defined according to the legend above, looking into piece 1, for example)
## Left
## Right
## Top
## Bottom
## Front
## Back
#
#

import copy

solution = []
piece = 1

for x in range(5):
  solution.append([])
  for y in range(5):
    solution[x].append([])
    for z in range(5):
      solution[x][y].append(0)

def printSolution():
  stringToPrint = ""
  for x in range(len(solution)):
    stringToPrint += "\n"
    for y in range(len(solution[x])):
      stringToPrint += " | "
      for z in range(len(solution[x][y])):
        stringToPrint += ","
        pieceNumber = str(solution[x][y][z])
        if len(pieceNumber) == 1:
          pieceNumber = " %s" %pieceNumber
        stringToPrint += pieceNumber
  print stringToPrint

def getSolutionNumber():
  counter = 0
  for x in range(len(solution)):
    for y in range(len(solution[x])):
      for z in range(len(solution[x][y])):
        if solution[x][y][z] != 0:
          counter+=1
  return counter/5

def solve():
  if findPath(0):
    print "Solved!"
    printSolution()
  else:
    print "Not solved"
    printSolution()


def findPath(depth):
  global piece
  global solution
  solutionPreGeneral = copy.deepcopy(solution)
  piecesNumberGeneral = piece
  nextSpot = nextEmptySpot()
  if nextSpot == "Filled":
    print "======"
    print "Filled:"
    printSolution()
    print "======"
    return False
  else:
    x, y, z = nextSpot

  if piece > 25:
    return True

  for eachPiece in [1,2,3,4,5]:
    for eachOrientation in ["Left","Right","Top","Bottom","Front","Back"]:
      for eachAngle in [0,90,180,270]:
        solution = copy.deepcopy(solutionPreGeneral)
        piece = piecesNumberGeneral
        if putPiece(x,y,z,eachPiece,eachOrientation,eachAngle):
          print "I put the piece #", piece
          piece+=1
          if findPath(depth+1):
            return True
        #print "Depth %d Trying again for piece # %d on spot (%d,%d,%d). There are %d pieces in the matrix." %(depth,piece,x,y,z,getSolutionNumber())


  print "Ok, shit happened. Returning one step behind. Number of pieces was set to %d. Number of pieces in the matrix is %d." %(piece,getSolutionNumber())
  return False

def nextEmptySpot():
  global piece
  global solution
  for x in range(len(solution)):
    for y in range(len(solution[x])):
      for z in range(len(solution[x][y])):
        if solution[x][y][z] == 0:
          return [x,y,z]
  return "Filled"


def putPiece(x,y,z,piecePart,orientation,angle):
  global piece
  global solution
  solutionPre = solution[:]
  if orientation == "Left":
    if angle == 0:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x+1,y,z],
          [x+2,y,z],
          [x+3,y,z],
          [x+2,y-1,z]
        ]
      elif piecePart == 2:
        array = [
          [x-1,y,z],
          [x,y,z],
          [x+1,y,z],
          [x+2,y,z],
          [x+1,y-1,z]
        ]
      elif piecePart == 3:
        array = [
          [x-2,y,z],
          [x-1,y,z],
          [x,y,z],
          [x+1,y,z],
          [x,y-1,z]
        ]
      elif piecePart == 4:
        array = [
          [x-3,y,z],
          [x-2,y,z],
          [x-1,y,z],
          [x,y,z],
          [x-1,y-1,z]
        ]
      elif piecePart == 5:
        array = [
          [x-2,y+1,z],
          [x-1,y+1,z],
          [x,y+1,z],
          [x+1,y+1,z],
          [x,y,z]
        ]

    elif angle == 90:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x+1,y,z],
          [x+2,y,z],
          [x+3,y,z],
          [x+2,y,z-1]
        ]
      elif piecePart == 2:
        array = [
          [x-1,y,z],
          [x,y,z],
          [x+1,y,z],
          [x+2,y,z],
          [x+1,y,z-1]
        ]
      elif piecePart == 3:
        array = [
          [x-2,y,z],
          [x-1,y,z],
          [x,y,z],
          [x+1,y,z],
          [x,y,z-1]
        ]
      elif piecePart == 4:
        array = [
          [x-3,y,z],
          [x-2,y,z],
          [x-1,y,z],
          [x,y,z],
          [x-1,y,z-1]
        ]
      elif piecePart == 5:
        array = [
          [x-2,y,z+1],
          [x-1,y,z+1],
          [x,y,z+1],
          [x+1,y,z+1],
          [x,y,z]
        ]


    elif angle == 180:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x+1,y,z],
          [x+2,y,z],
          [x+3,y,z],
          [x+2,y+1,z]
        ]
      elif piecePart == 2:
        array = [
          [x-1,y,z],
          [x,y,z],
          [x+1,y,z],
          [x+2,y,z],
          [x+1,y+1,z]
        ]
      elif piecePart == 3:
        array = [
          [x-2,y,z],
          [x-1,y,z],
          [x,y,z],
          [x+1,y,z],
          [x,y+1,z]
        ]
      elif piecePart == 4:
        array = [
          [x-3,y,z],
          [x-2,y,z],
          [x-1,y,z],
          [x,y,z],
          [x-1,y+1,z]
        ]
      elif piecePart == 5:
        array = [
          [x-2,y-1,z],
          [x-1,y-1,z],
          [x,y-1,z],
          [x+1,y-1,z],
          [x,y,z]
        ]

    elif angle == 270:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x+1,y,z],
          [x+2,y,z],
          [x+3,y,z],
          [x+2,y,z+1]
        ]
      elif piecePart == 2:
        array = [
          [x-1,y,z],
          [x,y,z],
          [x+1,y,z],
          [x+2,y,z],
          [x+1,y,z+1]
        ]
      elif piecePart == 3:
        array = [
          [x-2,y,z],
          [x-1,y,z],
          [x,y,z],
          [x+1,y,z],
          [x,y,z+1]
        ]
      elif piecePart == 4:
        array = [
          [x-3,y,z],
          [x-2,y,z],
          [x-1,y,z],
          [x,y,z],
          [x-1,y,z+1]
        ]
      elif piecePart == 5:
        array = [
          [x-2,y,z-1],
          [x-1,y,z-1],
          [x,y,z-1],
          [x+1,y,z-1],
          [x,y,z]
        ]


  elif orientation == "Right":
    if angle == 0:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x-1,y,z],
          [x-2,y,z],
          [x-3,y,z],
          [x-2,y-1,z]
        ]
      elif piecePart == 2:
        array = [
          [x+1,y,z],
          [x,y,z],
          [x-1,y,z],
          [x-2,y,z],
          [x-1,y-1,z]
        ]
      elif piecePart == 3:
        array = [
          [x+2,y,z],
          [x+1,y,z],
          [x,y,z],
          [x-1,y,z],
          [x,y-1,z]
        ]
      elif piecePart == 4:
        array = [
          [x+3,y,z],
          [x+2,y,z],
          [x+1,y,z],
          [x,y,z],
          [x+1,y-1,z]
        ]
      elif piecePart == 5:
        array = [
          [x+2,y+1,z],
          [x+1,y+1,z],
          [x,y+1,z],
          [x-1,y+1,z],
          [x,y,z]
        ]

    elif angle == 90:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x-1,y,z],
          [x-2,y,z],
          [x-3,y,z],
          [x-2,y,z-1]
        ]
      elif piecePart == 2:
        array = [
          [x+1,y,z],
          [x,y,z],
          [x-1,y,z],
          [x-2,y,z],
          [x-1,y,z-1]
        ]
      elif piecePart == 3:
        array = [
          [x+2,y,z],
          [x+1,y,z],
          [x,y,z],
          [x-1,y,z],
          [x,y,z-1]
        ]
      elif piecePart == 4:
        array = [
          [x+3,y,z],
          [x+2,y,z],
          [x+1,y,z],
          [x,y,z],
          [x+1,y,z-1]
        ]
      elif piecePart == 5:
        array = [
          [x+2,y,z+1],
          [x+1,y,z+1],
          [x,y,z+1],
          [x-1,y,z+1],
          [x,y,z]
        ]


    elif angle == 180:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x-1,y,z],
          [x-2,y,z],
          [x-3,y,z],
          [x-2,y+1,z]
        ]
      elif piecePart == 2:
        array = [
          [x+1,y,z],
          [x,y,z],
          [x-1,y,z],
          [x-2,y,z],
          [x-1,y+1,z]
        ]
      elif piecePart == 3:
        array = [
          [x+2,y,z],
          [x+1,y,z],
          [x,y,z],
          [x-1,y,z],
          [x,y+1,z]
        ]
      elif piecePart == 4:
        array = [
          [x+3,y,z],
          [x+2,y,z],
          [x+1,y,z],
          [x,y,z],
          [x+1,y+1,z]
        ]
      elif piecePart == 5:
        array = [
          [x+2,y-1,z],
          [x+1,y-1,z],
          [x,y-1,z],
          [x-1,y-1,z],
          [x,y,z]
        ]

    elif angle == 270:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x-1,y,z],
          [x-2,y,z],
          [x-3,y,z],
          [x-2,y,z+1]
        ]
      elif piecePart == 2:
        array = [
          [x+1,y,z],
          [x,y,z],
          [x-1,y,z],
          [x-2,y,z],
          [x-1,y,z+1]
        ]
      elif piecePart == 3:
        array = [
          [x+2,y,z],
          [x+1,y,z],
          [x,y,z],
          [x-1,y,z],
          [x,y,z+1]
        ]
      elif piecePart == 4:
        array = [
          [x+3,y,z],
          [x+2,y,z],
          [x+1,y,z],
          [x,y,z],
          [x+1,y,z+1]
        ]
      elif piecePart == 5:
        array = [
          [x+2,y,z-1],
          [x+1,y,z-1],
          [x,y,z-1],
          [x-1,y,z-1],
          [x,y,z]
        ]



  elif orientation == "Front":
    if angle == 0:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x,y,z-1],
          [x,y,z-2],
          [x,y,z-3],
          [x-1,y,z-1]
        ]
      elif piecePart == 2:
        array = [
          [x,y,z+1],
          [x,y,z],
          [x,y,z-1],
          [x,y,z-2],
          [x-1,y,z]
        ]
      elif piecePart == 3:
        array = [
          [x,y,z+2],
          [x,y,z+1],
          [x,y,z],
          [x,y,z-1],
          [x-1,y,z+1]
        ]
      elif piecePart == 4:
        array = [
          [x,y,z+3],
          [x,y,z+2],
          [x,y,z+1],
          [x,y,z],
          [x-1,y,z+2]
        ]
      elif piecePart == 5:
        array = [
          [x+1,y,z+1],
          [x+1,y,z],
          [x+1,y,z-1],
          [x+1,y,z-2],
          [x,y,z]
        ]

    elif angle == 90:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x,y-1,z],
          [x,y-2,z],
          [x,y-3,z],
          [x-1,y-2,z]
        ]
      elif piecePart == 2:
        array = [
          [x,y+1,z],
          [x,y,z],
          [x,y-1,z],
          [x,y-2,z],
          [x-1,y-1,z]
        ]
      elif piecePart == 3:
        array = [
          [x,y+2,z],
          [x,y+1,z],
          [x,y,z],
          [x,y-1,z],
          [x-1,y,z]
        ]
      elif piecePart == 4:
        array = [
          [x,y+3,z],
          [x,y+2,z],
          [x,y+1,z],
          [x,y,z],
          [x-1,y+1,z]
        ]
      elif piecePart == 5:
        array = [
          [x+1,y+2,z],
          [x+1,y+1,z],
          [x+1,y,z],
          [x+1,y-1,z],
          [x,y,z]
        ]


    elif angle == 180:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x,y,z-1],
          [x,y,z-2],
          [x,y,z-3],
          [x-1,y,z-2]
        ]
      elif piecePart == 2:
        array = [
          [x,y,z+1],
          [x,y,z],
          [x,y,z-1],
          [x,y,z-2],
          [x-1,y,z-1]
        ]
      elif piecePart == 3:
        array = [
          [x,y,z+2],
          [x,y,z+1],
          [x,y,z],
          [x,y,z-1],
          [x-1,y,z]
        ]
      elif piecePart == 4:
        array = [
          [x,y,z+3],
          [x,y,z+2],
          [x,y,z+1],
          [x,y,z],
          [x-1,y,z+1]
        ]
      elif piecePart == 5:
        array = [
          [x+1,y,z+2],
          [x+1,y,z+1],
          [x+1,y,z],
          [x+1,y,z-1],
          [x,y,z]
        ]

    elif angle == 270:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x,y+1,z],
          [x,y+2,z],
          [x,y+3,z],
          [x-1,y+2,z]
        ]
      elif piecePart == 2:
        array = [
          [x,y-1,z],
          [x,y,z],
          [x,y+1,z],
          [x,y+2,z],
          [x-1,y+1,z]
        ]
      elif piecePart == 3:
        array = [
          [x,y-2,z],
          [x,y-1,z],
          [x,y,z],
          [x,y+1,z],
          [x-1,y,z]
        ]
      elif piecePart == 4:
        array = [
          [x,y-3,z],
          [x,y-2,z],
          [x,y-1,z],
          [x,y,z],
          [x-1,y-1,z]
        ]
      elif piecePart == 5:
        array = [
          [x+1,y-2,z],
          [x+1,y-1,z],
          [x+1,y,z],
          [x+1,y+1,z],
          [x,y,z]
        ]



  elif orientation == "Back":
    if angle == 0:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x,y,z+1],
          [x,y,z+2],
          [x,y,z+3],
          [x+1,y,z+2]
        ]
      elif piecePart == 2:
        array = [
          [x,y,z-1],
          [x,y,z],
          [x,y,z+1],
          [x,y,z+2],
          [x+1,y,z+1]
        ]
      elif piecePart == 3:
        array = [
          [x,y,z-2],
          [x,y,z-1],
          [x,y,z],
          [x,y,z+1],
          [x+1,y,z]
        ]
      elif piecePart == 4:
        array = [
          [x,y,z-3],
          [x,y,z-2],
          [x,y,z-1],
          [x,y,z],
          [x+1,y,z-1]
        ]
      elif piecePart == 5:
        array = [
          [x-1,y,z-2],
          [x-1,y,z-1],
          [x-1,y,z],
          [x-1,y,z+1],
          [x,y,z]
        ]

    elif angle == 90:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x,y-1,z],
          [x,y-2,z],
          [x,y-3,z],
          [x+1,y-2,z]
        ]
      elif piecePart == 2:
        array = [
          [x,y+1,z],
          [x,y,z],
          [x,y-1,z],
          [x,y-2,z],
          [x+1,y-1,z]
        ]
      elif piecePart == 3:
        array = [
          [x,y+2,z],
          [x,y+1,z],
          [x,y,z],
          [x,y-1,z],
          [x+1,y,z]
        ]
      elif piecePart == 4:
        array = [
          [x,y+3,z],
          [x,y+2,z],
          [x,y+1,z],
          [x,y,z],
          [x+1,y+1,z]
        ]
      elif piecePart == 5:
        array = [
          [x-1,y+2,z],
          [x-1,y+1,z],
          [x-1,y,z],
          [x-1,y-1,z],
          [x,y,z]
        ]


    elif angle == 180:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x,y,z-1],
          [x,y,z-2],
          [x,y,z-3],
          [x+1,y,z-2]
        ]
      elif piecePart == 2:
        array = [
          [x,y,z+1],
          [x,y,z],
          [x,y,z-1],
          [x,y,z-2],
          [x+1,y,z-1]
        ]
      elif piecePart == 3:
        array = [
          [x,y,z+2],
          [x,y,z+1],
          [x,y,z],
          [x,y,z-1],
          [x+1,y,z]
        ]
      elif piecePart == 4:
        array = [
          [x,y,z+3],
          [x,y,z+2],
          [x,y,z+1],
          [x,y,z],
          [x+1,y,z+1]
        ]
      elif piecePart == 5:
        array = [
          [x-1,y,z+2],
          [x-1,y,z+1],
          [x-1,y,z],
          [x-1,y,z-1],
          [x,y,z]
        ]

    elif angle == 270:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x,y+1,z],
          [x,y+2,z],
          [x,y+3,z],
          [x+1,y+2,z]
        ]
      elif piecePart == 2:
        array = [
          [x,y-1,z],
          [x,y,z],
          [x,y+1,z],
          [x,y+2,z],
          [x+1,y+1,z]
        ]
      elif piecePart == 3:
        array = [
          [x,y-2,z],
          [x,y-1,z],
          [x,y,z],
          [x,y+1,z],
          [x+1,y,z]
        ]
      elif piecePart == 4:
        array = [
          [x,y-3,z],
          [x,y-2,z],
          [x,y-1,z],
          [x,y,z],
          [x+1,y-1,z]
        ]
      elif piecePart == 5:
        array = [
          [x-1,y-2,z],
          [x-1,y-1,z],
          [x-1,y,z],
          [x-1,y+1,z],
          [x,y,z]
        ]



  elif orientation == "Top":
    if angle == 0:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x,y,z+1],
          [x,y,z+2],
          [x,y,z+3],
          [x,y-1,z+2]
        ]
      elif piecePart == 2:
        array = [
          [x,y,z-1],
          [x,y,z],
          [x,y,z+1],
          [x,y,z+2],
          [x,y-1,z+1]
        ]
      elif piecePart == 3:
        array = [
          [x,y,z-2],
          [x,y,z-1],
          [x,y,z],
          [x,y,z+1],
          [x,y-1,z]
        ]
      elif piecePart == 4:
        array = [
          [x,y,z-3],
          [x,y,z-2],
          [x,y,z-1],
          [x,y,z],
          [x,y-1,z-1]
        ]
      elif piecePart == 5:
        array = [
          [x,y+1,z-2],
          [x,y+1,z-1],
          [x,y+1,z],
          [x,y+1,z+1],
          [x,y,z]
        ]

    elif angle == 90:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x,y-1,z],
          [x,y-2,z],
          [x,y-3,z],
          [x,y-2,z-1]
        ]
      elif piecePart == 2:
        array = [
          [x,y+1,z],
          [x,y,z],
          [x,y-1,z],
          [x,y-2,z],
          [x,y-1,z-1]
        ]
      elif piecePart == 3:
        array = [
          [x,y+2,z],
          [x,y+1,z],
          [x,y,z],
          [x,y-1,z],
          [x,y,z-1]
        ]
      elif piecePart == 4:
        array = [
          [x,y+3,z],
          [x,y+2,z],
          [x,y+1,z],
          [x,y,z],
          [x,y+1,z-1]
        ]
      elif piecePart == 5:
        array = [
          [x,y+2,z+1],
          [x,y+1,z+1],
          [x,y,z+1],
          [x,y-1,z+1],
          [x,y,z]
        ]


    elif angle == 180:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x,y,z-1],
          [x,y,z-2],
          [x,y,z-3],
          [x,y+1,z-2]
        ]
      elif piecePart == 2:
        array = [
          [x,y,z+1],
          [x,y,z],
          [x,y,z-1],
          [x,y,z-2],
          [x,y+1,z-1]
        ]
      elif piecePart == 3:
        array = [
          [x,y,z+2],
          [x,y,z+1],
          [x,y,z],
          [x,y,z-1],
          [x,y+1,z]
        ]
      elif piecePart == 4:
        array = [
          [x,y,z+3],
          [x,y,z+2],
          [x,y,z+1],
          [x,y,z],
          [x,y+1,z+1]
        ]
      elif piecePart == 5:
        array = [
          [x,y-1,z+2],
          [x,y-1,z+1],
          [x,y-1,z],
          [x,y-1,z-1],
          [x,y,z]
        ]

    elif angle == 270:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x,y+1,z],
          [x,y+2,z],
          [x,y+3,z],
          [x,y+2,z+1]
        ]
      elif piecePart == 2:
        array = [
          [x,y-1,z],
          [x,y,z],
          [x,y+1,z],
          [x,y+2,z],
          [x,y+1,z+1]
        ]
      elif piecePart == 3:
        array = [
          [x,y-2,z],
          [x,y-1,z],
          [x,y,z],
          [x,y+1,z],
          [x,y,z+1]
        ]
      elif piecePart == 4:
        array = [
          [x,y-3,z],
          [x,y-2,z],
          [x,y-1,z],
          [x,y,z],
          [x,y-1,z+1]
        ]
      elif piecePart == 5:
        array = [
          [x,y-2,z-1],
          [x,y-1,z-1],
          [x,y,z-1],
          [x,y+1,z-1],
          [x,y,z]
        ]



  elif orientation == "Bottom":
    if angle == 0:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x,y,z-1],
          [x,y,z-2],
          [x,y,z-3],
          [x,y-1,z-2]
        ]
      elif piecePart == 2:
        array = [
          [x,y,z+1],
          [x,y,z],
          [x,y,z-1],
          [x,y,z-2],
          [x,y-1,z-1]
        ]
      elif piecePart == 3:
        array = [
          [x,y,z+2],
          [x,y,z+1],
          [x,y,z],
          [x,y,z-1],
          [x,y-1,z]
        ]
      elif piecePart == 4:
        array = [
          [x,y,z+3],
          [x,y,z+2],
          [x,y,z+1],
          [x,y,z],
          [x,y-1,z+1]
        ]
      elif piecePart == 5:
        array = [
          [x,y+1,z+2],
          [x,y+1,z+1],
          [x,y+1,z],
          [x,y+1,z-1],
          [x,y,z]
        ]

    elif angle == 90:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x,y+1,z],
          [x,y+2,z],
          [x,y+3,z],
          [x,y+2,z-1]
        ]
      elif piecePart == 2:
        array = [
          [x,y-1,z],
          [x,y,z],
          [x,y+1,z],
          [x,y+2,z],
          [x,y+1,z-1]
        ]
      elif piecePart == 3:
        array = [
          [x,y-2,z],
          [x,y-1,z],
          [x,y,z],
          [x,y+1,z],
          [x,y,z-1]
        ]
      elif piecePart == 4:
        array = [
          [x,y-3,z],
          [x,y-2,z],
          [x,y-1,z],
          [x,y,z],
          [x,y-1,z-1]
        ]
      elif piecePart == 5:
        array = [  
          [x,y-2,z+1],
          [x,y-1,z+1],
          [x,y,z+1],
          [x,y+1,z+1],
          [x,y,z]
        ]


    elif angle == 180:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x,y,z+1],
          [x,y,z+2],
          [x,y,z+3],
          [x,y+1,z+2]
        ]
      elif piecePart == 2:
        array = [
          [x,y,z-1],
          [x,y,z],
          [x,y,z+1],
          [x,y,z+2],
          [x,y+1,z+1]
        ]
      elif piecePart == 3:
        array = [
          [x,y,z-2],
          [x,y,z-1],
          [x,y,z],
          [x,y,z+1],
          [x,y+1,z]
        ]
      elif piecePart == 4:
        array = [
          [x,y,z-3],
          [x,y,z-2],
          [x,y,z-1],
          [x,y,z],
          [x,y+1,z-1]
        ]
      elif piecePart == 5:
        array = [
          [x,y-1,z-2],
          [x,y-1,z-1],
          [x,y-1,z],
          [x,y-1,z+1],
          [x,y,z]
        ]

    elif angle == 270:
      if piecePart == 1:
        array = [
          [x,y,z],
          [x,y-1,z],
          [x,y-2,z],
          [x,y-3,z],
          [x,y-2,z+1]
        ]
      elif piecePart == 2:
        array = [
          [x,y+1,z],
          [x,y,z],
          [x,y-1,z],
          [x,y-2,z],
          [x,y-1,z+1]
        ]
      elif piecePart == 3:
        array = [
          [x,y+2,z],
          [x,y+1,z],
          [x,y,z],
          [x,y-1,z],
          [x,y,z+1]
        ]
      elif piecePart == 4:
        array = [
          [x,y+3,z],
          [x,y+2,z],
          [x,y+1,z],
          [x,y,z],
          [x,y+1,z+1]
        ]
      elif piecePart == 5:
        array = [
          [x,y+2,z-1],
          [x,y+1,z-1],
          [x,y,z-1],
          [x,y-1,z-1],
          [x,y,z]
        ]
        
        
        
  if existAndEmpty(array):
    fillSpots(array)
    return True
  solution = solutionPre[:]
  return False

def existAndEmpty(array):
  global piece
  global solution
  for eachPoint in array:
    x,y,z = eachPoint
    if not (x>=0 and y>=0 and z>=0 and x<5 and y<5 and z<5):
      return False
    if solution[x][y][z] != 0:
      return False
  return True

def fillSpots(array):
  global piece
  global solution
  for eachPoint in array:
    x,y,z = eachPoint
    solution[x][y][z] = piece


solve()