"""
Title of task:
Sum Mixed Array (level 8kyu)

Description:
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
Return your answer as a number.
"""

def sum_mix(arr):
    sum = 0
    lst_int = []
    for i in arr:
        lst_int.append(int(i))

    for j in lst_int:
        sum += j
    return sum