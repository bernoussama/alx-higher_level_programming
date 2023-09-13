#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    if a_dictionary:
        for k, v in a_dictionary.items:
            if v > best:
                best = k
        return best
    else:
        return None
