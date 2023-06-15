# import packages
import pandas as pd # For reading and manipulating 2D data (like spreadsheets)
import numpy as np # For doing numerical calculations (literally NUMerical PYthon)
import matplotlib.pyplot as plt # For making graphs
from IPython.display import display

url_palm = 'https://raw.githubusercontent.com/janzika/MATH3041/main/data/palm-oil-production.csv'
PO_data = pd.read_csv(url_palm)
# display(PO_data)

# The row values where the entity is World
row_values = np.where(PO_data['Entity']=='World')[0]

# total palm oil production for the world 
PO_world=PO_data['Palm oil | 00000257 || Production | 005510 || tonnes'][row_values[0]:row_values[-1]]
years = PO_data['months'][row_values[0]:row_values[-1]] # associated years

# # plot palm oil produciton data 
# plt.plot(years,PO_world) 
# # define axis labels and title
# plt.xlabel('Year')
# plt.ylabel('Production (Tonnes)')
# plt.title('Total Palm Oil Production')
#plt.show()

# palm oil production in Malaysia
Mal_rowval = np.where(PO_data['Entity']=='Malaysia')[0] # find all the row values where country is Malayasia 

# Get years and data for palm oil production using Mal_rowvals
PO_malaysia=[ PO_data['Year'][Mal_rowval[0]:Mal_rowval[-1]],PO_data['Palm oil | 00000257 || Production | 005510 || tonnes'][Mal_rowval[0]:Mal_rowval[-1]]]

# repeat with Indonesia 
Indo_rowval = np.where(PO_data['Entity']=='Indonesia')[0]
PO_indonesia=[ PO_data['Year'][Indo_rowval[0]:Indo_rowval[-1]],PO_data['Palm oil | 00000257 || Production | 005510 || tonnes'][Indo_rowval[0]:Indo_rowval[-1]]]

# plot values 
plt.plot(PO_malaysia[0],PO_malaysia[1])
plt.plot(PO_indonesia[0],PO_indonesia[1])
plt.plot(years,PO_world)

# axis and title labels 
plt.xlabel('Years')
plt.ylabel('Production (Tonnes)')
plt.title('Palm Oil Production')
plt.legend(['Malaysia','Indonesia','World'])
plt.show()