from random import randint, gauss

def generate_data(n, xmin, xmax, slope, intercept, error):
    sample = []
    for i in range(n):
        x = randint(xmin, xmax)
        y = round(gauss(intercept + x * slope, error))
        sample.append([x, y])
    return sample
