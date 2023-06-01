from flask import Flask, render_template, request
from math import pi
from math import sin

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/', methods=['POST'])
def calculate():
    n = int(request.form['n'])
    midpoint_result, diff_mid = midpoint(n)
    trapezoidal_result, diff_trap = trapezoidal(n)
    simpson_result, diff_simp = simpson(n)
    return render_template('result.html', n=n,
                           result_mid=midpoint_result, diff_mid=diff_mid,
                           result_trap=trapezoidal_result, diff_trap=diff_trap,
                           result_simp=simpson_result, diff_simp=diff_simp)

def midpoint(n):
    midpoint_result = 0
    a = 0
    b = 0.5
    while b <= 5000:
        midpoint = float((b - a) * (borwein_calc(n, ((a + b) / 2))))
        midpoint_result += midpoint
        a = a + 0.5
        b = b + 0.5
    diff_mid = pi_difference(midpoint_result)
    return "{:.10f}".format(midpoint_result), "{:.10f}".format(diff_mid)

def trapezoidal(n) -> float:
    trapezoidal_result = 0
    a = 0
    b = 0.5
    while b <= 5000:
        trapezoidal = float(((b - a) / 2) * (borwein_calc(n, a) + borwein_calc(n, b)))
        trapezoidal_result += trapezoidal
        a = a + 0.5
        b = b + 0.5
    diff_trap = pi_difference(trapezoidal_result)
    return "{:.10f}".format(trapezoidal_result), "{:.10f}".format(diff_trap)

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
    diff_simp = pi_difference(simpson_result)
    return "{:.10f}".format(simpson_result), "{:.10f}".format(diff_simp)

if __name__ == '__main__':
    app.run(debug=True)