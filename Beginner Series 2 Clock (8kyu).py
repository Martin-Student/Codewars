"""
Title of task:
Beginner Series #2 Clock (level 8kyu)

Description:
Clock shows h hours, m minutes and s seconds after midnight.
Your task is to write a function which returns the time since midnight in milliseconds.
Example:
h = 0
m = 1
s = 1
result = 61000
Input constraints:
0 <= h <= 23
0 <= m <= 59
0 <= s <= 59
"""

def past(h, m, s):
    hour_seconds = h * 3600
    minute_seconds = m * 60
    seconds_in_general = hour_seconds + minute_seconds + s
    miliseconds = seconds_in_general * 1000
    return miliseconds