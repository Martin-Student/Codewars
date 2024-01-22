"""
Title of task:
Basic Mathematical Operations (level 8kyu)

Description:
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples(Operator, value1, value2) --> output
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7
"""

def basic_op(operator, value1, value2):
    if operator == '+':
        plus = value1 + value2
        return plus
    elif operator == '-':
        minus = value1 - value2
        return minus
    elif operator == '*':
        multiply = value1 * value2
        return multiply
    elif operator == '/':
        divide = value1 / value2
        return divide
    else:
        print("Unknown operator!")