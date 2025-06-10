# BISECTION METHOD FOR ROOT FINDING
import numpy as np

def f(x):
    return 5*x**2-95
  # define the function or the equation

def bisection_method(a, b, tolerance): # inputs take the ends of the
                                    #range a=left end, b=right end, tolerance is the telling the function to stop when the difference is something
    
    if f(a) * f(b) >= 0:
        print("Invalid interval: No sign change")
        return None

    while (b - a) / 2 > tolerance:
        m = (a + b) / 2
        if f(m) == 0:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2

# use

root = bisection_method(0, 3.5, 0.01)
print("Root found at:", root)
