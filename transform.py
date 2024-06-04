# transform.py
# ------------
# By MWC Contributors
# The functions in this module transform data. 
# None of them are finished; this is your job!

def maximum(data):
    "Returns the biggest number in data"
    highest = None
    for number in data:
        if highest is None:
            highest = number
        if number > highest:
            highest = number
    return highest

def minimum(data):
    "Returns the smallest number in data"
    lowest = None
    for number in data:
        if lowest is None:
            lowest = number
        if number < lowest:
            lowest = number
    return lowest
def bounds(data):
    "Returns a list of the smallest and largest numbers in data"
    return min(data), max(data)

def clamp(value, low, high):
    """Clamps a value to a range from low to high. 
    Returns value if it is between low and high.
    If value is lower than low, returns low. If value is higher than high, returns high.
    """
    if value >= low and value <= high:
        return value
    elif value > high:
        return "High" ,m
    else:
        return "Low"

def ratio(value, start, end):
    """Returns a number from 0.0 to 1.0, representing how far along value is from start to end.
    The return value is clamped to [0, 1], so even if value is lower than start, the return 
    value will not be lower than 0.0.
    """
    return (value - start) / (end - start)


def scale(value, domain_min, domain_max, range_min, range_max):
    "Given a value within a domain, returns the scaled equivalent within range."
    #raise NotImplementedError
    r = ratio(value, domain_min, domain_max)
    return range_min + r * (range_max - range_min)

def get_x_values(points):
    "Returns the first value for each point in points."
    x_vals = points[0]
    return x_vals

def get_y_values(points):
    y_vals = points[1]
    return y_vals
