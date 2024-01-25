def valid_braces(string):
    tablo = []
    valid_braces = False

    for i in string:
        tablo.append(i)
    istnieje_brace1 = False
    istnieje_brace2 = False
    istnieje_brace3 = False
    istnieje_brace4 = False
    istnieje_brace5 = False
    istnieje_brace6 = False
    first = 0
    second = 0
    nfirst = 0
    nsecond = 0
    zfirst = 0
    zsecond = 0
    for position in range(len(tablo)):
        letter = tablo[position]
        if letter == "{":
            first = position
            istnieje_brace1 = True
        elif letter == "}":
            second = position
            istnieje_brace2 = True
        elif letter == "[":
            nfirst = position
            istnieje_brace3 = True
        elif letter == "]":
            nsecond = position
            istnieje_brace4 = True
        elif letter == "(":
            zfirst = position
            istnieje_brace5 = True
        elif letter == ")":
            zsecond = position
            istnieje_brace6 = True

    if (istnieje_brace1 == True and istnieje_brace2 == True):
        if first < second:
            valid_braces = True

    elif istnieje_brace3 == True and istnieje_brace4 == True:
        if nfirst < nsecond:
            valid_braces = True

    elif istnieje_brace5 == True and istnieje_brace6 == True:
        if zfirst < zsecond:
            valid_braces = True

    elif nfirst + zfirst 

    return valid_braces
