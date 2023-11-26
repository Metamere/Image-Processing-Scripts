import os
import PIL
import random
# from PIL import Image, ImageOps
import PIL.Image
import PIL.ImageOps
from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()

# Get list of image paths
image_paths_list = [os.path.join(folder_selected, f) for f in os.listdir(folder_selected) if f.endswith('.png')]


def image_grid(size, shape=None):

    # Open images and resize them
    images = map(PIL.Image.open, image_paths_list)

    images = [PIL.ImageOps.fit(img, size) for img in images]
    image_count = len(image_paths_list)
    print(image_count)
    width, height = size

    # Create canvas for the final image with total size
    shape_list = shape if shape else (1, len(images))
    image_size = (width * shape_list[0], height * shape_list[1])
    final_image = PIL.Image.new('RGB', image_size)

    # Paste images into final image
    for col in range(shape_list[0]):
        for row in range(shape_list[1]):
            offset = (width * col, height * row)
            idx = row + col * shape_list[1]
            if idx == image_count:
                return final_image
            final_image.paste(images[idx], offset)

    return final_image


# Create and save image grid
image = image_grid(size=(421, 750), shape=(9, 4))  # (width, height), (columns, rows)
image.save('image' + str(random.randint(0, 100000000)) + '.png', 'PNG')


# image = image_grid((800, 800), (3, 3))  # width x height
