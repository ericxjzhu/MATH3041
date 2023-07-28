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

plt.figure("Population log UN High Projection Scenario")
plt.scatter(years, log_population, color='r')
plt.plot(years, y_cal1)
plt.title('Population log')
plt.xlabel('Years')
plt.ylabel('log Population')

plt.figure("Population UN High Projection Scenario")
plt.scatter(years, population, color='g')
plt.plot(years, y_cal2)
plt.title('Population')
plt.xlabel('Years')
plt.ylabel('Population')
plt.show()
# plt.figure("Population")
# plt.plot(years, population)
# plt.title("Population growth based on high UN projections")
# plt.show()
