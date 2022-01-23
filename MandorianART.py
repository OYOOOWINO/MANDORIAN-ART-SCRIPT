'''
The program uses recursion to generate a random Mandorian styled art.
'''
import turtle
from random import randrange, random

# Height and width of the turtle window
WIDTH = 1024
HEIGHT = 768


def drawSquare(x, y, w, h, color, tur):
    '''
    Draw a rectangle with the Lower Right corder at (x, y)
    The width of the rectangle is w and its height is h
    The fill color for the rectangle is specified by color
    '''

    tur.up()

    # First Corner
    tur.goto(x, y)
    tur.down()

    tur.fillcolor(color)
    tur.begin_fill()

    # Second Corner
    tur.goto(x+w, y)
    tur.up()
    tur.forward(2)
    tur.down()
    # Third Corner
    tur.goto(x+w, y+h)

    # Fourth Corner
    tur.goto(x, y+h)

    # Back to First Corner
    tur.goto(x, y)

    tur.end_fill()

    tur.up()
    tur.color(randomColor())


# randomly select a fill culor
def randomColor():
    '''
    Select a color randomly
    Return a random color as described in the assignment.
    This color is just a string with the name of the color
    '''
    r = random()
    if r < 0.0833:
        return "green"
    elif r < 0.1667:
        return "blue"
    elif r < 0.25:
        return "orange"
    elif r < 0.35:
        return "black"
    elif r < 0.45:
        return "red"
    elif r < 0.55:
        return "maroon"
    elif r < 0.65:
        return "violet"
    elif r < 0.75:
        return "cyan"
    elif r < 0.85:
        return "pink"
    else:
        return "indigo"


def split_horiz(x, y, w, h, tur):
    '''
    Split horizontally - So one rectangle is beside the other. 
    Make a recursive call to the "art" function for each smaller rectangle.
       +----------+            +----+-----+
       |          |            |    |     |
       |          |  Becomes   |    |     |
       +----------+            +----+-----+
    '''
    # Choose the split point on X randomly,between 33% >= w <= 67% of
    # generate number between 0.33 and 0.68 0.33 included
    splitPointX = round(randrange(33, 68) / 100 * w)

    # recursive call on the subdivided rectangles

    # recursion on the left recttngle
    art(x, y, splitPointX, h, tur)
    # recursion on the right rectangle
    art(x + splitPointX, y, w - splitPointX, h, tur)


def split_vert(x, y, w, h, tur):
    '''
    Split Vertically - So one rectangle is above the other
    Make a recursive call to the "art" function for each smaller rectangle.
       +---+            +---+
       |   |            |   |
       |   |  Becomes   |   |
       |   |            +---+
       |   |            |   |
       +---+            +---+
    '''
    # Choose the split point on Y randomly,between 33% >= h <= 67% of
    # generate number between 0.33 and 0.68 0.33 included
    splitPointY = round(randrange(33, 68) / 100 * h)

    # recursion on the top rectangle
    art(x, y, w, splitPointY, tur)

    # recursion on the bottom recttngle
    art(x, y + splitPointY, w, h - splitPointY, tur)


def split_both(x, y, w, h, tur):
    '''
    Split both vertically and horizontally
    Make a recursive call to the "art" function for each smaller rectangle.
       +------------------+         +-------------+----+
       |                  |         |             |    |
       |                  | Becomes |             |    |
       |                  |         |             |    |
       |                  |         +-------------+----+
       |                  |         |             |    |
       +------------------+         +-------------+----+
    '''
    # Choose the split point on X randomly,between 33% >= w <= 67% of
    splitPointX = round(randrange(33, 68) / 100 * w)
    # Choose the split point on Y randomly,between 33% >= h <= 67% of
    splitPointY = round(randrange(33, 68) / 100 * h)

    # recursion call on the subdivision of the rectangles

    # recursion on the top left rectangle
    art(x, y, splitPointX, splitPointY, tur)

    # recursion call on the top right rectangel
    art(x + splitPointX, y, w - splitPointX, splitPointY, tur)

    # recursion call on the bottom left rectangel
    art(x, y + splitPointY, splitPointX, h - splitPointY, tur)

    # recursion call on the bottom right rectangel
    art(x + splitPointX, y + splitPointY, w - splitPointX, h - splitPointY, tur)


def doSplit(dim):
    '''
    Decide at random whether or not to split
    '''
    # Generate a random integer r between 120 and 1.5 × dim in steps of 121
    r = randrange(120, max(round(1.5 * dim) + 1, 120 + 1))
    # if generated number < dim return true else return false
    if r < dim:
        return True
    return False


def art(x, y, w, h, tur):
    '''
    Uses recursion to draw "art" in a Mondrian style
    Input is a rectangle with bottom left corner at (x, y) 
    and with width w and height h.
    '''
    make_horizontal_split = False
    make_vertical_split = True

    # Split depending on the size of Height and Width
    # both h and w > half WIDTH and HEIGHT
    if w > WIDTH * 0.05 and h > HEIGHT * 0.05:
        make_horizontal_split = True
        make_vertical_split = True
    # only w > half Width
    elif w > WIDTH * 0.05:
        make_horizontal_split = True
        make_vertical_split = False
    # only h > half width
    elif h > HEIGHT * 0.05:
        make_horizontal_split = False
        make_vertical_split = True
    # other cases
    else:
        # Randomly decide on to split or not
        if doSplit(w) and doSplit(h):
            make_horizontal_split = True
            make_vertical_split = True
        elif doSplit(w):
            make_horizontal_split = True
            make_vertical_split = False
        elif doSplit(h):
            make_horizontal_split = False
            make_vertical_split = True
        else:
            make_horizontal_split = False
            make_vertical_split = False

    # execute splitting based on decision made above
    if make_vertical_split and make_horizontal_split:
        split_both(x, y, w, h, tur)
    elif make_horizontal_split:
        split_horiz(x, y, w, h, tur)
    elif make_vertical_split:
        split_vert(x, y, w, h, tur)
    else:
        drawSquare(x, y, x + w, y + h, randomColor(), tur)


def makeTurtle():
    '''
    Set up the turtle
    '''
    turtle.setworldcoordinates(-2, -2, WIDTH+18, HEIGHT+8)  # Trial and error
    turtle.setup()
    ourWindow = turtle.Screen()
    ourWindow.title('Mandorian Art')
    ourWindow.tracer(0)  # Comment this line to turn off animation
    tur = turtle.Turtle()
    tur.hideturtle()
    tur.speed(6)
    tur.width(1)
    turtle.hideturtle()

    return tur


def main():
    # You can uncomment the following line so you program will always behave the same
    # random.seed(1985)

    # Create the turtle
    tur = makeTurtle()

    # Draw the art
    art(0, 0, WIDTH, HEIGHT, tur)

    turtle.done()


main()
