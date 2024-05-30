# Nikisha_Shrestha_2408239 
import numpy as np
import matplotlib.pyplot as plt

def plot_function(func, a, b):
    """
    This function plot the graph of the input func 
    within the given interval [a,b).
    """
    # Your code goes here
    x = np.linspace(a, b, 1000)
    y = func(x)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of the Function using MidpointApproxMethod')
    plt.grid(True)
    plt.show()

def midpoint_approx(func, a, b, N):
    '''Compute the Midpoint Approximation of Definite Integral of a function over the interval [a,b].

    Parameters
    ----------
    func : function
           Vectorized function of one variable
    a , b : numbers
        Endpoints of the interval [a,b]
    N : integer
        Number of subintervals of equal length in the partition of [a,b]

    Returns
    -------
    float
        Approximation of the definite integral by Midpoint Approximation.
    '''

    # Your code goes here
    h = (b - a) / N
    # initialize the result
    result = 0
    # loop through each subinterval
    for i in range(N):
        # calculate the midpoint of the current subinterval
        x_mid = a + (i + 0.5) * h
        # add the area of the rectangle to the result
        result += func(x_mid) * h
    return result

if __name__ == "__main__":
    # 1st Function to be integrated
    func_1 = lambda x : x/(x**2 + 1)
    # Indefinite Integral of the function
    antiderivative_1 = lambda x: 0.5 * np.log(x**2 + 1)# Your code goes here
    
    # 2nd Function to be integrated
    func_2 = lambda x : np.exp(x)
    # Indefinite Integral of the function
    antiderivative_2 = lambda x: np.exp(x)# Your code goes here
    
    # End points for 1st Function
    a1 = 0; b1 = 5;  # Change the values as required
    # End points for 2nd Function
    a2 = 0; b2 = 5;  # Change the values as required

    # Call the function to Plot the graph of the functions
    # Your code goes here
    plot_function(func_1, a1, b1)
    plot_function(func_2, a2, b2)
    
    # Number of partition for 1st Function
    N1 = 1000 # Change the value as required
    # Number of partition for 2nd Function
    N2 = 1000 # Change the value as required

    # Call midpont_method to compute Midpoint Approximation:
    midpoint_approx_1 = midpoint_approx(func_1, a1, b1, 500)# Your code for 1st function
    midpoint_approx_2 = midpoint_approx(func_2, a2, b2, 500)# Your code for 2nd function
    
    # Calculate the true value of the definite integral
    definite_integral_1 = antiderivative_1(b1) - antiderivative_1(a1)  # For 1st Function
    definite_integral_2 = antiderivative_2(b2) - antiderivative_2(a2)  # For 2nd Function

    # Calculate the absolute error between the approximate value and true value
    error_1 = np.abs(midpoint_approx_1 - definite_integral_1)  # For 1st Function
    error_2 = np.abs(midpoint_approx_2 - definite_integral_2)  # For 2nd Function

    print("Subinterval width = {:0.6f}".format((b1-a1)/N1))
    print("Midpoint Approximation for 1st Function = {:0.6f}".format(midpoint_approx_1))
    print("Actual Value for 1st Function = {:0.6f}".format(definite_integral_1))
    print("Absolute error between the above methods ={:0.8f}".format(error_1))

    print("Subinterval width = {:0.6f}".format((b2-a2)/N2))
    print("Midpoint Approximation for 2nd Function = {:0.6f}".format(midpoint_approx_2))
    print("Actual Value for 2nd Function = {:0.6f}".format(definite_integral_2))
    print("Absolute error between the above methods ={:0.8f}".format(error_2))


    