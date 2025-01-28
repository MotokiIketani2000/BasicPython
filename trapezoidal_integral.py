from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math

def trapezoidal_integral():
    a = 0
    b = math.pi / 2
    n = 100
    
    h = (b - a) / n
    
    total = sin(a) + sin(b)
    
    for i in range(1, n):
        x = a + i * h
        total += 2 * sin(x)
    
    result = total * h / 2
    return result
integral_value = trapezoidal_integral()
print(f"台形積分による近似値: {integral_value}")