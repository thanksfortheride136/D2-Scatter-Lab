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

def test(function, arguments, expected):
    observed = function(*arguments)
    if observed != expected:
        args = ', '.join(str(arg) for arg in arguments) 
        print(f"Error: Expected {function}({args}) to equal {expected}, but it was {observed}")

test(maximum, [[0, 1, 2, 3]], 3)
test(maximum, [[-10, -20, -30]], -10)
test(minimum, [[0, 1, 2, 3]], 0)
test(minimum, [[-10, -20, -30]], -30)
test(bounds, [[0, 1, 2, 3]], [0, 3])
test(bounds, [[-10, -20, -30]], [-30, -10])
test(clamp, [[10, 0, 100]], 10)
test(clamp, [[-10, 0, 100]], 0)
test(clamp, [[104, 0, 100]], 100)
test(ratio, [[5, 0, 10]], 0.5)
test(ratio, [[167, 100, 200]], 0.67)
test(ratio, [[8, 10, 0]], 0.2)
test(ratio, [[4, 10, 20]], 0.0)
test(scale, [[4, 0, 10, 0, 100]], 40)
test(scale, [[180, 120, 240, 0, 100]], 50)
test(get_x_values, [[[0, 5], [1, 5], [2, 5]]], [0, 1, 2])
test(get_y_values, [[[0, 5], [1, 5], [2, 5]]], [5, 5, 5])
