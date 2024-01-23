"""
Title of task:
Invert values (level 8kyu)

Description:
Given a set of numbers, return the additive inverse of each.
Each positive becomes negatives, and the negatives become positives.
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
= []
You can invert([]) =assume that all values are integers.
Do not mutate the input array/list.
"""

def invert(lst):
    result_list = []
    for num in lst:
        result_list.append(num * (-1))
    return result_list

tablica = [1,2,3,4,5]
tablica2 = [1,-2,3,-4,5]
tablica3 = []

print(invert(tablica2))