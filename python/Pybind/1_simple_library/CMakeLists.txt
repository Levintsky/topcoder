cmake_minimum_required(VERSION 2.8.12)
project(example)

# option(WITH_DSO         "Compile PaddlePaddle with dynamic linked CUDA" ON)
# option(PYTHON_EXECUTABLE:FILEPATH "Which Python to Build" "/usr/bin/python")

add_subdirectory(pybind11)

# one step
# correct: different do it
# pybind11_add_module(example example2.cc)

# step 1:
add_library(exp example.cc)

# step 2:
pybind11_add_module(_exp pybind.cc)
target_link_libraries(_exp PRIVATE exp)