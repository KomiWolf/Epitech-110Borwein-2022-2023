from borwein import *

def midpoint(n) -> float:
    midpoint_result = 0
    a = 0
    b = 0.5
    while b <= 5000:
        midpoint = float((b - a) * (borwein_calc(n, ((a + b) / 2))))
        midpoint_result += midpoint
        a = a + 0.5
        b = b + 0.5
    diff = pi_difference(midpoint_result)
    print("Midpoint:")
    print("I", n, " = ", "{:.10f}".format(midpoint_result), sep='')
    print("diff =", "{:.10f}".format(diff))
    print()
