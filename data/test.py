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
years_ph=data_ph['Date'][row_values_ph[0]:row_values_ph[-1]] # associated dates
years_ph.replace(to_replace = '1988-10-31', value = '1988')
for index, value in enumerate(years_ph):
    years_ph[index] = toYearFraction(dt.strptime(value, '%Y-%m-%d').date())

url = 'https://raw.githubusercontent.com/janzika/MATH3041/main/data/annual-co-emissions-by-region.csv'
data_emissions = pd.read_csv(url)

# The row values where the entity is World
row_values_emissions = np.where((data_emissions['Entity']=='World') & (data_emissions['Year']>=1988))[0]

# annual CO2 emmsions (billion tonnes) for each country from 1750 to 2021
world_emissions=data_emissions['Annual CO₂ emissions (zero filled)'][row_values_emissions[0]:row_values_emissions[-1]]
years_emissions=data_emissions['Year'][row_values_emissions[0]:row_values_emissions[-1]] # associated years

# Plot both graphs separatley
# plot palm oil produciton data
plt.figure("Separate Graphs")
plt.subplot(1,3,1)
# plt.plot(years_ph,world_ph_monthly) 
plt.plot(years_ph,world_ph_annual,color='g',label='Ocean pH')
# plt.legend(['Monthly average','Annual average'])
plt.xlabel('Year')
plt.ylabel('Ocean pH levels')
plt.title('Annual pH measurement')

# plot palm oil produciton data log
plt.subplot(1,3,2)
plt.semilogy(years_emissions,world_emissions,color='b',label='C02 emissions') 
# define axis labels and title
plt.xlabel('Year')
plt.ylabel('log CO2 emmsions (log(Tonnes))')
plt.grid()
plt.title('Annual CO2 emissions')

plt.subplot(1,3,3)
plt.plot(years_emissions,world_emissions,color='y',label='C02 emissions') 
# define axis labels and title
plt.xlabel('Year')
plt.ylabel('CO2 emmsions (billion tonnes)')
plt.title('Annual CO2 emissions')

plt.show()

#########################################################################################

xval = np.linspace(1988,2030,1000) # define  values from 1960 to 2030

# Determine constants for Annual ph
m_world_ph,b_world_ph = linear_fit(years_ph,world_ph_annual)
yval_world_ph = m_world_ph*xval + b_world_ph # find y values 

# define figure size
plt.figure("Line of best fit")

plt.subplot(1,2,1)
plt.scatter(years_ph,world_ph_annual,color='r',s=12)
plt.plot(xval,yval_world_ph)
plt.title('Annual World ph')
plt.legend(['Actual','Predicted'])
plt.xlabel('Years')
plt.ylabel('Ocean pH levels')

# Determine constants for CO2 production
m_world_emissions,b_world_emissions = linear_fit(years_emissions,world_emissions)
yval_world_emissions = m_world_emissions*xval + b_world_emissions # find y values 

plt.subplot(1,2,2)
plt.scatter(years_emissions,world_emissions,color='r',s=12)
plt.plot(xval,yval_world_emissions)
plt.title('Annual CO2 emissions')
plt.legend(['Actual','Predicted'])
plt.xlabel('Years')
plt.ylabel('log CO2 emmsions (log(Tonnes))')

#########################################################################################

print('Annual ph world')
print(r_squared(years_ph,world_ph_annual,m_world_ph,b_world_ph))
print('CO2 world')
print(r_squared(years_emissions,world_emissions,m_world_emissions,b_world_emissions))
# Annual ph world
# 0.950557992515578
# CO2 world
# 0.9542271797924022

fig, ax = plt.subplots()

# lns1 = ax.plot(years_ph,world_ph_monthly,color='o',label='Monthly world pH') 
lns2 = ax.plot(years_ph,world_ph_annual,color='g',label='Ocean pH')
ax.set_ylabel('Ocean pH levels')
ax.set_xlabel('Year')

# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
lns3=plt.semilogy(years_emissions,world_emissions,color='b',label='C02 emissions') 

# ax2.set_ylim([0,2.5e7])
ax2.set_ylabel('log CO2 emmsions (log(Tonnes))')

# added these three lines
# lns = lns1+lns3+lns2
# labs = [l.get_label() for l in lns]
# ax.legend(lns, labs, loc=0)
fig.legend(['Monthly world pH','Annual world pH','World CO2 concentration'],loc='upper left')

# plt.show()