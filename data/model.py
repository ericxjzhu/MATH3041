import pandas as pd # For reading and manipulating 2D data (like spreadsheets)
import numpy as np # For doing numerical calculations (literally NUMerical PYthon)
import matplotlib.pyplot as plt # For making graphs
from pprint import pprint
from sklearn.metrics import r2_score


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

data = pd.read_csv("data/output.csv")

years = data['Date']
co2 = data['Cumulative co2 emissions']

goals = {
    'Goal 1': {
        'L': 6.201 * (10**12),
        'a': -0.0339,
        't0': 2043.01,
    },
    'Goal 2': {
        'L': 3.361 * (10**12),
        'a': -0.0420,
        't0': 2018.81,
    },
    'Goal 3': {
        'L': 1.955 * (10**12),
        'a': -0.0500,
        't0': 1995.95,
    },
}

r2_emissions = []
years_projection = np.linspace(1880,2100,1000)
co2_projection = []

for name, goal in goals.items():
    r2_emissions.append(goal['L'] / (1 + np.exp(goal['a'] * (years - goal['t0']))))
    co2_projection.append(goal['L'] / (1 + np.exp(goal['a'] * (years_projection - goal['t0']))))


for i in range(len(co2_projection)):
    plt.figure(f'Goal {i + 1} Model')
    plt.scatter(years, co2, color='black')
    plt.plot(years_projection, co2_projection[i])
    plt.title(f'Goal {i + 1} Model')
    plt.xlabel('Years')
    plt.ylabel('Cumulative CO2 Emissions')
    print(f'R2 score = {r2_score(co2, r2_emissions[i])}')

plt.show()