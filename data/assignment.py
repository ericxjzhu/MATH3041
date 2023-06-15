import pandas as pd # For reading and manipulating 2D data (like spreadsheets)
import numpy as np # For doing numerical calculations (literally NUMerical PYthon)
import matplotlib.pyplot as plt # For making graphs
from IPython.display import display

url = 'https://raw.githubusercontent.com/janzika/MATH3041/main/data/climate-change_2.csv'
data = pd.read_csv("data\ph.csv")
display(data)

# The row values where the entity is World
row_values = np.where(data['Entity']=='World')[0]

# total palm oil production for the world 
world=data['Monthly pH measurement'][row_values[0]:row_values[-1]]
dates=data['Date'][row_values[0]:row_values[-1]] # associated years


# plot palm oil produciton data 
plt.plot(dates,world) 
# define axis labels and title
plt.xlabel('Dates')
plt.ylabel('Production (Tonnes)')
plt.title('ph measurement')
plt.show()