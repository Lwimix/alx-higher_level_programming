#!/usr/bin/python3
def multiple_returns(sentence):
    len_sentence = len(sentence)
    f_char = None
    if len_sentence == 0:
        return len_sentence, f_char
    else:
        f_char = sentence[0]
        return len_sentence, f_char
