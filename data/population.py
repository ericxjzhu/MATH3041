import pandas as pd # For reading and manipulating 2D data (like spreadsheets)
import numpy as np # For doing numerical calculations (literally NUMerical PYthon)
import matplotlib.pyplot as plt # For making graphs

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
population = data['Population'][row[0]:row[-1]]

m2, b2 = linear_fit(years, population)
print("UN High Projection Scenario")
print(f"y = {m2}x + {b2}") # y = 84590486.78003466x + -162930039046.18018
y_cal2 = m2*years + b2

r2 = r_squared(years,population,m2,b2) # 0.9990243646492619
print(r2)

plt.figure("Population UN High Projection Scenario")
plt.scatter(years, population, color='g', s=4)
plt.plot(years, y_cal2)
plt.title('Population')
plt.xlabel('Years')
plt.ylabel('Population')
plt.show()
