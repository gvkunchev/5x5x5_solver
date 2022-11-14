#######################################################################
#                            Cube Solver v1                           #
# Uses a backtrack approach for constructing a 5x5x5 cube consisting  #
# of 25 identical pieces, each of which looks like the following ex.  #
#                   ____   ____   ____   ____                         #
#                  |    | |    | |    | |    |                        #
#                  |  1 | |  2 | |  3 | |  4 |                        #
#                  |____| |____| |____| |____|                        #
#                                 ____                                #
#                                |    |                               #
#                                |  5 |                               #
#                                |____|                               #
#                                                                     #
# The example above shows the labeling that the script uses for       #
# defining a specific part of a single piece.                         #
#                                                                     #
# Orientation of a piece is defined as Left, Right, Top,              #
# Bottom, Front, Back. Each of these are showing the side of a        #
# single part of the piece that is used for reference and define      #
# the orientation of the piece we are trying to implement.            #
#                                                                     #
# Angle of a piece is defined as 0, 90, 180, 270 degrees.             #
# Rotation is applied looking into the specific side of the piece     #
# we are applying. In other words, its orientation.                   #
#                                                                     #
#                                                                     #
# These properties (part of the piece, side of the part               #
# and angle at which it is rotated) define the way we try to put      #
# a piece in the 5x5x5 matrix. We try all combinations and if         #
# a path is halting to an end, we backtrack to a previous version     #
# of the matrix, switching to the next possible placing of a piece.   #
#                                                                     #
#                                                                     #
# The pieces are placed one by one, starting at one of the cube       #
# angles. Once a piece is placed, we try putting a piece in the next  #
# empty spot of the matrix (consider that putting a piece does not    #
# mean occupying a single place in the matrix, it fills 5 different   #
# spots so we just look for the next empty one.                       #
#                                                                     #
#######################################################################

# These two will hold the current version of the matrix
# and the current piece we are trying to place
solution = []
piece = 1

# Number of sides in the matrix
N = 5

