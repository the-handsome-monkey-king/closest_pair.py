#!/usr/bin/env python
"""closest_pair.py

A Python implementation of the closest pair of points problem."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import math
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def get_distance(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        return math.hypot(dx, dy)

def get_random_point():
    x = random.randint(0, 800)
    y = random.randint(0, 800)
    return Point(x, y)

def find_closest_pair(points):
    """Returns a list of Point objects that are closest together
    in the input list of Point objects."""

    min_dist = -1
    pair = []
    for i in range(len(points)):
            for j in range(i+1, len(points)):
                p1 = points[i]
                p2 = points[j]
                if min_dist == -1:
                    min_dist = p1.get_distance(p2)
                    pair = [p1, p2]
                else:
                    dist = p1.get_distance(p2)
                    if dist < min_dist:
                        min_dist = dist
                        pair = [p1, p2]
    return pair

def main():
    # random set of points
    point_amt = random.randint(10, 50)
    points = []
    for x in range(point_amt):
        points.append(get_random_point())
    print("Random set of points: {}\n\n".format(points))

    pair = find_closest_pair(points)
    print("Closest pair of points: {}\b".format(pair))
    dist = pair[0].get_distance(pair[1])
    print("Distance: {}\n".format(dist))

if __name__ == "__main__":
    main()
