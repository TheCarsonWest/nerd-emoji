# [[Virtual Environments]]
# Package Management with Pip

Pip is the standard package manager for Python.  It allows you to install, manage, and uninstall packages (libraries) easily.

**Key Commands:**

* **Installation:**
```bash
pip install <package_name>
```
   * To install a specific version:
   ```bash
   pip install <package_name>==<version>
   ```
   * To install from a requirements file:
   ```bash
   pip install -r requirements.txt
   ```
   ([[Requirements Files]])

* **Uninstallation:**
```bash
pip uninstall <package_name>
```

* **Listing Installed Packages:**
```bash
pip list
pip freeze  # Shows installed packages and their versions in requirements format.
```

* **Updating Packages:**
```bash
pip install --upgrade <package_name>
pip install --upgrade -r requirements.txt #Update all packages from requirements.txt
```

* **Searching for Packages:**
```bash
pip search <search_term>
```


**Virtual Environments:**  It's crucial to use virtual environments to isolate project dependencies.  Pip integrates well with `venv` (or `virtualenv`).

```bash
python3 -m venv .venv  # Creates a virtual environment named '.venv'
source .venv/bin/activate  # Activates the environment (Linux/macOS)
.venv\Scripts\activate  # Activates the environment (Windows)
pip install <package_name> # Install packages within the virtual environment
deactivate # Deactivates the environment
```
([[Virtual Environments]])


**Other Useful Options:**

* `--user`: Installs packages only for the current user.
* `-t <directory>`: Specifies the installation directory.
* `--index-url <url>`: Specifies an alternative PyPI index URL.


**Troubleshooting:**

* **Permission Errors:** You might need administrator privileges (sudo on Linux/macOS) to install packages globally.  Virtual environments are a better solution to avoid permission issues.
* **Network Issues:** Ensure you have a stable internet connection.
* **Proxy Settings:** If you're behind a proxy, you'll need to configure pip to use it. (see pip documentation)


[[Pip Configuration]]
[[Package Conflicts]]

