from sys import path
import requests
import sys
from tqdm.auto import tqdm
import numpy as np

def download_github_content(path, filename, chnksz=1000):
    url = ""
    
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