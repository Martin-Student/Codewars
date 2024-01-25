"""
Title of task:
Isograms (level 7kyu)

Description:
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
"""
def is_isogram(string):
    tablo = []
    isIsogram = False
    for letter in string:
        tablo.append(letter.lower())

    unikalne = set(tablo)
    if len(tablo) == 0:
        isIsogram = True
    elif len(tablo) == len(unikalne):
        isIsogram = True

    return isIsogram