# Types of parts of a single piece(look in the example at the beginning of the document
allParts = range(1,6)
# Types of orientation of a single part of piece
allOrientations = ["Left", "Right", "Top", "Bottom", "Front", "Back"]
# Types of angles that can be applied to a specific part and orientation
allAngles = [0, 90, 180, 270]
# Dictionary defining the coordinates of all parts of a piece
# Based on the part, orientation and angle of the part we want to insert
pieceCoordinates = {
  "Left": {
    0: {
      1: [
           "x  ,y  ,z",
           "x+1,y  ,z",
           "x+2,y  ,z",
           "x+3,y  ,z",
           "x+2,y-1,z"
         ],
      2: [
           "x-1,y  ,z",
           "x  ,y  ,z",
           "x+1,y  ,z",
           "x+2,y  ,z",
           "x+1,y-1,z"
         ],
      3: [
           "x-2,y  ,z",
           "x-1,y  ,z",
           "x  ,y  ,z",
           "x+1,y  ,z",
           "x  ,y-1,z"
         ],
      4: [
           "x-3,y  ,z",
           "x-2,y  ,z",
           "x-1,y  ,z",
           "x  ,y  ,z",
           "x-1,y-1,z"
         ],
      5: [
           "x-2,y+1,z",
           "x-1,y+1,z",
           "x  ,y+1,z",
           "x+1,y+1,z",
           "x  ,y  ,z"
         ]
    },
    90: {
      1: [
           "x  ,y  ,z",
           "x+1,y  ,z",
           "x+2,y  ,z",
           "x+3,y  ,z",
           "x+2,y  ,z-1"
         ],
      2: [
           "x-1,y  ,z",
           "x  ,y  ,z",
           "x+1,y  ,z",
           "x+2,y  ,z",
           "x+1,y  ,z-1"
         ],
      3: [
           "x-2,y  ,z",
           "x-1,y  ,z",
           "x  ,y  ,z",
           "x+1,y  ,z",
           "x  ,y  ,z-1"
         ],
      4: [
           "x-3,y  ,z",
           "x-2,y  ,z",
           "x-1,y  ,z",
           "x  ,y  ,z",
           "x-1,y  ,z-1"
         ],
      5: [
           "x-2,y  ,z+1",
           "x-1,y  ,z+1",
           "x  ,y  ,z+1",
           "x+1,y  ,z+1",
           "x  ,y  ,z"
         ]
    },
    180: {
      1: [
           "x  ,y  ,z",
           "x+1,y  ,z",
           "x+2,y  ,z",
           "x+3,y  ,z",
           "x+2,y+1,z"
         ],
      2: [
           "x-1,y  ,z",
           "x  ,y  ,z",
           "x+1,y  ,z",
           "x+2,y  ,z",
           "x+1,y+1,z"
         ],
      3: [
           "x-2,y  ,z",
           "x-1,y  ,z",
           "x  ,y  ,z",
           "x+1,y  ,z",
           "x  ,y+1,z"
         ],
      4: [
           "x-3,y  ,z",
           "x-2,y  ,z",
           "x-1,y  ,z",
           "x  ,y  ,z",
           "x-1,y+1,z"
         ],
      5: [
           "x-2,y-1,z",
           "x-1,y-1,z",
           "x  ,y-1,z",
           "x+1,y-1,z",
           "x  ,y  ,z"
         ]
    },
    270: {
      1: [
           "x  ,y  ,z",
           "x+1,y  ,z",
           "x+2,y  ,z",
           "x+3,y  ,z",
           "x+2,y  ,z+1"
         ],
      2: [
           "x-1,y  ,z",
           "x  ,y  ,z",
           "x+1,y  ,z",
           "x+2,y  ,z",
           "x+1,y  ,z+1"
         ],
      3: [
           "x-2,y  ,z",
           "x-1,y  ,z",
           "x  ,y  ,z",
           "x+1,y  ,z",
           "x  ,y  ,z+1"
         ],
      4: [
           "x-3,y  ,z",
           "x-2,y  ,z",
           "x-1,y  ,z",
           "x  ,y  ,z",
           "x-1,y  ,z+1"
         ],
      5: [
           "x-2,y  ,z-1",
           "x-1,y  ,z-1",
           "x  ,y  ,z-1",
           "x+1,y  ,z-1",
           "x  ,y  ,z"
         ]
    }
  },
  "Right": {
    0: {
      1: [
           "x  ,y  ,z",
           "x-1,y  ,z",
           "x-2,y  ,z",
           "x-3,y  ,z",
           "x-2,y-1,z"
         ],
      2: [
           "x+1,y  ,z",
           "x  ,y  ,z",
           "x-1,y  ,z",
           "x-2,y  ,z",
           "x-1,y-1,z"
         ],
      3: [
           "x+2,y  ,z",
           "x+1,y  ,z",
           "x  ,y  ,z",
           "x-1,y  ,z",
           "x  ,y-1,z"
         ],
      4: [
           "x+3,y  ,z",
           "x+2,y  ,z",
           "x+1,y  ,z",
           "x  ,y  ,z",
           "x+1,y-1,z"
         ],
      5: [
           "x+2,y+1,z",
           "x+1,y+1,z",
           "x  ,y+1,z",
           "x-1,y+1,z",
           "x  ,y  ,z"
         ]
    },
    90: {
      1: [
           "x  ,y  ,z",
           "x-1,y  ,z",
           "x-2,y  ,z",
           "x-3,y  ,z",
           "x-2,y  ,z-1"
         ],
      2: [
           "x+1,y  ,z",
           "x  ,y  ,z",
           "x-1,y  ,z",
           "x-2,y  ,z",
           "x-1,y  ,z-1"
         ],
      3: [
           "x+2,y  ,z",
           "x+1,y  ,z",
           "x  ,y  ,z",
           "x-1,y  ,z",
           "x  ,y  ,z-1"
         ],
      4: [
           "x+3,y  ,z",
           "x+2,y  ,z",
           "x+1,y  ,z",
           "x  ,y  ,z",
           "x+1,y  ,z-1"
         ],
      5: [
           "x+2,y  ,z+1",
           "x+1,y  ,z+1",
           "x  ,y  ,z+1",
           "x-1,y  ,z+1",
           "x  ,y  ,z"
         ]
    },
    180: {
      1: [
           "x  ,y  ,z",
           "x-1,y  ,z",
           "x-2,y  ,z",
           "x-3,y  ,z",
           "x-2,y+1,z"
         ],
      2: [
           "x+1,y  ,z",
           "x  ,y  ,z",
           "x-1,y  ,z",
           "x-2,y  ,z",
           "x-1,y+1,z"
         ],
      3: [
           "x+2,y  ,z",
           "x+1,y  ,z",
           "x  ,y  ,z",
           "x-1,y  ,z",
           "x  ,y+1,z"
         ],
      4: [
           "x+3,y  ,z",
           "x+2,y  ,z",
           "x+1,y  ,z",
           "x  ,y  ,z",
           "x+1,y+1,z"
         ],
      5: [
           "x+2,y-1,z",
           "x+1,y-1,z",
           "x  ,y-1,z",
           "x-1,y-1,z",
           "x  ,y  ,z"
         ]
    },
    270: {
      1: [
           "x  ,y  ,z",
           "x-1,y  ,z",
           "x-2,y  ,z",
           "x-3,y  ,z",
           "x-2,y  ,z+1"
         ],
      2: [
           "x+1,y  ,z",
           "x  ,y  ,z",
           "x-1,y  ,z",
           "x-2,y  ,z",
           "x-1,y  ,z+1"
         ],
      3: [
           "x+2,y  ,z",
           "x+1,y  ,z",
           "x  ,y  ,z",
           "x-1,y  ,z",
           "x  ,y  ,z+1"
         ],
      4: [
           "x+3,y  ,z",
           "x+2,y  ,z",
           "x+1,y  ,z",
           "x  ,y  ,z",
           "x+1,y  ,z+1"
         ],
      5: [
           "x+2,y  ,z-1",
           "x+1,y  ,z-1",
           "x  ,y  ,z-1",
           "x-1,y  ,z-1",
           "x  ,y  ,z"
         ]
    }
  },
  "Front": {
    0: {
      1: [
           "x  ,y  ,z",
           "x  ,y  ,z+1",
           "x  ,y  ,z+2",
           "x  ,y  ,z+3",
           "x-1,y  ,z+2"
         ],
      2: [
           "x  ,y  ,z-1",
           "x  ,y  ,z",
           "x  ,y  ,z+1",
           "x  ,y  ,z+2",
           "x-1,y  ,z+1"
         ],
      3: [
           "x  ,y  ,z-2",
           "x  ,y  ,z-1",
           "x  ,y  ,z",
           "x  ,y  ,z+1",
           "x-1,y  ,z"
         ],
      4: [
           "x  ,y  ,z-3",
           "x  ,y  ,z-2",
           "x  ,y  ,z-1",
           "x  ,y  ,z",
           "x-1,y  ,z-1"
         ],
      5: [
           "x+1,y  ,z-2",
           "x+1,y  ,z-1",
           "x+1,y  ,z",
           "x+1,y  ,z+1",
           "x  ,y  ,z"
         ]
    },
    90: {
      1: [
           "x  ,y  ,z",
           "x  ,y-1,z",
           "x  ,y-2,z",
           "x  ,y-3,z",
           "x-1,y-2,z"
         ],
      2: [
           "x  ,y+1,z",
           "x  ,y  ,z",
           "x  ,y-1,z",
           "x  ,y-2,z",
           "x-1,y-1,z"
         ],
      3: [
           "x  ,y+2,z",
           "x  ,y+1,z",
           "x  ,y  ,z",
           "x  ,y-1,z",
           "x-1,y  ,z"
         ],
      4: [
           "x  ,y+3,z",
           "x  ,y+2,z",
           "x  ,y+1,z",
           "x  ,y  ,z",
           "x-1,y+1,z"
         ],
      5: [
           "x+1,y+2,z",
           "x+1,y+1,z",
           "x+1,y  ,z",
           "x+1,y-1,z",
           "x  ,y  ,z"
         ]
    },
    180: {
      1: [
           "x  ,y  ,z",
           "x  ,y  ,z-1",
           "x  ,y  ,z-2",
           "x  ,y  ,z-3",
           "x-1,y  ,z-2"
         ],
      2: [
           "x  ,y  ,z+1",
           "x  ,y  ,z",
           "x  ,y  ,z-1",
           "x  ,y  ,z-2",
           "x-1,y  ,z-1"
         ],
      3: [
           "x  ,y  ,z+2",
           "x  ,y  ,z+1",
           "x  ,y  ,z",
           "x  ,y  ,z-1",
           "x-1,y  ,z"
         ],
      4: [
           "x  ,y  ,z+3",
           "x  ,y  ,z+2",
           "x  ,y  ,z+1",
           "x  ,y  ,z",
           "x-1,y  ,z+1"
         ],
      5: [
           "x+1,y  ,z+2",
           "x+1,y  ,z+1",
           "x+1,y  ,z",
           "x+1,y  ,z-1",
           "x  ,y  ,z"
         ]
    },
    270: {
      1: [
           "x  ,y  ,z",
           "x  ,y+1,z",
           "x  ,y+2,z",
           "x  ,y+3,z",
           "x-1,y+2,z"
         ],
      2: [
           "x  ,y-1,z",
           "x  ,y  ,z",
           "x  ,y+1,z",
           "x  ,y+2,z",
           "x-1,y+1,z"
         ],
      3: [
           "x  ,y-2,z",
           "x  ,y-1,z",
           "x  ,y  ,z",
           "x  ,y+1,z",
           "x-1,y  ,z"
         ],
      4: [
           "x  ,y-3,z",
           "x  ,y-2,z",
           "x  ,y-1,z",
           "x  ,y  ,z",
           "x-1,y-1,z"
         ],
      5: [
           "x+1,y-2,z",
           "x+1,y-1,z",
           "x+1,y  ,z",
           "x+1,y+1,z",
           "x  ,y  ,z"
         ]
    }
  },
  "Back": {
    0: {
      1: [
           "x  ,y  ,z",
           "x  ,y  ,z+1",
           "x  ,y  ,z+2",
           "x  ,y  ,z+3",
           "x+1,y  ,z+2"
         ],
      2: [
           "x  ,y  ,z-1",
           "x  ,y  ,z",
           "x  ,y  ,z+1",
           "x  ,y  ,z+2",
           "x+1,y  ,z+1"
         ],
      3: [
           "x  ,y  ,z-2",
           "x  ,y  ,z-1",
           "x  ,y  ,z",
           "x  ,y  ,z+1",
           "x+1,y  ,z"
         ],
      4: [
           "x  ,y  ,z-3",
           "x  ,y  ,z-2",
           "x  ,y  ,z-1",
           "x  ,y  ,z",
           "x+1,y  ,z-1"
         ],
      5: [
           "x-1,y  ,z-2",
           "x-1,y  ,z-1",
           "x-1,y  ,z",
           "x-1,y  ,z+1",
           "x  ,y  ,z"
         ]
    },
    90: {
      1: [
           "x  ,y  ,z",
           "x  ,y-1,z",
           "x  ,y-2,z",
           "x  ,y-3,z",
           "x+1,y-2,z"
         ],
      2: [
           "x  ,y+1,z",
           "x  ,y  ,z",
           "x  ,y-1,z",
           "x  ,y-2,z",
           "x+1,y-1,z"
         ],
      3: [
           "x  ,y+2,z",
           "x  ,y+1,z",
           "x  ,y  ,z",
           "x  ,y-1,z",
           "x+1,y  ,z"
         ],
      4: [
           "x  ,y+3,z",
           "x  ,y+2,z",
           "x  ,y+1,z",
           "x  ,y  ,z",
           "x+1,y+1,z"
         ],
      5: [
           "x-1,y+2,z",
           "x-1,y+1,z",
           "x-1,y  ,z",
           "x-1,y-1,z",
           "x  ,y  ,z"
         ]
    },
    180: {
      1: [
           "x  ,y  ,z",
           "x  ,y  ,z-1",
           "x  ,y  ,z-2",
           "x  ,y  ,z-3",
           "x+1,y  ,z-2"
         ],
      2: [
           "x  ,y  ,z+1",
           "x  ,y  ,z",
           "x  ,y  ,z-1",
           "x  ,y  ,z-2",
           "x+1,y  ,z-1"
         ],
      3: [
           "x  ,y  ,z+2",
           "x  ,y  ,z+1",
           "x  ,y  ,z",
           "x  ,y  ,z-1",
           "x+1,y  ,z"
         ],
      4: [
           "x  ,y  ,z+3",
           "x  ,y  ,z+2",
           "x  ,y  ,z+1",
           "x  ,y  ,z",
           "x+1,y  ,z+1"
         ],
      5: [
           "x-1,y  ,z+2",
           "x-1,y  ,z+1",
           "x-1,y  ,z",
           "x-1,y  ,z-1",
           "x  ,y  ,z"
         ]
    },
    270: {
      1: [
           "x  ,y  ,z",
           "x  ,y+1,z",
           "x  ,y+2,z",
           "x  ,y+3,z",
           "x+1,y+2,z"
         ],
      2: [
           "x  ,y-1,z",
           "x  ,y  ,z",
           "x  ,y+1,z",
           "x  ,y+2,z",
           "x+1,y+1,z"
         ],
      3: [
           "x  ,y-2,z",
           "x  ,y-1,z",
           "x  ,y  ,z",
           "x  ,y+1,z",
           "x+1,y  ,z"
         ],
      4: [
           "x  ,y-3,z",
           "x  ,y-2,z",
           "x  ,y-1,z",
           "x  ,y  ,z",
           "x+1,y-1,z"
         ],
      5: [
           "x-1,y-2,z",
           "x-1,y-1,z",
           "x-1,y  ,z",
           "x-1,y+1,z",
           "x  ,y  ,z"
         ]
    }
  },
  "Top": {
    0: {
      1: [
           "x  ,y  ,z",
           "x  ,y  ,z+1",
           "x  ,y  ,z+2",
           "x  ,y  ,z+3",
           "x  ,y-1,z+2"
         ],
      2: [
           "x  ,y  ,z-1",
           "x  ,y  ,z",
           "x  ,y  ,z+1",
           "x  ,y  ,z+2",
           "x  ,y-1,z+1"
         ],
      3: [
           "x  ,y  ,z-2",
           "x  ,y  ,z-1",
           "x  ,y  ,z",
           "x  ,y  ,z+1",
           "x  ,y-1,z"
         ],
      4: [
           "x  ,y  ,z-3",
           "x  ,y  ,z-2",
           "x  ,y  ,z-1",
           "x  ,y  ,z",
           "x  ,y-1,z-1"
         ],
      5: [
           "x  ,y+1,z-2",
           "x  ,y+1,z-1",
           "x  ,y+1,z",
           "x  ,y+1,z+1",
           "x  ,y  ,z"
         ]
    },
    90: {
      1: [
           "x  ,y  ,z",
           "x  ,y-1,z",
           "x  ,y-2,z",
           "x  ,y-3,z",
           "x  ,y-2,z-1"
         ],
      2: [
           "x  ,y+1,z",
           "x  ,y  ,z",
           "x  ,y-1,z",
           "x  ,y-2,z",
           "x  ,y-1,z-1"
         ],
      3: [
           "x  ,y+2,z",
           "x  ,y+1,z",
           "x  ,y  ,z",
           "x  ,y-1,z",
           "x  ,y  ,z-1"
         ],
      4: [
           "x  ,y+3,z",
           "x  ,y+2,z",
           "x  ,y+1,z",
           "x  ,y  ,z",
           "x  ,y+1,z-1"
         ],
      5: [
           "x  ,y+2,z+1",
           "x  ,y+1,z+1",
           "x  ,y  ,z+1",
           "x  ,y-1,z+1",
           "x  ,y  ,z"
         ]
    },
    180: {
      1: [
           "x  ,y  ,z",
           "x  ,y  ,z-1",
           "x  ,y  ,z-2",
           "x  ,y  ,z-3",
           "x  ,y+1,z-2"
         ],
      2: [
           "x  ,y  ,z+1",
           "x  ,y  ,z",
           "x  ,y  ,z-1",
           "x  ,y  ,z-2",
           "x  ,y+1,z-1"
         ],
      3: [
           "x  ,y  ,z+2",
           "x  ,y  ,z+1",
           "x  ,y  ,z",
           "x  ,y  ,z-1",
           "x  ,y+1,z"
         ],
      4: [
           "x  ,y  ,z+3",
           "x  ,y  ,z+2",
           "x  ,y  ,z+1",
           "x  ,y  ,z",
           "x  ,y+1,z+1"
         ],
      5: [
           "x  ,y-1,z+2",
           "x  ,y-1,z+1",
           "x  ,y-1,z",
           "x  ,y-1,z-1",
           "x  ,y  ,z"
         ]
    },
    270: {
      1: [
           "x  ,y  ,z",
           "x  ,y+1,z",
           "x  ,y+2,z",
           "x  ,y+3,z",
           "x  ,y+2,z+1"
         ],
      2: [
           "x  ,y-1,z",
           "x  ,y  ,z",
           "x  ,y+1,z",
           "x  ,y+2,z",
           "x  ,y+1,z+1"
         ],
      3: [
           "x  ,y-2,z",
           "x  ,y-1,z",
           "x  ,y  ,z",
           "x  ,y+1,z",
           "x  ,y  ,z+1"
         ],
      4: [
           "x  ,y-3,z",
           "x  ,y-2,z",
           "x  ,y-1,z",
           "x  ,y  ,z",
           "x  ,y-1,z+1"
         ],
      5: [
           "x  ,y-2,z-1",
           "x  ,y-1,z-1",
           "x  ,y  ,z-1",
           "x  ,y+1,z-1",
           "x  ,y  ,z"
         ]
    }
  },
  "Bottom": {
    0: {
      1: [
           "x  ,y  ,z",
           "x  ,y  ,z-1",
           "x  ,y  ,z-2",
           "x  ,y  ,z-3",
           "x  ,y-1,z-2"
         ],
      2: [
           "x  ,y  ,z+1",
           "x  ,y  ,z",
           "x  ,y  ,z-1",
           "x  ,y  ,z-2",
           "x  ,y-1,z-1"
         ],
      3: [
           "x  ,y  ,z+2",
           "x  ,y  ,z+1",
           "x  ,y  ,z",
           "x  ,y  ,z-1",
           "x  ,y-1,z"
         ],
      4: [
           "x  ,y  ,z+3",
           "x  ,y  ,z+2",
           "x  ,y  ,z+1",
           "x  ,y  ,z",
           "x  ,y-1,z-1"
         ],
      5: [
           "x  ,y+1,z+2",
           "x  ,y+1,z+1",
           "x  ,y+1,z",
           "x  ,y+1,z-1",
           "x  ,y  ,z"
         ]
    },
    90: {
      1: [
           "x  ,y  ,z",
           "x  ,y+1,z",
           "x  ,y+2,z",
           "x  ,y+3,z",
           "x  ,y+2,z-1"
         ],
      2: [
           "x  ,y-1,z",
           "x  ,y  ,z",
           "x  ,y+1,z",
           "x  ,y+2,z",
           "x  ,y+1,z-1"
         ],
      3: [
           "x  ,y-2,z",
           "x  ,y-1,z",
           "x  ,y  ,z",
           "x  ,y+1,z",
           "x  ,y  ,z-1"
         ],
      4: [
           "x  ,y-3,z",
           "x  ,y-2,z",
           "x  ,y-1,z",
           "x  ,y  ,z",
           "x  ,y-1,z-1"
         ],
      5: [
           "x  ,y-2,z+1",
           "x  ,y-1,z+1",
           "x  ,y  ,z+1",
           "x  ,y+1,z+1",
           "x  ,y  ,z"
         ]
    },
    180: {
      1: [
           "x  ,y  ,z",
           "x  ,y  ,z+1",
           "x  ,y  ,z+2",
           "x  ,y  ,z+3",
           "x  ,y+1,z+2"
         ],
      2: [
           "x  ,y  ,z-1",
           "x  ,y  ,z",
           "x  ,y  ,z+1",
           "x  ,y  ,z+2",
           "x  ,y+1,z+1"
         ],
      3: [
           "x  ,y  ,z-2",
           "x  ,y  ,z-1",
           "x  ,y  ,z",
           "x  ,y  ,z+1",
           "x  ,y+1,z"
         ],
      4: [
           "x  ,y  ,z-3",
           "x  ,y  ,z-2",
           "x  ,y  ,z-1",
           "x  ,y  ,z",
           "x  ,y+1,z-1"
         ],
      5: [
           "x  ,y-1,z-2",
           "x  ,y-1,z-1",
           "x  ,y-1,z",
           "x  ,y-1,z+1",
           "x  ,y  ,z"
         ]
    },
    270: {
      1: [
           "x  ,y  ,z",
           "x  ,y-1,z",
           "x  ,y-2,z",
           "x  ,y-3,z",
           "x  ,y-2,z+1"
         ],
      2: [
           "x  ,y+1,z",
           "x  ,y  ,z",
           "x  ,y-1,z",
           "x  ,y-2,z",
           "x  ,y-1,z+1"
         ],
      3: [
           "x  ,y+2,z",
           "x  ,y+1,z",
           "x  ,y  ,z",
           "x  ,y-1,z",
           "x  ,y  ,z+1"
         ],
      4: [
           "x  ,y+3,z",
           "x  ,y+2,z",
           "x  ,y+1,z",
           "x  ,y  ,z",
           "x  ,y+1,z+1"
         ],
      5: [
           "x  ,y+2,z-1",
           "x  ,y+1,z-1",
           "x  ,y  ,z-1",
           "x  ,y-1,z-1",
           "x  ,y  ,z"
         ]
    }
  }
}


