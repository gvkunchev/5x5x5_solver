###########################################
#                                         #
#                                         #
#                                         #
#       Cube Solver Back Up Maker         #
#                                         #
#                                         #
#                                         #
###########################################

import os
import locale
from shutil import copyfile


# Used to format the number of moves in a readable way
locale.setlocale(locale.LC_ALL, '')

# Checks the current status and prepare the variables for the directory name
with open("cube_solver_log.dat") as f:
  logDict = eval(f.readlines()[0])
  moves = logDict["Movements"]
  solutions = logDict["Solutions"]
  f.close()


# Create the new directory and copy the files
pathName = "Log Back up/%s moves and %d solutions" %("{0:n}".format(moves).replace(',', ' '),solutions)
os.mkdir(pathName)
copyfile("cube_solver_log.dat", "%s/cube_solver_log.dat" %pathName)
copyfile("cube_solver_solution.dat", "%s/cube_solver_solution.dat" %pathName)
