#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    values = list(a_dictionary.values())
    biggest = 0
    for value in values:
        if value > biggest:
            biggest = value
    keys = list(a_dictionary.keys())
    for key in keys:
        if a_dictionary[key] == biggest:
            return key
