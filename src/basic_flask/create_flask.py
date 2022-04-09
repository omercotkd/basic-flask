import subprocess
import secrets
import os
import pathlib
import shutil

#Path for where the script is runing
path = os.getcwd()

#Path for this file 
this_path = pathlib.Path(__file__).parent.resolve()

def create():

    subprocess.run("python -m venv .venv")
    subprocess.run("mkdir Routes")
    subprocess.run("mkdir Modules")
    subprocess.run("touch .env requirements.txt")

    shutil.copy(f"{this_path}/creation_files/activate_this.py", f"{path}/.venv/scripts/activate_this.py")
    shutil.copy(f"{this_path}/creation_files/main.py", f"{path}/main.py")
    shutil.copy(f"{this_path}/creation_files/.gitignore", f"{path}/.gitignore")
    shutil.copy(f"{this_path}/creation_files/.flaskenv", f"{path}/.flaskenv")

    # Creates env file with random secret key
    with open(f"{path}\\.env", "w") as env:
        env.write(f"SECRET_KEY={secrets.token_hex(48)}\n")

    # active the new venv
    activator = f"{path}\\.venv\\scripts\\activate_this.py"
    with open(activator) as f:
        exec(f.read(), {'__file__': activator})

    # installing the modules in the venv
    subprocess.run("pip install flask python-dotenv")

    # updating requirements.txt
    with open(f"{path}\\requirements.txt", "w") as requirements:
        subprocess.run("pip3 freeze > requirements.txt", stdout=requirements)
