from borwein import *

def simpson(n) -> float:
    simpson_result = 0
    a = 0
    b = 0.5
    while b <= 5000:
        simpson = float((borwein_calc(n, a) + borwein_calc(n, b)))
        simpson += float(4 * borwein_calc(n, ((a + b) / 2)))
        simpson *= float((b - a) / 6)
        simpson_result += simpson
        a = a + 0.5
        b = b + 0.5
    diff = pi_difference(simpson_result)
    print("Simpson:")
    print("I", n, " = ", "{:.10f}".format(simpson_result), sep='')
    print("diff =", "{:.10f}".format(diff))