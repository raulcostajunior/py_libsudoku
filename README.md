# py_libsudoku
Python binding for libsudoku - a C++ lib for generating and solving Sudoku puzzles.

# Setup
**py_libsudoku** references [**pybind11**](https://github.com/pybind/pybind11) and [**libsudoku**](https://github.com/raulcostajunior/libsudoku) as submodules. To clone **py_sudoku**, use:

    git clone --recurse-submodules git@github.com:raulcostajunior/py_libsudoku.git

To install in your current Python environment:

    cd [directory where py_libsudoku is]
    pip install .

To run the demo script with examples on how to generate
and solve puzzles:

    python demo.py


