from canvas import Canvas
from shapes import Square, Rectangle

canvasWidth = int(input("Enter canvas width: "))
canvasHeight = int(input("Enter canvas height: "))
canvasColorCode = {"white": [255, 255, 255], "black": [0, 0, 0]}
canvasColor = canvasColorCode[input("Enter canvas color(white or black): ")]
makeCanvas = Canvas(canvasWidth, canvasHeight, canvasColor)

while True:
    choice = input("Enter what shape do you want to draw(square or rectangle) / Press exit to quit: ")
    if choice == "square":

        # taking user input
        shapeX = int(input("Enter x coordinate(top left of the square): "))
        shapeY = int(input("Enter y coordinate(top left of the square): "))
        shapeSide = int(input("Enter side of the square: "))
        red = int(input("Enter value of red: "))
        green = int(input("Enter value of green: "))
        blue = int(input("Enter value of blue: "))

        shape = Square(shapeX, shapeY, shapeSide, [red, green, blue])
        shape.draw(makeCanvas)

    elif choice == "rectangle":

        # taking user input
        shapeX = int(input("Enter x coordinate(top left of the rectangle): "))
        shapeY = int(input("Enter y coordinate(top left of the rectangle): "))
        shapeWidth = int(input("Enter width of the rectangle: "))
        shapeHeight = int(input("Enter height of the rectangle: "))
        red = int(input("Enter value of red: "))
        green = int(input("Enter value of green: "))
        blue = int(input("Enter value of blue: "))

        shape = Rectangle(shapeX, shapeY, shapeWidth, shapeHeight, [red, green, blue])
        shape.draw(makeCanvas)

    elif choice == "exit":
        print("Exited")
        break

    else:
        print("Invalid Choice")

# saving the created image as - image.png
makeCanvas.make("image.png")
