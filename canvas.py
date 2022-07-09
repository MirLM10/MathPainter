import numpy as np
from PIL import Image


class Canvas:
    """
    Object to create the canvas of specific width
    and height and color entered by the user
    """

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.data = np.zeros(shape=(self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    # to draw the canvas
    def make(self, imagePath):
        image = Image.fromarray(obj=self.data, mode="RGB")

        # save the image formed
        image.save(fp=imagePath)
