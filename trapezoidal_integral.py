from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math

def trapezoidal_integral_math(f, a=0, b=1, n=100):
    h = (b - a) / n 
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n): 
        integral += f(a + i * h)
    return integral * h
    

print(trapezoidal_integral_math(math.sin, 0, math.pi / 2, 50))

print(trapezoidal_integral_math(lambda x: 4 / (1 + x**2), 0, 1, 100))

print(trapezoidal_integral_math( lambda x: math.sqrt(math.pi) * math.exp(-x**2), -100, 100, 1000))

        