# Initiate the solution matrix
# all spots are defined to be zeroes
# which indicates an empty spot
for x in range(N):
  solution.append([])
  for y in range(N):
    solution[x].append([])
    for z in range(N):
      solution[x][y].append(0)

# Prints the current version of the matrix
def printSolution():
  stringToPrint = ""
  for x in solution:
    stringToPrint += "\n"
    for y in x:
      stringToPrint += ", ".join(["%02d" %z for z in y])
      stringToPrint += " | "
  print stringToPrint
  
# Main function. It tries to find a path and 
# if found, print it. If not, report the status.
def solve():
  if findPath():
    print "Solved!"
    printSolution()
  else:
    print "Not solved :("

# Function for looking into depth
# Called recursively every time a piece is placed
# If a the function cannot find another piece to place on the next empty spot
# it will return False and thus the previous level of depth will continue trying
# to put another piece on the spot
def findPath():
  # Get the global definition of the matrix and piece
  # This is where we have gone so far
  global piece
  global solution
  
  # Try to get the next empty spot
  # If we get an empty list
  # Then the puzzle is solved
  nextSpot = nextEmptySpot()
  if nextSpot:
    x, y, z = nextSpot
  else:
    return True

  # Start fliping and rotating a piece, trying to fit it in the empty spot
  # If we succeed, we just call the function again and start looking for the next piece
  # If not, we backtrack to the previous level of depth
  for eachPart in allParts:
    for eachOrientation in allOrientations:
      for eachAngle in allAngles:
        # Use the last version of the matrix that has not been confirmed to be unsolvable
        # We then try to put another piece and if we succeed, we continue one level of depth further
        # If not, we get back here and revert the matrix, trying to put another pieces
        if putPiece(x,y,z,eachPart,eachOrientation,eachAngle):
          print "Putting piece # %d" %piece
          piece+=1 # We have successfully placed a new piece and start looking for the next one
          if findPath():
            return True
          else:
            # If there is not possible further path
            # We revert the change
            piece-=1
            removePiece(x,y,z,eachPart,eachOrientation,eachAngle)

  # If we are here, this means that the configuration that was present to the function did not
  # allow putting another piece so we get back one level of depth and try another configuration
  return False

