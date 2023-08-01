import pandas as pd # For reading and manipulating 2D data (like spreadsheets)
import numpy as np # For doing numerical calculations (literally NUMerical PYthon)
import matplotlib.pyplot as plt # For making graphs
from pprint import pprint

# Computing X and Y
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

data = pd.read_csv("data/population-high.csv")

row = np.where(data['Country name'] == 'World')[0]
years = data['Year'][row[0]:row[-1]]
# years.add(data['Year'][row[-1]])
population = data['Population'][row[0]:row[-1]]
# population.add(data['Population'][row[-1]])

log_population = np.log(population)
m1, b1 = linear_fit(years, log_population)
# print(f"y = {m1}x + {b1}")
y_cal1 = m1*years + b1
m2, b2 = linear_fit(years, population)
print("UN High Projection Scenario")
print(f"y = {m2}x + {b2}")
y_cal2 = m2*years + b2

r2 = r_squared(years,population,m2,b2)
print(r2)

plt.figure("Population log UN High Projection Scenario")
plt.scatter(years, log_population, color='r')
plt.plot(years, y_cal1)
plt.title('Population log')
plt.xlabel('Years')
plt.ylabel('log Population')

plt.figure("Population UN High Projection Scenario")
plt.scatter(years, population, color='g', s=4)
plt.plot(years, y_cal2)
plt.title('Population')
plt.xlabel('Years')
plt.ylabel('Population')
plt.show()
# plt.figure("Population")
# plt.plot(years, population)
# plt.title("Population growth based on high UN projections")
# plt.show()
