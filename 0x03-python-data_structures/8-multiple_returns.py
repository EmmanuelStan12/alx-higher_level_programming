#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_letter = None
    if length != 0:
        first_letter = sentence[0]
    return (length, first_letter)
