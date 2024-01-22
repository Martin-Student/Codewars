"""
Title of task:
Beginner Series #4 Cockroach (level 8kyu)

Description:
The cockroach is one of the fastest insects.
Write a function which takes its speed in km per hour and returns it in cm per second,
rounded down to the integer (= floored).

For example:
1.08 --> 30
Note! The input is a Real number (actual type is language dependent) and is >= 0.
The result should be an Integer.
"""

import math

def cockroach_speed(s):
    cms = s * 27.777777777778
    cms = int(cms)
    return cms