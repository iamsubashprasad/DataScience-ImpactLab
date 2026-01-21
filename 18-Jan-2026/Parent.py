import math

def area_circle(radius):
    return math.pi * radius * radius

def area_rectangle(length, width):
    return length * width


if __name__ == "__main__":

    radius = 11
    len = 7
    width = 3

    print("Area of Circle:", area_circle(radius))
    print("Area of Rectangle:", area_rectangle(len, width))