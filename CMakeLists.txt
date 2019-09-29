cmake_minimum_required(VERSION 3.13.0)
project(py_libsudoku)

add_subdirectory(pybind11)
pybind11_add_module(py_libsudoku src/py_libsudoku.cpp)

add_subdirectory(libsudoku)
