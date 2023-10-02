# cs325_pj1

This program takes a user given URL, makes an HTTP GET request and returns the data to a text file

# Installation

You can clone this repository and run the yaml file for setup 

```
git clone <HTTPS/SSH/CLI>
python -m venv environment  # Create a new venv
source environment/bin/activate  # Activate the venv on Unix-like systems (use `activate.bat` on Windows)
pip install -r environment.yml  # Install packages from the YAML file
```

# Usage

```
python main.py https://old.<reddit URL>	# Omit "www" and replace with "old"
```