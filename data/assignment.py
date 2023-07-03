import pandas as pd # For reading and manipulating 2D data (like spreadsheets)
import numpy as np # For doing numerical calculations (literally NUMerical PYthon)
import matplotlib.pyplot as plt # For making graphs
from IPython.display import display
from datetime import datetime as dt
import time

def toYearFraction(date):
    def sinceEpoch(date): # returns seconds since epoch
        return time.mktime(date.timetuple())
    s = sinceEpoch

    year = date.year
    startOfThisYear = dt(year=year, month=1, day=1)
    startOfNextYear = dt(year=year+1, month=1, day=1)

    yearElapsed = s(date) - s(startOfThisYear)
    yearDuration = s(startOfNextYear) - s(startOfThisYear)
    fraction = yearElapsed/yearDuration

    return date.year + fraction

# Coomputing X and Y
def linear_fit(xx,yy):
    X = xx.values
    Y = yy.values

    # Total number of values
    n = len(X) 

    numer = n*sum(X*Y) - sum(X)*sum(Y)
    denom = n*sum(X**2) - sum(X)**2

    m = numer/denom

    b = (sum(Y)- m*sum(X))/n

    return(m, b) # return coefficents

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

# run the following bash script on the file climate-change_2.csv to get scraped data that we need for ph
# grep -E 'World' climate-change_2.csv | cut -f1,2,10,11 -d',' | sed -E '/,$/d' > ph.csv

data_ph = pd.read_csv("data/ph.csv")

# The row values where the entity is World
row_values_ph = np.where(data_ph['Entity']=='World')[0]
world_ph_annual=data_ph['Annual average'][row_values_ph[0]:row_values_ph[-1]]
years_ph=data_ph['Date'][row_values_ph[0]:row_values_ph[-1]] # associated dates
for index, value in enumerate(years_ph):
    years_ph[index] = toYearFraction(dt.strptime(value, '%Y-%m-%d').date())

url = 'https://raw.githubusercontent.com/janzika/MATH3041/main/data/annual-co-emissions-by-region.csv'
data_emissions = pd.read_csv(url)

row_values_emissions = np.where((data_emissions['Entity']=='World'))[0]

# annual CO2 emmsions (billion tonnes) for each country from 1750 to 2021
world_emissions=data_emissions['Annual CO₂ emissions (zero filled)'][row_values_emissions[0]:row_values_emissions[-1]]
years_emissions=data_emissions['Year'][row_values_emissions[0]:row_values_emissions[-1]] # associated years

# Plot both graphs separatley
# plot ocaen pH graph
plt.figure("Separate Graphs")
plt.subplot(1,2,1)
xval = np.linspace(1988,2030,1000)
# row_values_emissions_comparison = np.where((data_emissions['Entity']=='World'))[0]
row_values_emissions_comparison = np.where((data_emissions['Entity']=='World') & (data_emissions['Year']>=1988))[0] # shorten years as pH mesurement only starts in 1988
world_emissions_comparison=data_emissions['Annual CO₂ emissions (zero filled)'][row_values_emissions_comparison[0]:row_values_emissions_comparison[-1]]
years_emissions_comparison=data_emissions['Year'][row_values_emissions_comparison[0]:row_values_emissions_comparison[-1]] # associated years


# Determine constants for Annual ph
m_world_ph,b_world_ph = linear_fit(years_ph,world_ph_annual)
yval_world_ph = m_world_ph*xval + b_world_ph # find y values 

# define figure size
plt.scatter(years_ph,world_ph_annual,color='r',s=12)
plt.plot(xval,yval_world_ph)
plt.title('Annual World ph')
plt.legend(['Actual','Predicted'])
plt.xlabel('Years')
plt.ylabel('Ocean pH levels')

# Plot CO2 emissions graph
plt.subplot(1,2,2)
plt.plot(years_emissions,world_emissions,color='b',label='C02 emissions') 
plt.xlabel('Year')
plt.ylabel('CO2 emissions (Tonnes)')
plt.title('Annual CO2 emissions')

#########################################################################################

print('Annual ph world')
print(r_squared(years_ph,world_ph_annual,m_world_ph,b_world_ph))
# Annual ph world
# 0.950557992515578

plt.show()
