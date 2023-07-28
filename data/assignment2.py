import pandas as pd # For reading and manipulating 2D data (like spreadsheets)
import numpy as np # For doing numerical calculations (literally NUMerical PYthon)
import matplotlib.pyplot as plt # For making graphs

data_gdp = pd.read_csv("data/world-gdp-per-capita-1900.csv")
data_co = pd.read_csv("data/world-co2-emissions-1900.csv")

row_gdp = np.where(data_gdp['Entity']=='World')[0]
years_gdp = data_gdp['Year'][row_gdp[0]:row_gdp[-1]]

ratio = []
for year in years_gdp:
    gdp_row = np.where(data_gdp['Year']==year)[0]
    co2_row = np.where(data_co['Year']==year)[0]
    gdp = data_gdp['GDP per capita'][gdp_row[0]]
    co2 = data_co['Annual CO2 emissions (zero filled)'][co2_row[0]]
    ratio.append(co2/gdp)


print(years_gdp, ratio)
plt.figure("Ratio of emissions over gdp per capita")
plt.plot(years_gdp, ratio)
plt.title('Ratio of emissions over gdp per capita of the world')
plt.show()