# Looks for the next empty spot in the matrix
# returns an array with x, y, z coordinates of that spot
def nextEmptySpot():
  global piece
  global solution
  for i,x in enumerate(solution):
    for j,y in enumerate(x):
      for k,z in enumerate(y):
        if z == 0:
          return [i, j, k]
  # If no empty space found, this should mean that the matrix is filled
  # Which means that the puzzle is solved
  # Returning an empty list so that we can cast to boolean False
  return []

# Checks if a piece at specific part, orientation and angle
# can be inserted in a specific spot
# If yes, we put the piece and return True
# If not, we return False
def putPiece(x,y,z,part,orientation,angle):
  global pieceCoordinates
  stringArray = pieceCoordinates[orientation][angle][part]
  array = [eval(l) for l in stringArray]
  if existAndEmpty(array):
    fillSpots(array)
    return True
  return False

# Remove a piece, in other words - assign zeros in the matrix
# For all spots this piece takes
# This is used when reverting to a previous version of the matrix
def removePiece(x,y,z,part,orientation,angle):
  global pieceCoordinates
  stringArray = pieceCoordinates[orientation][angle][part]
  array = [eval(l) for l in stringArray]
  emptySpots(array)


# Checks if an array of spots in the matrix exist (coordinates are inside the matrix's boundaries)
# and if the spots are empty (meaning it's zero)
def existAndEmpty(array):
  global piece
  global solution
  global N
  for x, y, z in array:
    if (x<0 or y<0 or z<0) or (x>=N or y>=N or z>=N):
      return False
    if solution[x][y][z] != 0:
      return False
  return True

# Occupies all spots in the array
# Representing putting a piece in the matrix
# The matrix is filled with the value of piece variable
# so that we know which piece is where
def fillSpots(array):
  global piece
  global solution
  for x, y, z in array:
    solution[x][y][z] = piece

# Sets all spots for the array to zero
def emptySpots(array):
  global solution
  for x, y, z in array:
    solution[x][y][z] = 0

# Run the whole thing
solve()