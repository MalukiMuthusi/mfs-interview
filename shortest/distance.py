
def distance(first, second):
    y = first[1] - second[1]
    x = first[0] - second[0]

    y = y*y
    x = x*x

    d = (y+x)**0.5

    return int(d)