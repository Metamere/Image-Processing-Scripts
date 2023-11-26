from PIL import Image
# Open image using Image module

import tkinter as tk
from tkinter import filedialog

# 1600 = hd (high definition, for social media)
# 1920 x 1280 = fhd (full hd)
# 2560 x 1440 = qhd (quad hd, aka 2k)
# 3840 x 2160 = 4k
# 7680 x 4320 = 8k
res_str = "4k"

res_str_list = ["hd", "fhd", "qhd", "4k", "8k", "10k", "12k", "14k", "max"]
res_list =     [1600, 1920,  2560,  3840, 7680, 10000, 12000, 14000, 99999]
max_final_image_dimension = res_list[res_str_list.index(res_str)]

crop_shift = 283  # pixels to remove from one side of each image. The side affected depends on pairing orientation.
image_merge = 1  # either merge the images to one, or save them separately, just resized
if not image_merge:
    crop_shift = 0

save = 1  # if save is off, just display the image for a review
show = 1  # only show final image(s) if this is on of if it is not saving
image_rotate = 0  # value here is number of quarter turns (range of integers 1-3, or 0 for off).
# Note that the flips occur after the rotation
A_flip_H = 0
A_flip_V = 0
B_flip_H = 0
B_flip_V = 0
A_first_override = 0
orientation_override = 0  # 1 for horizontal arrangement, -1 for vertical. 0 for automatic.
duplicated = 0  # set to 1 to duplicate a single image

root = tk.Tk()
root.withdraw()

image_name = filedialog.askopenfilename(title='select', filetypes=[("image", ".png"), ("image", ".jpg")])
base_image_extension = image_name[-4:len(image_name)]

if duplicated:
    image_name_A = image_name
    image_name_B = image_name
    duplicated = image_merge
elif image_name[-5] == "B":
    A_first = 0 if not A_first_override else 1
    image_name_B = image_name
    base_image_name = image_name[0:(len(image_name) - 6)]
    image_name_A = base_image_name + base_image_extension
else:
    A_first = 1
    image_name_A = image_name
    base_image_name = image_name[0:(len(image_name) - 4)]
    image_name_B = base_image_name + "-B" + base_image_extension

image_A = Image.open(image_name_A)
image_B = Image.open(image_name_B)
if image_rotate == 1:
    image_A = image_A.transpose(Image.Transpose.ROTATE_90)
    image_B = image_B.transpose(Image.Transpose.ROTATE_90)
elif image_rotate == 2:
    image_A = image_A.transpose(Image.Transpose.ROTATE_180)
    image_B = image_B.transpose(Image.Transpose.ROTATE_180)
elif image_rotate == 3:
    image_A = image_A.transpose(Image.Transpose.ROTATE_270)
    image_B = image_B.transpose(Image.Transpose.ROTATE_270)
if A_flip_H:
    image_A = image_A.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
if A_flip_V:
    image_A = image_A.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
if B_flip_H:
    image_B = image_B.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
if B_flip_V:
    image_B = image_B.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

width, height = image_A.size
AR = height/width
print(f"starting image dimensions = {width} x {height}, AR = {round(height/width, 3)}")

X_pair = False
Y_pair = False
if image_merge:
    if (height / width >= 1.125 or orientation_override == 1) and not orientation_override == -1:
        # if it's a taller image, set up side by side.
        # But if closer to square, keep vertical arrangement
        max_image_dim = max(2 * (width - crop_shift), height)
        X_pair = True
    else:
        max_image_dim = max(2 * (height - crop_shift), width)
        Y_pair = True
else:
    max_image_dim = max(width, height)

crop_X = crop_shift if X_pair else 0
crop_Y = crop_shift if Y_pair else 0

scale_factor = max_final_image_dimension / max_image_dim

if duplicated:
    image1 = image_A
    image2 = image_B
    suffix_abba = "DD"
elif A_first:
    image1 = image_A
    image2 = image_B
    suffix_abba = "-AB"
else:
    image1 = image_B
    image2 = image_A
    suffix_abba = "-BA"

if crop_shift > 0:
    left = 0
    top = 0
    right = width - left - crop_X
    bottom = height - crop_Y

    image1 = image1.crop((left, top, right, bottom))
    image2 = image2.crop((left + crop_X, top + crop_Y, width - left, height))
    width, height = image1.size
    print(f"cropped image dimensions = {width} x {height}")

if scale_factor < 1.0:
    image1R = image1.resize((round(width * scale_factor), round(height * scale_factor)))
    image2R = image2.resize((round(width * scale_factor), round(height * scale_factor)))
    width, height = image1R.size
    print(f"resized image dimensions = {width} x {height}")
else:
    image1R = image1
    image2R = image2
    print(f"desired size exceeds image dimensions, no resize necessary.")
    res_str = "max"

if image_merge:
    if X_pair:
        new_image = Image.new('RGB', (2 * image1R.size[0], image1R.size[1]), (250, 250, 250))
        new_image.paste(image1R, (0, 0))
        new_image.paste(image2R, (image2R.size[0], 0))
    else:
        new_image = Image.new('RGB', (image1R.size[0], 2 * image1R.size[1]), (250, 250, 250))
        new_image.paste(image1R, (0, 0))
        new_image.paste(image2R, (0, image2R.size[1]))

    width, height = new_image.size
    print(f"merged image dimensions = {width} x {height}, AR = {round(height/width, 3)}")
    if save:
        new_image.save(base_image_name + suffix_abba + "-" + res_str + ".png", "PNG")
    if show or not save:
        new_image.show()
else:
    if save:
        image1R.save(base_image_name + "-A-" + res_str + ".png", "PNG")
        image2R.save(base_image_name + "-B-" + res_str + ".png", "PNG")
    else:
        image1R.show()
        image2R.show()
# ---------------------------------------------------------------
