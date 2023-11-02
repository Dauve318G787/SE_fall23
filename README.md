# SE_fall23

This program takes a user given URL, processes the URL and sends the processed file to OpenAI API

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

# Project 4

Specifically for this project we need an API key. So you must create a .env file or use global environment variables.
Look at module_4 to see how to authenticate your API key and the environment variable name