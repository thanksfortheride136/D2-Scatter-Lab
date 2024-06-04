# scatterplot.py
# ------------
# By MWC Contributors
# Uses lots of helper functions in other modules to draw a scatter plot.

from turtle import *
from superturtle.movement import no_delay
import constants
from generate_data import generate_data
from ticks import get_tick_values
from plotting import (
    prepare_screen, 
    draw_x_axis, 
    draw_y_axis,
    draw_x_tick, 
    draw_y_tick,
    draw_point, 
)
from transform import (
    maximum, 
    minimum,
    bounds, 
    clamp,
    ratio, 
    scale,
    get_x_values,
    get_y_values,
)

def draw_scatterplot(data, size=5, color="black"):
    "Draws a scatter plot, showing the data"
    prepare_screen()
    draw_axes(data)
    draw_points(data, color, size)


def draw_axes(data):
    "Draws the scatter plot's axes."
    draw_x_axis()
    x_values = get_x_values(data)
    xmin, xmax = bounds(x_values)
    ticks = get_tick_values(xmin, xmax)
    for tick in ticks:
        screen_x_position = scale(tick, xmin, xmax, 0, constants.PLOT_WIDTH)
        draw_x_tick(screen_x_position, tick)

    draw_y_axis()
    y_values = get_y_values(data)
    ymin, ymax = bounds(y_values)
    ticks = get_tick_values(ymin, ymax)
    for tick in ticks:
        screen_y_position = scale(tick, ymin, ymax, 0, constants.PLOT_WIDTH)
        draw_x_tick(screen_y_position, tick)

def draw_points(data, color, size):
    "Draws the scatter plot's points."
    xmin, xmax = bounds(get_x_values(data))
    ymin, ymax = bounds(get_y_values(data))
    for x, y in data:
        scaled_x = scale(x, xmin, xmax, 0, constants.PLOT_WIDTH)
        scaled_y = scale(y, ymin, ymax, 0, constants.PLOT_HEIGHT)
        draw_point(scaled_x, scaled_y, color, size)

with no_delay():
    data = generate_data(50, 10, 500, 5, 400, 1000)
    draw_scatterplot(data, size=5, color="blue")
    hideturtle()
done()
