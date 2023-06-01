from math import pi
from math import sin

def pi_difference(form) -> float:
    n = float(form - (pi / 2))
    if n >= 0:
        return n
    else:
        return -n

def borwein_calc(n, value) -> float:
    form = 0
    k = 0
    if value == 0:
        return 1
    while k <= n:
        denom = (2 * k) + 1
        num_form = sin(value / denom)
        denom_form = value / denom
        if k != 0:
            form *= (num_form / denom_form)
        else:
            form = (num_form / denom_form)
        k += 1
    return form
