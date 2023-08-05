import pandas as pd # For reading and manipulating 2D data (like spreadsheets)
import numpy as np # For doing numerical calculations (literally NUMerical PYthon)
import matplotlib.pyplot as plt # For making graphs
from datetime import datetime as dt
import time

def toYearFraction(date):
    def sinceEpoch(date): # returns seconds since epoch
        return time.mktime(date.timetuple())
    s = sinceEpoch

    year = date.year
    startOfThisYear = dt(year=year, month=1, day=1)
    startOfNextYear = dt(year=year+1, month=1, day=1)

    yearElapsed = s(date) - s(startOfThisYear)
    yearDuration = s(startOfNextYear) - s(startOfThisYear)
    fraction = yearElapsed/yearDuration

    return date.year + fraction

# Computing X and Y
def linear_fit(xx,yy):
    X = xx
    Y = yy

    # Total number of values
    n = len(X) 

    numer = n*sum(X*Y) - sum(X)*sum(Y)
    denom = n*sum(X**2) - sum(X)**2

    m = numer/denom

    b = (sum(Y)- m*sum(X))/n

    return(m, b) # return coefficents

# Calculating R2 coefficient
def r_squared(xx,yy,m,c):
    X = xx.values
    Y = yy.values
    # Mean X and Y
    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    # Total number of values
    n = len(X)

    ss_tot=0
    ss_res=0

    for i in range(n):
        y_pred = c + m * X[i]
        ss_tot += (Y[i] - mean_y) ** 2
        ss_res += (Y[i] - y_pred) ** 2
        r2 = 1 - (ss_res/ss_tot)
    return(r2)
x = np.linspace(1, 4, 4)
y_plots = np.array([10, 9, 5.5, 2.5])
Y_plots = np.log(y_plots)
m, b = linear_fit(x, Y_plots)
print(f"y = {m}x + {b}")
y_cal = m*x + b

plt.figure("Test")
plt.scatter(x, Y_plots, color='r')
plt.plot(x, y_cal)
plt.title('Test')
plt.xlabel('Years')
plt.ylabel('log Production (log(Tonnes))')
plt.show()
