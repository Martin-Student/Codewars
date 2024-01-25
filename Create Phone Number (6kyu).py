"""
Title of task:
Create Phone Number (level 6kyu)

Description:
Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!
"""

def create_phone_number(n):
    first = []
    second = []
    third = []

    for num in range(len(n)):
        if num in range(0, 3):
            first.append(str(n[num]))
        elif num in range(3, 6):
            second.append(str(n[num]))
        else:
            third.append(str(n[num]))

    pass1 = ""
    pass2 = ""
    pass3 = ""
    for num in first:
        pass1 += num
    for num in second:
        pass2 += num
    for num in third:
        pass3 += num

    final_number = (f"({pass1}) {pass2}-{pass3}")

    return final_number

# EASIER WAY
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"({num[0]}{num[1]}{num[2]}) {num[3]}{num[4]}{num[5]}-{num[6]}{num[7]}{num[8]}{num[9]}")