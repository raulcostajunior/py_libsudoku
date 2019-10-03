import py_libsudoku

clear_board = py_libsudoku.Board()

print("clear_board = {}"
      .format(clear_board))

print("Is clear_board empty? {}"
      .format(clear_board.isEmpty))

print("Is clear_board valid? {}"
      .format(clear_board.isValid))

print("Is clear_board complete? {}"
      .format(clear_board.isComplete))

print()
print()

one_to_nine = py_libsudoku.Board([1, 2, 3, 4, 5, 6, 7, 8, 9])

print("one_to_nine = {}"
      .format(one_to_nine))

print("Is one_to_nine valid? {}"
      .format(one_to_nine.isValid))

print()
print()

one_to_nine_cpy = py_libsudoku.Board(one_to_nine)

print("one_to_nine_cpy = {}"
      .format(one_to_nine_cpy))

print("Is one_to_nine equal to its copy? {}"
      .format(one_to_nine == one_to_nine_cpy))

result = one_to_nine_cpy.setValueAt(1, 0, 1)
if result == py_libsudoku.SetValueResult.VALUE_INVALIDATES_BOARD:
      print("1 at (0,0) would make one_to_nine_cpy invalid.")
# Shows that setting was rejected.
print("Value at one_to_nine_cpy(1,0) = {}"
      .format(one_to_nine_cpy.valueAt(line=1, column=0)))

print()
print()

one_to_nine_cpy.clear()
print("one_to_nine_cpy after clear: {}"
      .format(one_to_nine_cpy))

print("Is one_to_nine still equal to its copy? {}"
      .format(one_to_nine == one_to_nine_cpy))

