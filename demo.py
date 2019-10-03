import py_libsudoku

if __name__ == '__main__':
    b = py_libsudoku.Board()
    print(b)
    print("Is board valid? {}".format(b.isValid))
