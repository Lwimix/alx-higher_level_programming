#!/usr/bin/python3
"""My text_indentation module
Contains text_indentation() function
No importing done, no unique functions
Indents after ., :, ? characters
"""


def text_indentation(text):
    """Indents a text based on (. : ?)
    Takes in a string of text and looks for the delimiters
    """
    if not isinstance(text, str) or len(text) == 0:
        raise TypeError('text must be a string')
    check = 0
    for character in text:
        if character in '.?:':
            check = 1
            print("{}".format(character), end="")
            print("\n")
        else:
            if check == 1:
                print("{}".format(character.lstrip()), end="")
                check = 0
            else:
                print("{}".format(character), end="")
