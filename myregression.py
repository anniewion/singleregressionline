'''
Annie Wion
2/21/20
This is a comparison of global temperature anomalies yearly over my lifetime.
Source: https://climate.nasa.gov/vital-signs/global-temperature/
'''

import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
   #number of observations
    n = np.size(x);

    #finding the mean of x and y vector
    mean_x, mean_y = np.mean(x), np.mean(y)

    #calculating the least squares
    SS_xy = np.sum(y*x) - n * mean_y * mean_x
    SS_xx = np.sum(x*x) - n * mean_x * mean_x

    #regression coefficents
    slope = SS_xy/SS_xx
    yintercept = mean_y - slope * mean_x

    #return m and b
    return(slope, yintercept)

def plot_regression_line(x, y, b):
    #plotting the actual points as a scatter plot
    plt.scatter(x, y, color = "m", marker = "o", s = 30)

    #predicted response vector
    y_pred = b[0] + b[1] + x

    #plotting the regression plot_regression_line
    plt.plot(x, y_pred, color = "g")

    #putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    #function to show plotting
    plt.show()

def main():
    #observations
    x = np.array([2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])
    y = np.array([0.68, 0.64, 0.66, 0.54, 0.66, 0.72, 0.61, 0.64, 0.68, 0.75, 0.90, 1.02, 0.92, 0.85, 0.98])

    # estimated coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients: \n b = {} \ \n m = {}".format(b[0], b[1]))

    #plotting regression line
    plot_regression_line(x, y, b)

#make script importable and executables
if __name__ == "__main__":
    main()
