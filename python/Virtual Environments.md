# [[Modules and Packages]]
# [[Virtual Environments]] 
Python's strength lies in its vast ecosystem of packages.  However, managing dependencies between different projects can become a nightmare without proper tools.  This is where virtual environments shine.

A virtual environment is an isolated space where you can install packages without affecting your system's global Python installation or other projects.  This prevents conflicts and ensures that each project has its own specific set of dependencies.

**Creating a Virtual Environment:**

The most common way is using `venv` (Python [[3].[[3]+):

```bash
python3 -m venv .venv  # Creates a virtual environment named '.venv' in the current directory
```

Other tools exist, like `conda` (often used with Anaconda):

```bash
conda create -n myenv python=[[3].9  # Creates a conda environment named 'myenv' with Python [[3].9
```

**Activating a Virtual Environment:**

After creation, you need to activate it to use it:

* **venv:**
    * Linux/macOS:  `source .venv/bin/activate`
    * Windows:  `.venv\Scripts\activate`

* **conda:**
    * `conda activate myenv`


**Installing Packages:**

Once activated, use `pip` to install packages within the environment:

```bash
pip install requests numpy pandas
```

These packages will *only* be available within this specific environment.


**Deactivating a Virtual Environment:**

To exit the environment and return to your system's default Python:

```bash
deactivate
```


[[Package Management with Pip]]  ([[Conda Environments]])
