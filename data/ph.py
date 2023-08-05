#!/usr/bin/env python3

# import packages
import pandas as pd # For reading and manipulating 2D data (like spreadsheets)
import numpy as np # For doing numerical calculations (literally NUMerical PYthon)
import matplotlib.pyplot as plt # For making graphs
from sklearn.metrics import r2_score

url_ph = 'https://raw.githubusercontent.com/janzika/MATH3041/main/data/climate-change_2.csv'
ph_data = pd.read_csv(url_ph)

url_co2 = 'https://raw.githubusercontent.com/janzika/MATH3041/main/data/annual-co-emissions-by-region.csv'
co2_data = pd.read_csv(url_co2)


#
ph_filtered_data = ph_data[(ph_data['Entity'] == 'World') & (ph_data['Annual average'].notna())][['Entity', 'Date', 'Monthly pH measurement', 'Annual average']]
co_filtered_data = co2_data[(co2_data['Entity'] == 'World') & (co2_data['Year'] >= 1880)]

#
ph_filtered_data['Date'] = pd.to_datetime(ph_filtered_data['Date'])
average_data = ph_filtered_data.groupby(ph_filtered_data['Date'].dt.year)[['Monthly pH measurement', 'Annual average']].mean()
average_data = average_data.reset_index()


# rate of change
average_data.set_index('Date', inplace=True)
average_data['Rate of change'] = average_data['Annual average'].diff()
average_data.reset_index(inplace=True)

# Merge average_data and co_filtered_data based on the 'Date' column
co_filtered_data.rename(columns={'Year' : 'Date'}, inplace=True)
merged_data = pd.merge(average_data, co_filtered_data, on='Date')

# Create a new column with the cumulative sum
merged_data['Cumulative co2 emissions'] = merged_data['Annual CO₂ emissions (zero filled)'].cumsum()

plt.plot(merged_data['Cumulative co2 emissions'], merged_data['Annual average'], 'ro', markersize=3, label='Data Points')
plt.xlabel('Cumulative CO₂ emissions (billion tonnes)')
plt.ylabel('Ocean pH')
plt.title('Relation between Cumulative CO₂ Emissions and Ocean Acidification')

x = merged_data['Cumulative co2 emissions']
y = merged_data['Annual average']
coefficients = np.polyfit(x, y, 1)
poly_eq = np.poly1d(coefficients)
# plt.plot(x, poly_eq(x))

x_fit = np.linspace(min(x), max(x) + 4300000000000, 100)  # Extend the range of 'x' for projections
plt.plot(x_fit, (poly_eq(x_fit)))

print(f'R2 score = {r2_score(merged_data["Annual average"], poly_eq(x))}') # 0.960251108751908

slope = coefficients[0]
intercept = coefficients[1]
print('slope: ', slope, 'intercept: ', intercept) # slope:  -5.944232904257503e-14 intercept:  8.11200305841759

plt.show()