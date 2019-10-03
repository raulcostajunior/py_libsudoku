#include "board.h"
#include "generator.h"
#include "solver.h"

#include <cstdint>
#include <iostream>
#include <sstream>
#include <vector>

#include <pybind11/pybind11.h>
namespace py = pybind11;

PYBIND11_MODULE(py_libsudoku, m) {
    m.doc() = "Python bindings for libsudoku";

    py::class_<sudoku::Board>(m, "Board")
        .def(py::init(), "Creates an empty board.")
        .def(py::init<const std::vector<std::uint8_t> &>(), 
             "Creates a board with the given values (up to 81 values between 0 and 9).")
        .def_property_readonly("isValid", &sudoku::Board::isValid,
             "True if the board has no invalid values nor repetitions of values "
             "across lines, columns or sections.")
        .def("__repr__",
             [](const sudoku::Board &board) {
                 std::ostringstream ostr;
                 ostr << "<py_libsudoku.Board:\n";
                 ostr << board;
                 ostr << ">\n";
                 return ostr.str();
                });

    py::class_<sudoku::Generator>(m, "Generator")
        .def(py::init());

    py::class_<sudoku::Solver>(m, "Solver")
        .def(py::init());
}

