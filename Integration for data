# INTEGRATION FOR  DATA --------

def integrate_points(x, y):
   
    # Check inputs have same number of points
    if len(x) != len(y):
        print("Error: x and y must have the same length.")
        return None
    
    # Need at least two points to form one trapezoid
    if len(x) < 2:
        print("Error: At least two points are required.")
        return None
    
    total_area = 0.0
    
    # Loop over each adjacent pair of points
    for i in range(len(x) - 1):
        dx = x[i+1] - x[i]                # width of this slice
        avg_height = (y[i] + y[i+1]) / 2  # average of the two y-values
        slice_area = avg_height * dx      # area of trapezoid
        total_area = total_area + slice_area
    
    return total_area

time = [0,5,12,20,28,35,45,55,65]
temp = [50,40,32,25,20,16,13,11,10]
integrate_points(time,temp)
