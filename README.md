# Image-Processing-Scripts
Here are the image processing utility scripts I made for my art projects using the Pillow library in Python. These won't be actively developed, but they may be of some use to people.

## Image Grid:
Combines a set of images into a new image, making a grid arrangement. Parameters must be set in the script, and include the width and height for the images to be resized and/or cropped to if required, and the number of columns and rows for the grid. If the number is larger then the amount of images, some spaces will be left blank. When the script is run, a dialog will open so the directory of the images can be selected. Below is an example of using it as a way to get an overview comparison of large sets of outputs from a generative art project. It can also be used to make more careful arrangements, but it requires manually renaming the files so it is a rather labor intensive and tedious process with larger image sets.

![image](https://github.com/Metamere/Image-Processing-Scripts/assets/62861841/bf08fdf8-8304-4ab6-97af-1428db895fd8)

***

## Image Pair:
Processes a pair of images. They can be merged into one by placing them side by side in any arrangement and/or resized to various preset dimensions. It is designed to work with a pair of images, where one's filename will end with "-B". They can be mirrored horizontally or vertically, rotated either direction in 90 degree increments, Arranged AB or BA, and can also be overlapped and cropped by a number of pixels based on the starting dimensions. When run, it opens a dialog to allow for selection of one of the images in the pair. There are many setup parameters for the various options, including the ability to simply duplicate a single image, which is useful for creating a repeating pattern from the output of an image pairing operation.

![KoruTawa v26 2022-07-18 op 401](https://github.com/Metamere/Image-Processing-Scripts/assets/62861841/e0dd562a-f94f-41fb-be5b-65e9cc36f332)

![KoruTawa v26 2022-07-18 op 401-B](https://github.com/Metamere/Image-Processing-Scripts/assets/62861841/a257e8a5-1f49-4d46-9bb4-d12e6d361b58)

![KoruTawa v26 2022-07-18 #401-ABABABAB-hd](https://github.com/Metamere/Image-Processing-Scripts/assets/62861841/81787d16-1bb0-40b5-90f4-3de0239976cf)
