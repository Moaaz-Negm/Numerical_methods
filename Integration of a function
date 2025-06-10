# INTEGRATION FOR A FUNCTION ---------------------------------

def f(x):
    # Define your function here. Example:
    return 3*x**2+x+5 # define your own function

def integrate(a,b,h):
   
    
    # Compute how many full subintervals fit
    n = int((b - a) / h)
    
    # Left Riemann sum
    left_sum = sum(f(a + i*h) for i in range(n)) * h
    # Right Riemann sum
    right_sum = sum(f(a + i*h) for i in range(1, n+1)) * h
    
    # Determine over- and underestimations
    over = max(left_sum, right_sum)
    under = min(left_sum, right_sum)
    avg = (over + under) / 2  # Trapezoidal approximation

    print(f"Overestimation:   {over}")
    print(f"Underestimation:  {under}")
    print(f"Average (trap.):  {avg}")
    
integrate(15, 20, 0.2)
