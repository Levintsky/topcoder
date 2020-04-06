# Jupyter Notebook

## Resources
- https://jupyter.readthedocs.io/en/latest/index.html
- https://jupyter.org/try
- https://ipython.org/

## Configuration
- https://jupyter.readthedocs.io/en/latest/migrating.html
- IPython location
```
~/.ipython/profile_default/static/custom
~/.ipython/profile_default/ipython_notebook_config.py
~/.ipython/profile_default/ipython_nbconvert_config.py
~/.ipython/profile_default/ipython_qtconsole_config.py
~/.ipython/profile_default/ipython_console_config.py
```
- Jupyter location
```
~/.jupyter/custom
~/.jupyter/jupyter_notebook_config.py
~/.jupyter/jupyter_nbconvert_config.py
~/.jupyter/jupyter_qtconsole_config.py
~/.jupyter/jupyter_console_config.py
```

## Running
```
jupyter notebook notebook.ipynb
jupyter notebook --port 9999
jupyter notebook --no-browser
jupyter notebook --help
```

## Architecture Guide
- All the other interfaces: the Notebook, the Qt console, ipython console in the terminal, and third party interfaces, use the **IPython Kernel**.
- The **IPython Kernel** is a separate process which is responsible for running user code, and things like **computing possible completions**.
- Frontends, like the notebook or the Qt console, communicate with the IPython Kernel using **JSON messages sent over ZeroMQ sockets**; the protocol used between the frontends and the IPython Kernel is described in Messaging in Jupyter.
	<img src="/Python/images/repos_map.png" alt="drawing" width="400"/>

## Examples
- IPython: https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks