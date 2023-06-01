from borwein import *

def trapezoidal(n) -> float:
    trapezoidal_result = 0
    a = 0
    b = 0.5
    while b <= 5000:
        trapezoidal = float(((b - a) / 2) * (borwein_calc(n, a) + borwein_calc(n, b)))
        trapezoidal_result += trapezoidal
        a = a + 0.5
        b = b + 0.5
    diff = pi_difference(trapezoidal_result)
    print("Trapezoidal:")
    print("I", n, " = ", "{:.10f}".format(trapezoidal_result), sep='')
    print("diff =", "{:.10f}".format(diff))
    print()