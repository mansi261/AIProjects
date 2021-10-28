"""
We the undersigned promise that we have in good faith attempted to follow the principles of pair programming.
Although we were free to discuss ideas with others, the implementation is our own.
We have shared a common workspace (possibly virtually) and taken turns at the keyboard for the majority of the work that we are submitting.
Furthermore, any non programming portions of the assignment were done independently.
We recognize that should this not be the case, we will be subject to penalties as outlined in the course syllabus.
Paired Programmer_1: Rutuja Medhekar
Paired Programmer_2: Mansi Vyas
"""
from backtrack import backtracking_search
from constraint_prop import *
from csp_lib.backtrack_util import forward_checking, mrv
from csp_lib.sudoku import Sudoku

from os import path, write

if __name__ == "__main__":

    easy1 = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    harder1 = '4173698.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
# Printing Easy Sudoku
sudoku = Sudoku(easy1)
sudoku.display(sudoku.infer_assignment())
# Printing Easy Sudoku After Backtracking
print("Easy Sudoku after Backtracking")
backtracking_search(sudoku, select_unassigned_variable=mrv, inference=forward_checking)
sudoku.display(sudoku.infer_assignment())

# Printing Hard Sudoku
print("Sudoku Hard Problem")
sudoku_hard = Sudoku(harder1)
sudoku_hard.display(sudoku_hard.infer_assignment())

# Printing Easy Sudoku After Backtracking
print("Sudoku Hard After Backtracking")
backtracking_search(sudoku_hard, select_unassigned_variable=mrv, inference=forward_checking)
sudoku_hard.display(sudoku_hard.infer_assignment())
