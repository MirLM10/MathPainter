class Square:
    """
    Object to create a square of specific side and color at
    specific coordinate of the canvas entered by the user
    """

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    # to draw the square
    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:
    """
    Object to create a rectangle of specific width and height and
    color at specific coordinate of the canvas entered by the user
    """

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    # to draw the rectangle
    def draw(self, canvas):
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color
