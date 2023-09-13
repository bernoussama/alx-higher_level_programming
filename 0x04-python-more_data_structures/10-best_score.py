#!/usr/bin/python3
def best_score(a_dictionary):
    best = None
    max = 0
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > max:
                max = v
                best = k
    return best
