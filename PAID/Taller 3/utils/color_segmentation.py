import requests
from skimage import io
from skimage import color
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Planetas
# url = "https://github.com/PacktPublishing/Python-Image-Processing-Cookbook/blob/master/Chapter%2004/images/planets.png?raw=true"
# Loto
# url = "https://github.com/PacktPublishing/Python-Image-Processing-Cookbook/blob/master/Chapter%2004/images/lotus.png?raw=true"
# Flor
# url = "https://red-viajes.com/wp-content/uploads/2019/09/8-flores-tropicales-encontradas-en-tahiti.jpg"
# Flor del beso
# url = "https://www.guiadejardineria.com/wp-content/uploads/2015/04/Psychotria-elata-1.jpg"
# Colibrí 1
# url = "https://hablemosdeaves.com/wp-content/uploads/2017/06/colibr%C3%AD-azul-5-300x166.jpg"
# Colibrí 2
# url = "https://i.blogs.es/e56933/colibri/450_1000.jpg"
# Flor
# url = "https://s1.significados.com/foto/photo-credit-dora-alis-on-visualhunt_bg.png"
# Brain Tumor MRI
# url = "https://docs.google.com/uc?export=download&id=1FDuWDGlTfUkLfi3dpApHPKlTlMlMtHYV"

def download_image(url, filename="image.jpg"):
    """
    Function that downloads and opens the image
    :param url: the url of the image
    :param filename: the filename of the image
    :return: the image loaded in memory
    """
    # We get the image address
    r = requests.get(url)

    # We open the image in "write-mode"
    with open(filename, "wb") as f:
        # We write the content to the file
        f.write(r.content)

    # Read the image with the module imread
    img = io.imread(filename)

    # Print the image shape
    print(f"The shape of the image is: {img.shape}")
    return img

def segmentation_demo(img, n_colors=(10, 8, 6, 4, 2), gray=False):
    """
    The function to perform the segmentation demo using KMeans
    algorithm
    :param img: the image to be used
    :param n_colors: the number of color we want to segment
    :param gray: a boolean to know if the demo is on color or grayscale
    :return: the segmented images
    """
    # We rescale the image in order to have values between 0 and 1
    if gray:
        plt.gray()

        # We convert the image to grayscale
        orig_img = color.rgb2gray(img)

        # We reshape the image to have just a simple array of grayscale points
        X = orig_img.reshape(-1, 1)

    else:
        if img.max() == 255:
            img = img / 255

        # We reshape the image to have just a simple array of channels
        orig_img = img.copy()
        X = orig_img.reshape(-1, orig_img.shape[-1])

    # Take the shape of the image to be segmented
    shape_ = orig_img.shape

    # An empty array of the segmented images
    segmented_imgs = []

    # Let's begin the segmentation
    for n_clusters in n_colors:
        # Execute the KMeans algorithm over the image
        kmeans = KMeans(n_clusters=n_clusters, random_state=1234).fit(X)
        # Let's retrieve the segmented image
        segmented_img = kmeans.cluster_centers_[kmeans.labels_]
        # Reshape the segmented image to its original shape
        # and append to the array
        segmented_imgs.append(segmented_img.reshape(shape_))

    # The image plotting
    plt.figure(figsize=(10, 5))

    # Create the subplots for each segmented image
    # and start to plot
    plt.subplot(231)
    plt.imshow(orig_img)
    plt.title("Imagen Original")
    plt.axis("off")

    for idx, n_clusters in enumerate(n_colors):
        plt.subplot(2, 3, 2 + idx)
        plt.imshow(segmented_imgs[idx])
        plt.title(f"{n_clusters} Colores")
        plt.axis("off")

    plt.show()
    return segmented_imgs
