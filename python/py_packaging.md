# Python Package and Environment

## Summaries and Popular Tools
- conda
- pip
- pipenv
- setuptools
- virtualenv
- wheel

## conda
- conda self
```bash
conda --version
conda update conda
```
- Environment
    - List all envs:
```bash
conda info --envs
conda env list
```
    - Create an environment
```bash
conda create --name snowflake biopython
source activate snowflakes

source deactivate
```
    - Clone an environment
```bash
conda create -n flowers --clone snowflakes
```
    - Remove an environment
```bash
conda remove -n flowers 
```
- Packages
    - List packages
```bash
conda list
```
    - Install a package
```bash
conda install --name bunnies beautifulsoup4
# same as
activate bunnies
conda install beautifulsoup4

# install from Anaconda.org
conda install--channel https：//conda .anaconda.ort/pandas bottleneck

# check online at pypi for packages
pip install xxx

# from source
python setup.py install
```
- To remove:
```bash
# To remove a package
conda remove -n bunnies iopro

# To remove an environment
conda remove -n snakes --all

# remove conda
rm -rf ~/miniconda 
```

## pip
- Look for packges: https://pypi.org/pypi/
- Install and update self
```bash
pip install -U pip
```
- Install a package
```bash
pip install PackageName                # latest version
pip install PackageName==1.0.4         # specific version
```
- Show package info (folder...)
```bash
pip show pkg
```
- Show all packages
```bash
pip list --outdated
pip list
```
- Install and uninstall
```bash
pip install -U pkg
pip uninstall pkg
```

## Setuptools
- 0. Sources:
	- https://setuptools.readthedocs.io/en/latest/userguide/index.html
	- https://pythonhosted.org/an_example_pypi_project/setuptools.html
	- https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/index.html
- 1. Install setuptools
```sh
pip install --upgrade setuptools
```
- 2. Write a setup
	- A setup.py should look like
```python
import os
from setuptools import setup
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
    name = "an_example_pypi_project",
    version = "0.0.4",
    author = "Andrew Carter",
    author_email = "andrewjcarter@gmail.com",
    description = ("An demonstration of how to create, document, and publish "
                                   "to the cheese shop a5 pypi.org."),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
```
	- With a folder structure like:
```
some_root_dir/
|-- README
|-- setup.py
|-- an_example_pypi_project
|   |-- __init__.py
|   |-- useful_1.py
|   |-- useful_2.py
|-- tests
|-- |-- __init__.py
|-- |-- runall.py
|-- |-- test0.py
```
- 3. CPP/Cuda extension
	- Case study (votenet): with cuda-only **ext_modules**
```python
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
# _ext_sources: a list with all .cpp and .cu files
# _ext_headers: all .h files
name='pointnet2'
ext_modules=[
    CUDAExtension(
        name="pointnet2._ext",
        sources=_ext_sources,
        extra_compile_args={
            "cxx": ["-O2", "-I{}".format("{}/include".format(_ext_src_root))],
            "nvcc": ["-O2", "-I{}".format("{}/include".format(_ext_src_root))],
        },
    )
]
cmdclass={"build_ext": BuildExtension}
```
	- Case study (pyrunner): with cpu-only **ext_modules**
```python
# _ext_sources: a list with all .cpp files
# _ext_headers: all .h files
ext_modules=[
    CppExtension (
        name='pointnet2._ext',
        sources=_ext_sources,
        extra_compile_args={
            "cxx": ["-O2", "-I{}".format("{}/include".format(_ext_src_root))],
        },
    )
]
cmdclass={"build_ext": BuildExtension}
```
	- Case study: OpenPCDet cuda-only **ext_modules**
