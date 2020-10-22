import requests
import sys
from tqdm.auto import tqdm
import numpy as np
import os
from shutil import copyfile
from google.colab import files
from IPython.display import clear_output

def download_github_content(path, filename, chnksz=1000):
    url = f"https://raw.githubusercontent.com/jpcano1/ISIS_4825_Imagenes_Vision/main/Machine%20Learning/{path}"
    
    try:
        r = requests.get(url, stream=True)
    except Exception as e:
        print("Error de conexión con el servidor")
        sys.exit()
        
    with open(filename, "wb") as f:
        try:
            total = int(np.ceil(int(r.headers.get("content-length"))/chnksz))
        except:
            total = 0

        gen = r.iter_content(chunk_size=chnksz)

        for pkg in tqdm(gen, total=total, unit="KB"):
            f.write(pkg)

        f.close()
        r.close()
    return

def setup_kaggle_token(filename: str):
    assert filename.endswith(".json"), "El archivo no es JSON"
    files.upload()
    clear_output(wait=True)
    os.makedirs("~/.kaggle", exist_ok=True)
    copyfile(filename, "~/.kaggle/")
    os.chmod(f"~/.kaggle/{filename}", 0o600)

def setup_general():
    os.makedirs("utils", exist_ok=True)
    with open("utils/__init__.py", "wb"):
        pass

    download_github_content("utils/general.py", "utils/general.py")
    print("General Functions Enabled Successfully")

def setup_workshop_8():
    setup_general()
    print("Workshop 8 Enabled Successfully")

def setup_workshop_9(filename: str="kaggle.json"):
    setup_general()
    setup_kaggle_token(filename)
    os.system("pip install -q kaggle==1.5.6")
    print("Workshop 9 Enabled Successfully")

def setup_workshop_10():
    setup_general()
    print("Workshop 10 Enabled Successfully")

def setup_workshop_11():
    setup_general()
    print("Workshop 11 Enabled Successfully")

def setup_workshop_12():
    setup_general()
    print("Workshop 12 Enabled Successfully")

def setup_workshop_13():
    setup_general()
    print("Workshop 13 Enabled Successfully")
