# LINEAR INTERPOLATION FOR EXPERIMENTAL DATA ----------------------------


def linear_interpolate(x, y, x0):
    
    # Basic input checks
    
    if len(x) != len(y):
        print("Error: x and y must have the same number of points.")
        return None
    
    if len(x) < 2:
        print("Error: At least two points are required for interpolation.")
        return None
    
    # Check bounds
    if x0 < x[0] or x0 > x[-1]:
        print("Error: x0 is outside the range of x.")
        return None

    # Find the interval [x[i], x[i+1]] that contains x0
    for i in range(len(x) - 1):
        x_left = x[i]
        x_right = x[i+1]
        if x0 >= x_left and x0 <= x_right:
            y_left = y[i]
            y_right = y[i+1]
            
            # Compute fraction along the interval
            t = (x0 - x_left) / (x_right - x_left)
            
            # Linear interpolation formula
            y0 = y_left + t * (y_right - y_left)
            
            return y0

    # Should never reach here if x0 is in bounds
    return None


linear_interpolate([2.2,3.8], [5.8,6.7] , 2.5)  # ([x1,x2], [y1,y2] , x?)
