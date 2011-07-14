import solver
import sys

if __name__=='main':
    mySolver = solver.Solver()
    mySolver.load('data/puzzle-01-simple')

    print("Current puzzle:")
    print(mySolver.getCurrentPuzzleString())

    sys.exit(0)

#EOF

