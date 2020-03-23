# Sudoku
A logic-based, combinatorial number-placement puzzle :boom:

The _objective_ is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contain all of the digits from 1 to 9. 
The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.

## Backtracking Algorithm
Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree).

## Sudoku Solver Algorithm
**Step 1:** Find a row, column of an unassigned cell.\
**Step 2:** Attempt to place digits 1-9 in the cell which fulfill the criteria.\
**Setp 3:** After assigning, recursively move to the next cell and try to fill it, if possible.\
**Step 4:** If not possible, reset the current cell that was just filled, backtrack and reassign the previous cell.\
**Step 5:** Once the board is full, by definition of the algorithm, a solution has been found.