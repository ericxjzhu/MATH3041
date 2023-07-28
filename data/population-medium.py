import pandas as pd # For reading and manipulating 2D data (like spreadsheets)
import numpy as np # For doing numerical calculations (literally NUMerical PYthon)
import matplotlib.pyplot as plt # For making graphs
from pprint import pprint

data = pd.read_csv("data/population-medium.csv")

row = np.where(data['Country name'] == 'World')[0]
years = data['Year'][row[0]:row[-1]]
years.add(data['Year'][row[-1]])
population = data['Population'][row[0]:row[-1]]
years.add(data['Population'][row[-1]])

plt.figure("Population")
plt.plot(years, population)
plt.title("Population growth based on medium UN projections")
plt.show()
