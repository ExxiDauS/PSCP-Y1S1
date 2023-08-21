"""[Midterm 2022] Heron of Alexandria"""

import math

def heron(var_a, var_b, var_c):
    'triangle'
    var_s = (var_a + var_b + var_c) / 2
    print("%.3f" % math.sqrt(var_s * (var_s - var_a) * (var_s - var_b) * (var_s - var_c)))

heron(float(input()), float(input()), float(input()))
