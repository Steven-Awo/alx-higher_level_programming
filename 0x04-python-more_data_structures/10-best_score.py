#!/usr/bin/python3
def best_score(a_dictionary):
    dirtry = a_dictionary
    if not dirtry:
        return (None)
    return (max(dirtry, key=a_dictionary.get))
