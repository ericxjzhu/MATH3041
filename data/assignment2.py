import pandas as pd # For reading and manipulating 2D data (like spreadsheets)
import numpy as np # For doing numerical calculations (literally NUMerical PYthon)
import matplotlib.pyplot as plt # For making graphs
from pprint import pprint

data_gdp = pd.read_csv("data/world-gdp.csv")
data_gdp_capita = pd.read_csv("data/world-gdp-per-capita-1900.csv")
data_co = pd.read_csv("data/world-co2-emissions.csv")

row_gdp = np.where(data_gdp['Entity']=='World')[0]
years_gdp = data_gdp['Year'][row_gdp[0]:row_gdp[-1]]
data = dict()
ratio = []
for year in years_gdp:
    gdp_row = np.where(data_gdp['Year']==year)[0]
    co2_row = np.where(data_co['Year']==year)[0]
    gdp = data_gdp['World GDP in 2011 Int.$ (OWID based on World Bank & Maddison (2017))'][gdp_row[0]]
    co2 = data_co['Annual CO2 emissions (zero filled)'][co2_row[0]]
    ratio.append(co2/gdp)
    data[year] = co2/gdp
pprint(data)

row_gdp_capita = np.where(data_gdp_capita['Entity']=='World')[0]
years_gdp_capita = data_gdp_capita['Year'][row_gdp_capita[0]:row_gdp_capita[-1]]

ratio_capita = []
for year in years_gdp_capita:
    gdp_row = np.where(data_gdp_capita['Year']==year)[0]
    co2_row = np.where(data_co['Year']==year)[0]
    gdp = data_gdp_capita['GDP per capita'][gdp_row[0]]
    co2 = data_co['Annual CO2 emissions (zero filled)'][co2_row[0]]
    ratio_capita.append(co2/gdp)

plt.figure("Ratio of emissions over gdp")
plt.plot(years_gdp, ratio)
plt.title('Ratio of emissions over gdp of the world')

plt.figure("Ratio of emissions over gdp per capita")
plt.plot(years_gdp_capita, ratio_capita)
plt.title('Ratio of emissions over gdp per capita of the world')
plt.show()
