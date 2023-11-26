# Image-Processing-Scripts
Some image processing utility scripts I made for my art projects.

Image Grid:
Combines a set of images into a new image, making a grid arrangement. Parameters must be set in the script, and include the width and height for the images to be resized and/or cropped to if required, and the number of columns and rows for the grid. If the number is larger then the amount of images, some spaces will be left blank. When the script is run, a dialog will open so the directory of the images can be selected.

Image Pair:
Processes a pair of images. They can be merged into one by placing them side by side in any arrangement and/or resized to various preset dimensions. It is designed to work with a pair of images, where one's filename will end with "-B". They can be mirrored horizontally or vertically, rotated either direction in 90 degree increments, Arranged AB or BA, and can also be overlapped and cropped by a number of pixels based on the starting dimensions. When run, it opens a dialog to allow for selection of one of the images in the pair. This process can be repeated multiple times by copying and renaming the resulting file, then rerunning.
