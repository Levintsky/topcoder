# Python Package and Environment

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
