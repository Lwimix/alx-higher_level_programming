#!/usr/bin/python3
def common(roma):
    add = 0
    if roma == "I":
        add = add + 1
    elif roma == "V":
        add = add + 1
    elif roma == "X":
        add = add + 10
    elif roma == "L":
        add = add + 50
    elif roma == "D":
        add = add + 500
    elif roma == "M":
        add = add + 1000
    elif roma == "C":
        add = add + 100
    return add


def roman_to_int(roman_string):
    roma = roman_string
    if not roman_string or not type(roma) == str:
        return None
    add = 0
    for i, rom in enumerate(roma):
        commoner = common(roma[i - 1])
        if rom == "I":
            add = add + 1
        elif rom == "V":
            add = add + 5
            if i > 0 and commoner < 5:
                add = add - (common(roma[i - 1])) * 2
        elif rom == "X":
            add = add + 10
            if i > 0 and commoner < 10:
                add = add - (common(roma[i - 1])) * 2
        elif rom == "L":
            add = add + 50
            if i > 0 and commoner < 50:
                add = add - (common(roma[i - 1])) * 2
        elif rom == "D":
            add = add + 500
            if i > 0 and commoner < 500:
                add = add - (common(roma[i - 1])) * 2
        elif rom == "M":
            add = add + 1000
            if i > 0 and commoner < 1000:
                add = add - (common(roma[i - 1])) * 2
        elif rom == "C":
            add = add + 100
            if i > 0 and commoner < 100:
                add = add - (common(roma[i - 1])) * 2
    return add
