import pandas as pd # For reading and manipulating 2D data (like spreadsheets)
import numpy as np # For doing numerical calculations (literally NUMerical PYthon)
import matplotlib.pyplot as plt # For making graphs
from sklearn.metrics import r2_score

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

alernate = {
    'L': 1.955 * (10**12),
    'a': -0.112,
    't0': 2004,
}

r2_emissions = []
years_projection = np.linspace(1880,2100,1000)
co2_projection = []

for name, goal in goals.items():
    r2_emissions.append(goal['L'] / (1 + np.exp(goal['a'] * (years - goal['t0']))))
    co2_projection.append(goal['L'] / (1 + np.exp(goal['a'] * (years_projection - goal['t0']))))

plt.figure(f'Target Models')
for i in range(len(co2_projection)):
    plt.subplot(1,3,i+1)
    plt.scatter(years, co2, color='red', s=4)
    plt.plot(years_projection, co2_projection[i], color='black')
    plt.title(f'Target {i + 1} Model')
    plt.xlabel('Year')
    plt.ylabel('Cumulative CO2 Emissions (billion tons)')
    print(f'Target {i+1} R2 score = {r2_score(co2, r2_emissions[i])}')

r2_alternate = alernate['L'] / (1 + np.exp(alernate['a'] * (years - alernate['t0'])))
co2_alternate_projection = alernate['L'] / (1 + np.exp(alernate['a'] * (years_projection - alernate['t0'])))
plt.figure(f'Target 3 Alternate Model')
plt.scatter(years, co2, color='red',  s=4)
plt.plot(years_projection, co2_alternate_projection, color='black')
plt.title(f'Target 3 Alternate Model')
plt.xlabel('Year')
plt.ylabel('Cumulative CO2 Emissions (billion tons)')
print(f'Target 3 Alternate R2 score = {r2_score(co2, r2_alternate)}')



plt.show()