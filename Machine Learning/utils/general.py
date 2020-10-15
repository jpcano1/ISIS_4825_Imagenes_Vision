import numpy as np
import requests
import sys
from tqdm.auto import tqdm
import zipfile
import os
import matplotlib.pyplot as plt

"""
OS Functions
"""
def create_and_verify(*args):
    full_path = os.path.join(*args)
    exists = os.path.exists(full_path)
    if exists:
        return full_path
    else:
        raise FileNotFoundError("La ruta no existe")

def read_listdir(dir_):
    listdir = os.listdir(dir_)
    full_dirs = list()
    for d in listdir:
        full_dir = create_and_verify(dir_, d)
        full_dirs.append(full_dir)
    return np.sort(full_dirs)

"""
DataViz Functions
"""
def imshow(img, title=None, color=True, cmap="gray", 
            axis=False, ax=None):
    if not ax:
        ax = plt
    # Plot Image
    if color:
        ax.imshow(img)
    else:
        ax.imshow(img, cmap=cmap)

    # Ask about the axis
    if not axis:
        ax.axis("off")

    # Ask about the title
    if title:
        ax.title(title)

def visualize_subplot(imgs: list, titles: list, 
                    division: tuple, figsize: tuple=None, cmap="gray"):
    """
    An even more complex function to plot multiple images in one or
    two axis
    :param imgs: The images to be shown
    :param titles: The titles of each image
    :param division: The division of the plot
    :param cmap: Image Color Map
    :param figsize: the figsize of the entire plot
    """
    # We create the figure
    fig: plt.Figure = plt.figure(figsize=figsize)

    # Validate the figsize
    if figsize:
        fig.set_figwidth(figsize[0])
        fig.set_figheight(figsize[1])

    # We make some assertions, the number of images and the number of titles
    # must be the same
    assert len(imgs) == len(titles), "La lista de imágenes y de títulos debe ser del mismo tamaño"

    # The division must have sense w.r.t. the number of images
    assert np.prod(division) >= len(imgs)

    # A loop to plot the images
    for index, title in enumerate(titles):
        ax: plt.Axes = fig.add_subplot(division[0], 
                            division[1], index+1)
        ax.imshow(imgs[index], cmap=cmap)
        ax.set_title(title)
        plt.axis("off")

"""
Miscellaneous Functions
"""
def download_content(url, chnksz=1000, filename="image.jpg", zip=False):
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