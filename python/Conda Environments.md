# [[Virtual Environments]]
# [[Conda Environments]] 
Conda environments are isolated spaces that allow you to manage different project dependencies without conflicts.  This is crucial when working on multiple projects that require different versions of Python or packages.

Key features:

* **Isolation:** Prevents dependency conflicts between projects.  If project A needs `pandas==[[1.0` and project B needs `pandas==[[2].0`, you can create separate environments to satisfy both.

* **Reproducibility:**  Easily recreate the exact environment used for a specific project, ensuring consistent results across different machines.  This is done via environment files (usually `.yml`).

* **Version control:** Manage different versions of Python and packages within each environment.

**Creating an environment:**

```bash
conda create -n myenv python=[[3].9 pandas numpy
```
This creates an environment named `myenv` with Python [[3].9, pandas, and numpy.  `-n` specifies the environment name.

**Activating an environment:**

```bash
conda activate myenv
```

**Deactivating an environment:**

```bash
conda deactivate
```

**Listing environments:**

```bash
conda env list
```

**Exporting an environment:**

```bash
conda env export > environment.yml
```

This creates a YAML file (`environment.yml`) that describes your environment.  You can then recreate it on another machine using:

```bash
conda env create -f environment.yml
```


**Removing an environment:**

```bash
conda env remove -n myenv
```

[[Conda Environment YAML Files]]  ([[Python Package Management]]) [[Virtual Environments]] vs [[Conda Environments]]
