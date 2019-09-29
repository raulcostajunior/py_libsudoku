#include <pybind11/pybind11.h>
#include "board.h"
#include "generator.h"

namespace py = pybind11;

PYBIND11_MODULE(py_libsudoku, m) {
    py::class_<sudoku::Board>(m, "Board")
        .def(py::init())
        .def("isValid", &sudoku::Board::isValid);
}