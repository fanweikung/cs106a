"""
File: forestfire.py
This program highlights fires in an image by identifying
pixels who red intensity is more than INTENSITY_THRESHOLD times
the average of the red, green, and blue values at a pixel.
----------------
Those "sufficiently red" pixels are then highlighted in the
image and the rest of the image is turned grey, by setting the
pixels red, green, and blue values all to be the same average
value.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage

DEFAULT_FILE = 'images/greenland-fire.png'

def find_flames(filename):
    """
    This function should highlight the "sufficiently red" pixels
    in the image and grayscale all other pixels in the image
    in order to highlight areas of wildfires.
    """
    image = SimpleImage(filename)
    # TODO: your code here
    # Find pixels which are sufficiently red
    # A pixel is sufficiently red if its red value is greater than 
    # or equal to the avearage of the pixel's 3 RGB values
    for pixel in image:
        if is_sufficiently_red(pixel):
            #
            # Set pixel's red value to 255 and blue and gren values to 0 
            # for pixels that are sufficiently red
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:    
            #
            # All other pixels, set their RGB values to grayscale equivalent
            # by summing their RGB values, dividing by 3 and then setting their
            # RGB alues to all have this same "average value."
            average = (pixel.red + pixel.green + pixel.blue)/3
            pixel.red = average
            pixel.green = average
            pixel.blue = average

    return image

def is_sufficiently_red(pixel):
    return pixel.red > (pixel.red + pixel.green + pixel.blue)/3



def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the original fire
    original_fire = SimpleImage(filename)
    original_fire.show()

    # Show the highlighted fire
    highlighted_fire = find_flames(filename)
    highlighted_fire.show()

    
def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
