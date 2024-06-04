# ticks.py
# ------------
# By MWC Contributors
# The functions in this module calculate suitable placements 
# for ticks on a plot axis which will display values. 
# These functions are all complete; you don't need to edit this file.

from math import floor, ceil, log
from transform import bounds

def get_tick_values(low, high):
    """Returns a list of values to use for ticks (labeled points along an axis). 
    Includes the lowest value, a bunch of "nice" intermediate values, and the highest value.
    """
    tick_interval = get_tick_interval(high - low)
    first_tick = ceil(low / tick_interval) * tick_interval
    return [low] + list(range(first_tick, high, tick_interval)) + [high]

def get_tick_interval(span):
    """Returns a 'nice' interval for ticks across span.
    The interval is a power of ten (e.g. 1000, 100, 0.1)
    scaled so that there will be between 0 and 10 internal ticks.
    """
    log_span = log(span, 10)
    return 10 ** floor(log_span)

