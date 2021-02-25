# task: https://www.hackerrank.com/challenges/find-angle/problem

import math

def my_round(n):
    n = int(n + (0.5 if n > 0 else -0.5))
    return n

def find_angle(AB, BC):
    if 0 < AB <= 100 and 0 < BC <= 100:
        # finding hypotenuse
        AC = math.sqrt(AB**2 + BC**2)
        # angle MBC is equal angle ACB
        # ACB = asin(AB/AC)
        ACB = math.asin(AB / AC)
        # convert radians to degrees and round it.
        print(my_round(ACB * 180 / math.pi), "°", sep="")
    else:
        raise ValueError("values must be 0 < AB <= 100 and 0 < BC <= 100")
