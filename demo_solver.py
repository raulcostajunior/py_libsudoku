import py_libsudoku as lsk

solvable_one_solution = lsk.Board(
    [0, 0, 6, 0, 0, 8, 5, 0, 0,
     0, 0, 0, 0, 7, 0, 6, 1, 3,
     0, 0, 0, 0, 0, 0, 0, 0, 9,
     0, 0, 0, 0, 9, 0, 0, 0, 1,
     0, 0, 1, 0, 0, 0, 8, 0, 0,
     4, 0, 0, 5, 3, 0, 0, 0, 0,
     1, 0, 7, 0, 5, 3, 0, 0, 0,
     0, 5, 0, 0, 6, 4, 0, 0, 0,
     3, 0, 0, 1, 0, 0, 0, 6, 0]
)

solution = lsk.Board()

solver = lsk.Solver()

print("Board to be solved - 'solvable_one_solution': {}"
      .format(solvable_one_solution))

print("Looking for solution ...")

result = solver.solve(solvable_one_solution, solution)
if result == lsk.SolverResult.NO_ERROR:
    print("... solution found: {}".format(solution))
    print("Is solution ok? {}"
          .format(solution.isComplete))
else:
    print("... could not find solution :(")
