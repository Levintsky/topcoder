#include <pybind11/pybind11.h>

#include "example.h"

namespace py = pybind11;

PYBIND11_MODULE(_exp, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("add", &add, "A function which adds two numbers",
          py::arg("i")=1, py::arg("j")=2);

    // shorthand
    using namespace pybind11::literals;
    m.def("add2", &add, "i"_a=1, "j"_a=2);
}

