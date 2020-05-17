cmake_minimum_required(VERSION 2.8.12)
project(example)

# option(WITH_DSO         "Compile PaddlePaddle with dynamic linked CUDA" ON)
# option(PYTHON_EXECUTABLE:FILEPATH "Which Python to Build" "/usr/bin/python")

add_subdirectory(pybind11)

# find_package(pybind11)
pybind11_add_module(example example.cc)
