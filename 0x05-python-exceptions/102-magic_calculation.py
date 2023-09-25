#!/usr/bin/python3
def magic_calculation(a, b):
    soln = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception('Too far')
            else:
                soln += a ** b / x
        except:
            soln = b + a
            break
    return (soln)
