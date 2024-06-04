# plotting.py
# ------------
# By MWC Contributors
# The functions in this module draw parts of a scatter plot. 
# These functions are all complete; you don't need to edit this file.

from turtle import *
import constants

def flyto(x, y):
    penup()
    goto(x, y)
    pendown()

def prepare_screen():
    """Sets up the screen for a plot.
    """
    screensize(constants.PLOT_WIDTH, constants.PLOT_HEIGHT)
    setworldcoordinates(
        -constants.PLOT_PADDING, 
        -constants.PLOT_PADDING, 
        constants.PLOT_WIDTH + constants.PLOT_PADDING,
        constants.PLOT_HEIGHT + constants.PLOT_PADDING,
    )

def draw_point(x, y, color, size):
    "Draws a dot at (x, y) screen position, using the color and size provided."
    flyto(x, y)
    dot(size, color)

def draw_x_axis():
    flyto(0, 0)
    goto(constants.PLOT_WIDTH, 0)

def draw_y_axis():
    flyto(0, 0)
    goto(0, constants.PLOT_HEIGHT)

def draw_y_tick(position, label):
    flyto(0, position)
    goto(-constants.TICK_LENGTH, position)
    write(label, align='right')

def draw_x_tick(position, label):
    flyto(position, 0)
    goto(position, -constants.TICK_LENGTH)
    flyto(position, -constants.TICK_LENGTH - 10)
    write(label, align='center')
