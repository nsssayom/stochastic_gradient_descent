# The documentation for p5 python version is not adequate enough
# to ignore star import. So, ignoring F405 warning of flake8
from p5 import *            # noqa ignore=F405
from decimal import *       # noqa ignore=F405
from decimal import *       # noqa ignore=F405
from shapely.geometry import LineString

from point import Point

# Global variables
width = 600
height = 700
points = []     # Data points

learning_rate = 0.3     # Learning rate
m = 1                   # Gradient
b = 0

# Fonts
sourceLight = create_font("SourceCodePro-Light.otf", 18)    # noqa ignore=F405
sourceBlack = create_font("SourceCodePro-Black.otf", 18)    # noqa ignore=F405
sourceBold = create_font("SourceCodePro-Bold.otf", 18)      # noqa ignore=F405
sourceMedium = create_font("SourceCodePro-Medium.otf", 18)  # noqa ignore=F405

# Run once


def setup():
    getcontext().prec = 2                   # noqa ignoe=F405
    size(width, height)                     # noqa ignore=F405
    text_font(sourceLight)                  # noqa ignore=F405
    no_stroke()                             # noqa ignore=F405
    background(200)                         # noqa ignore=F405


# Main loop
def draw():
    drawAxis()
    # Handel mouse press if in area
    if mouse_is_pressed and (mouse_x in range(50, 550)          # noqa ignore=F405
                            and mouse_y in range(50, 550)):     # noqa ignore=F405
        new_point = Point(mouse_x, mouse_y)     # noqa ignore=F405
        points.append(new_point)

    # Draw all points in points list
    for point in points:
        no_stroke()                                         # noqa ignore=F405
        fill(point.r, point.g, point.b)                     # noqa ignore=F405
        circle((point.x, point.y), 10, mode=CENTER)        # noqa ignore=F405

    # Calculate gradient decent and draw the line
    if len(points) > 1:
        gradient_decent()
        draw_line()


# Function to draw primary and secondary axis lines and labels
def drawAxis():
    text_font(sourceLight)          # noqa ignore=F405
    # Draw secondaty Y axis lines
    for x in range(100, 600, 50):
        stroke(180)                 # noqa ignore=F405
        stroke_weight(1)            # noqa ignore=F405
        line((x, 550), (x, 50))     # noqa ignore=F405

        # Draw Y axis labels
        no_stroke()                 # noqa ignore=F405
        text_font(sourceLight)      # noqa ignore=F405
        fill(0)                     # noqa ignore=F405
        text(str(600 - x), (10, x - 60))         # noqa ignore=F405

    # Draw secondaty X axis lines
    for y in range(0, 550, 50):
        stroke(180)                 # noqa ignore=F405
        stroke_weight(1)            # noqa ignore=F405
        line((50, y), (550, y))     # noqa ignore=F405

        # Draw X axis labels
        no_stroke()                 # noqa ignore=F405
        text_font(sourceLight)      # noqa ignore=F405
        fill(0)                     # noqa ignore=F405
        text(str(y), (y + 35, 550)) # noqa ignore=F405

    # Draw primary axis lines
    stroke(0)                       # noqa ignore=F405
    stroke_weight(4)                # noqa ignore=F405
    line((50, 550), (550, 550))     # noqa ignore=F405
    line((50, 550), (50, 50))       # noqa ignore=F405


# Function to calculate gradient decent
def gradient_decent():
    global m, b
    for point in points:
        x = remap(point.x, (50, 550), (0, 1))    # noqa ignore=F405
        y = remap(point.y, (550, 50), (0, 1))    # noqa ignore=F405

        guess = m * x + b
        err = y - guess
        m = m + ((err * x) * learning_rate)
        b = b + (err * learning_rate)


# Draw the gradient line
def draw_line():
    x1 = 0
    y1 = m * x1 + b
    x2 = 1
    y2 = m * x2 + b

    # Remaping values to scale for drawing into the canvas
    x1 = remap(x1, (0, 1), (50, 550))    # noqa ignore=F405
    y1 = remap(y1, (0, 1), (550, 50))    # noqa ignore=F405
    x2 = remap(x2, (0, 1), (50, 550))    # noqa ignore=F405
    y2 = remap(y2, (0, 1), (550, 50))    # noqa ignore=F405

    gradient_line = LineString([(x1, y1), (x2, y2)])
    x_axis_line = LineString([(50, 550), (550, 550)])
    y_axis_line = LineString([(50, 50), (550, 50)])

    # Avoiding gradient line to crosss defined area
    if y1 > 550:
        int_pt = x_axis_line.intersection(gradient_line)
        x1 = int_pt.x
        y1 = int_pt.y
    if y2 > 550:
        int_pt = x_axis_line.intersection(gradient_line)
        x2 = int_pt.x
        y2 = int_pt.y
    if y1 < 50:
        int_pt = y_axis_line.intersection(gradient_line)
        x1 = int_pt.x
        y1 = int_pt.y
    if y2 < 50:
        int_pt = y_axis_line.intersection(gradient_line)
        x2 = int_pt.x
        y2 = int_pt.y

    # Draw gradient line
    stroke(255, 0, 0)               # noqa ignore=F405
    stroke_weight(3)                # noqa ignore=F405
    line((x1, y1), (x2, y2))        # noqa ignore=F405

    # Refresh Screen
    background(200)                 # noqa ignore=F405
    drawAxis()

    # Print points of the gradient line
    no_stroke()                 # noqa ignore=F405
    text_font(sourceLight)      # noqa ignore=F405
    fill(0)                     # noqa ignore=F405
    text("x1: " + str(x1 - 50.0), (20, 580))     # noqa ignore=F405
    text("y1: " + str(y1 - 50.0), (20, 600))     # noqa ignore=F405
    text("x2: " + str(x2 - 50.0), (20, 620))     # noqa ignore=F405
    text("y2: " + str(y2 - 50.0), (20, 640))     # noqa ignore=F405

    text_font(sourceMedium)      # noqa ignore=F405
    fill(255, 51, 51)   # noqa ignore=F405
    text("Learning rate: " + str(learning_rate) + " [Press ↑/↓ to change]", (20, 660))     # noqa ignore=F405

    text_font(sourceBold)      # noqa ignore=F405
    fill(255, 0, 0)   # noqa ignore=F405
    text("y=" + str(round(m,2)) + "x+" + str(round(b,2)), (50, 10))     # noqa ignore=F405


# Keyboard input handeler
def key_pressed():
    global learning_rate

    if str(key) == 'UP':        # noqa ignore=F405
        if (learning_rate <= 0.99):
            learning_rate = float(Decimal(learning_rate) + Decimal(0.01))    # noqa ignore=F405
    if str(key) == 'DOWN':        # noqa ignore=F405
        if (learning_rate >= 0.01):
            learning_rate = float(Decimal(learning_rate) - Decimal(0.01))    # noqa ignore=F405


if __name__ == '__main__':
    run()                        # noqa ignore=F405