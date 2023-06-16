import pandas as pd # For reading and manipulating 2D data (like spreadsheets)
import numpy as np # For doing numerical calculations (literally NUMerical PYthon)
import matplotlib.pyplot as plt # For making graphs
from IPython.display import display

# url = 'https://raw.githubusercontent.com/janzika/MATH3041/main/data/climate-change_2.csv'
data_ph = pd.read_csv("data\ph.csv")
# display(data)

# run the following bash script to get scraped data that we need for ph
# grep -E 'World' climate-change_2.csv | cut -f1,2,10,11 -d',' | sed -E '/,$/d' > ph.csv

# The row values where the entity is World
row_values_ph = np.where(data_ph['Entity']=='World')[0]

# total palm oil production for the world 
world_ph_monthly=data_ph['Monthly pH measurement'][row_values_ph[0]:row_values_ph[-1]]
world_ph_annual=data_ph['Annual average'][row_values_ph[0]:row_values_ph[-1]]
dates_ph=data_ph['Date'][row_values_ph[0]:row_values_ph[-1]] # associated years
print(dates_ph[0])

url = 'https://raw.githubusercontent.com/janzika/MATH3041/main/data/annual-co-emissions-by-region.csv'
data_emissions = pd.read_csv(url)

# The row values where the entity is World
row_values_emissions = np.where(data_emissions['Entity']=='World')[0]

# annual CO2 emmsions (billion tonnes) for each country from 1750 to 2021
world_emissions=data_emissions['Annual CO₂ emissions (zero filled)'][row_values_emissions[0]:row_values_emissions[-1]]
years_emissions=data_emissions['Year'][row_values_emissions[0]:row_values_emissions[-1]] # associated years


# plot palm oil produciton data 
plt.subplot(1,2,1)
plt.plot(dates_ph,world_ph_monthly) 
plt.plot(dates_ph,world_ph_annual)
plt.legend(['Monthly average','Annual average'])
# define axis labels and title
plt.xlabel('Dates')
plt.ylabel('Ocean pH levels')
plt.title('ph measurement')

# plot palm oil produciton data 
plt.subplot(1,2,2)
plt.plot(years_emissions,world_emissions) 
# define axis labels and title
plt.xlabel('Year')
plt.ylabel('CO2 emmsions (billion tonnes)')
plt.title('Annual CO2 emissions')
plt.show()