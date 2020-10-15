import numpy as np
import requests
import sys
from tqdm.auto import tqdm
import zipfile
import os

def download_content(url, chnksz=1000, filename="image.jpg", zip=False):
    """
    Función que se encarga de descargar un archivo deseado
    :param url: la url de descarga
    :param filename: El nombre del archivo
    :param zip: Boolean que indica si lo que se descarga 
    es zipfile
    """
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
    
    if zip:
        with zipfile.ZipFile(filename, "r") as zfile:
            print("\nExtrayedo Zip File...")
            zfile.extractall()
            print("Eliminando Zip File...")
            os.remove(filename)
    return