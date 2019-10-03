import py_libsudoku

if __name__ == '__main__':
    b = py_libsudoku.Board
    if b.isValid:
        print("Board is valid!")
    else:
        print("Board is invalid!")