```python
install_requires=['numpy', 'torch>=1.1', 'spconv', 'numba', 'tensorboardX', 'easydict', 'pyyaml']
packages=find_packages(exclude=['tools', 'data', 'output'])
cmdclass={"build_ext": BuildExtension}
# add them in one by one
ext_modules=[
    make_cuda_ext(
        name='iou3d_nms_cuda',
        module='pcdet.ops.iou3d_nms',
        sources=[
            'src/iou3d_cpu.cpp',
            'src/iou3d_nms_api.cpp',
            'src/iou3d_nms.cpp',
            'src/iou3d_nms_kernel.cu',
        ]
    ),
    make_cuda_ext(
        name='roiaware_pool3d_cuda',
        module='pcdet.ops.roiaware_pool3d',
        sources=[
            'src/roiaware_pool3d.cpp',
            'src/roiaware_pool3d_kernel.cu',
        ]
    ),...
]
# wrap a CUDAExtension module
def make_cuda_ext(name, module, sources):
    cuda_ext = CUDAExtension(
        name='%s.%s' % (module, name),
        sources=[os.path.join(*module.split('.'), src) for src in sources]
    )
    return cuda_ext
```
	- Case study: detectron2 (support both cpu and gpu)
```python
ext_modules = get_extensions() # get all extensions

def get_extensions():
	...
	extension = CppExtension
    extra_compile_args = {"cxx": []}
	if torch.cuda.is_available():
	    extension = CUDAExtension
	    sources += source_cuda
	    extra_compile_args["nvcc"] = [
                "-O3",
                "-DCUDA_HAS_FP16=1",
                "-D__CUDA_NO_HALF_OPERATORS__",
                "-D__CUDA_NO_HALF_CONVERSIONS__",
                "-D__CUDA_NO_HALF2_OPERATORS__",
        ]
    include_dirs = [extensions_dir]
    ext_modules = [
        extension(
            "detectron2._C",
            sources,
            include_dirs=include_dirs,
            define_macros=define_macros,
            extra_compile_args=extra_compile_args,
        )
    ]
    return ext_modules
```
	- Case study: torch vision (very similar to detectron2)
```python
def get_extensions():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    extensions_dir = os.path.join(this_dir, 'torchvision', 'csrc')

    main_file = glob.glob(os.path.join(extensions_dir, '*.cpp'))
    source_cpu = glob.glob(os.path.join(extensions_dir, 'cpu', '*.cpp'))
    source_cuda = glob.glob(os.path.join(extensions_dir, 'cuda', '*.cu'))

    sources = main_file + source_cpu
    extension = CppExtension

    define_macros = []

    extra_compile_args = {}
    if torch.cuda.is_available() and CUDA_HOME is not None:
        extension = CUDAExtension
        sources += source_cuda
        define_macros += [('WITH_CUDA', None)]
        nvcc_flags = os.getenv('NVCC_FLAGS', '')
        if nvcc_flags == '':
            nvcc_flags = []
        else:
            nvcc_flags = nvcc_flags.split(' ')
        extra_compile_args = {
            'cxx': ['-O0'],
            'nvcc': nvcc_flags,
        }

    sources = [os.path.join(extensions_dir, s) for s in sources]

    include_dirs = [extensions_dir]

    ext_modules = [
        extension(
            'torchvision._C',
            sources,
            include_dirs=include_dirs,
            define_macros=define_macros,
            extra_compile_args=extra_compile_args,
        )
    ]

    return ext_modules
```
- 4. Installation:
```sh
# build everything needed to install
python setup.py build
# clean up temporary files from 'build' command
python setup.py clean
# install everything from build directory
python setup.py install
# create a source distribution (tarball, zip file, etc.)
python setup.py sdist
# create a built (binary) distribution
python setup.py bdist
# install package in 'development mode'
python setup.py develop
```
- 4. Trouble shooting:
	- In case of on macbook with error "cstddef not found":
```sh
CFLAGS='-stdlib=libc++' python setup.py build
```
	- The folder in your build with .so file might not be copied automatically (only the .egg file is moved)
		- You have to copy them yourself;
- 5. Register online
```sh
python setup.py register
```
