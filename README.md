# Aqueduc

Aqueduc is a small script used to move or copy files and folders using preconfigured parameters.\
It is usefull to automate recurring file transfers.

## Requirement

- Python 3 (tested with python 3.7.2)

## How to get

```console
git clone https://github.com/Mozenn/Aqueduc.git
```

## How to use

1. create a JSON configuration file following [Configuration-file](#Configuration-file) or by checking the files in data/ folder

2. From the directory where the script file is located, run :

```console
python aqueduc.py configFile/Relative/Path
```

## Tips

### Configuration file

Configurations files are in JSON format following this structure:

"Screenshot"

- target (str):
- sources (array)
  - path (str): Path of the source destination
  - options
    - overwrite (boolean): 
    - move (boolean):
    - size_limit (number): 
    - forbidden_extensions(array): 
    - last_date_allowed (str): 

### Other

- You can put the script .py file wherever you want and execute it from there, or add it to your PATH.
