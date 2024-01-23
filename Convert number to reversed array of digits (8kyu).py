"""
Title of task:
Convert number to reversed array of digits (level 8kyu)

Description:
Given a random non-negative number, you have to return
the digits of this number within an array in reverse order.
Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]
"""


def digitize(n):
    tablo = []
    n = str(n)
    for num in n:
        tablo.append(int(num))

    reversed_list = list(tablo)
    reversed_list.reverse()
    return reversed_list


