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

# Coomputing X and Y
def linear_fit(xx,yy):
    X = xx.values
    Y = yy.values

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

data_gdp = pd.read_csv("data/world-gdp-per-capita-1900.csv")
data_co = pd.read_csv("data/world-co2-emissions-1900.csv")

row_gdp = np.where(data_gdp['Entity']=='World')[0]
years_gdp = data_gdp['Year'][row_gdp[0]:row_gdp[-1]]

ratio = []
for year in years_gdp:
    gdp_row = np.where(data_gdp['Year']==year)[0]
    co2_row = np.where(data_co['Year']==year)[0]
    gdp = data_gdp['GDP per capita'][gdp_row[0]]
    co2 = data_co['Annual CO2 emissions (zero filled)'][co2_row[0]]
    ratio.append(co2/gdp)


print(years_gdp, ratio)
plt.figure("Ratio of emissions over gdp per capita")
plt.plot(years_gdp, ratio)
plt.show()

