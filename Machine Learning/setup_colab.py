import requests
import sys
from tqdm.auto import tqdm
import numpy as np
import os

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

def setup_general():
    os.makedirs("utils", exist_ok=True)
    with open("utils/__init__.py", "wb"):
        pass

    download_github_content("utils/general.py", "utils/general.py")
    print("General Functions Enabled Successfully")

def setup_workshop_1():
    setup_general()
    print("Workshop 1 Enabled Successfully")

def setup_workshop_2():
    setup_general()
    print("Workshop 2 Enabled Successfully")

def setup_workshop_3():
    setup_general()
    print("Workshop 3 Enabled Successfully")

def setup_workshop_4():
    setup_general()
    print("Workshop 4 Enabled Successfully")

def setup_workshop_5():
    setup_general()
    print("Workshop 5 Enabled Successfully")

def setup_workshop_6():
    setup_general()
    print("Workshop 6 Enabled Successfully")