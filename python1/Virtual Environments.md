## Python [[Virtual Environments]]

### What is a Virtual Environment?
A Python virtual environment is an isolated and self-contained environment for running Python projects. It allows you to manage different versions of Python installations, install and manage different packages, and avoid conflicts with the system-wide Python installation.

### How to Use [[Virtual Environments]]
To create a virtual environment, use the following command:

```bash
python3 -m venv venv_name
```

where `venv_name` is the name of the virtual environment.

To activate the virtual environment, use:

```bash
source venv_name/bin/activate
```

To deactivate the virtual environment, use:

```bash
deactivate
```

### Code Examples
```bash
# create a virtual environment named 'myenv'
python3 -m venv myenv

# activate the 'myenv' virtual environment
source ./myenv/bin/activate

# install a package in the 'myenv' virtual environment
pip install numpy

# deactivate the 'myenv' virtual environment
deactivate
```

### Related Python Concepts

- [[Modules and Packages]]: Virtual environments help manage and isolate different versions of Python modules and packages.
- [[Installing and Managing Modules]]: Virtual environments allow you to install and manage packages specific to a project without affecting the system-wide Python installation.
- [[Python Package Index (PyPI) Publishing]]: Virtual environments help test and develop packages before publishing them to PyPI.
- [[Building and Distributing Python Packages]]: Virtual environments provide a controlled environment for building and distributing Python packages.
- [[Concurrency and Multithreading]]: Virtual environments can be used to create isolated environments for running multithreaded or concurrent applications.
# [[Python 1 Home]]