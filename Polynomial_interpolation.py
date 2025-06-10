# POLYNOMIAL INTERPOLATION FOR EXPERIMENTAL DATA POINTS -----------------

import numpy as np

def polynomial_interpolate(x, y, degree, x0):
   
    # Fit polynomial coefficients [c0, c1, ..., c_degree]
    coeffs = np.polyfit(x, y, degree)
    # Evaluate the polynomial at x0
    y0 = np.polyval(coeffs, x0)
    return y0

polynomial_interpolate([5,6,7],[171,283,435], 2, 6.5)      #(x, y, degree, x0)
