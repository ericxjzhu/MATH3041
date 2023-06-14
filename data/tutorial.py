# import packages
import pandas as pd # For reading and manipulating 2D data (like spreadsheets)
import numpy as np # For doing numerical calculations (literally NUMerical PYthon)
import matplotlib.pyplot as plt # For making graphs
from IPython.display import display


# creates a 1D array of 5 values between 0 and 1
# x = np.linspace(0,1,5)
# print(x.shape) # shape of array x

# 2D coordinate arrays on a 5x5 grid
# xx ,yy= np.meshgrid(x,x,indexing='ij')
# print(xx)


url_palm = 'https://raw.githubusercontent.com/janzika/MATH3041/main/data/palm-oil-production.csv'
PO_data = pd.read_csv(url_palm)
# display(PO_data)

# The row values where the entity is World
row_values = np.where(PO_data['Entity']=='World')[0]

# total palm oil production for the world 
PO_world=PO_data['Palm oil | 00000257 || Production | 005510 || tonnes'][row_values[0]:row_values[-1]]
years = PO_data['Year'][row_values[0]:row_values[-1]] # associated years

# plot palm oil produciton data 
plt.plot(years,PO_world) 
# define axis labels and title
plt.xlabel('Year')
plt.ylabel('Production (Tonnes)')
plt.title('Total Palm Oil Production')
plt.show()