import pandas as pd #per importare i dataset
from matplotlib import pyplot as plt #per importare pyplot è possibile utilizzare anche %matplotlib inline
import seaborn as sns #importare seaborn

"""

a) the details for first, last and 10th entry, 32/34/36
b) the details for each day, 26
c) entries when total distance travelled in a day is greater than 90 but less than 100,
d) the distance and fuel economy for a single row from c),
e) entries for Fridays when the average moving speed is greater than 90,
f) entries when max speed is greater than 135 or fuel economy is less than 8, and
g) details for the entries by day of week.

"""


travel_df = pd.read_csv('travel-times.csv')

# print(travel_df.head()) 
# print(travel_df.describe())
# print(travel_df.info())
travel_df.drop(labels=("Comments"), axis=1, inplace=True)
#print(travel_df.head())

#print(travel_df.info())

travel_df['FuelEconomy'] = pd.to_numeric(travel_df['FuelEconomy'], errors="coerce")
travel_df['FuelEconomy'].fillna(travel_df['FuelEconomy'].mean(), inplace=True)

#print(travel_df.head())

travel_df_groupbydate = travel_df.groupby(['Date', 'DayOfWeek'])
travel_df_sum = travel_df_groupbydate.sum()
travel_df_sum['MaxSpeed'] = travel_df_groupbydate['MaxSpeed'].max()
travel_df_sum['AvgSpeed'] = travel_df_groupbydate['AvgSpeed'].mean()
travel_df_sum['AvgMovingSpeed'] = travel_df_groupbydate['AvgMovingSpeed'].mean()
travel_df_sum['FuelEconomy'] = travel_df_groupbydate['FuelEconomy'].mean()
#print(travel_df_sum.head)

#print(travel_df_sum['Distance'])

travel_df_sum.reset_index(inplace=True)

#print(travel_df_sum.tail())

# print(travel_df_sum.iloc[0])

# print(travel_df_sum.iloc[-1])

# print(travel_df_sum.iloc[9])

#travel_df_sum.info()

#print(travel_df_sum.dtypes)

distance_above_ninety = travel_df_sum['Distance'] > 90
distance_under_hundred = travel_df_sum['Distance'] < 100
ninety_to_hundred = travel_df_sum[distance_above_ninety & distance_under_hundred]
#print(ninety_to_hundred)

lastdate = ninety_to_hundred.iloc[-1]
#print(lastdate.loc[['Distance', 'FuelEconomy']])

onfriday = travel_df_sum['DayOfWeek'] == 'Friday'
overninety = travel_df_sum['AvgSpeed'] > 90
overninety_friday = travel_df_sum[onfriday & onfriday & overninety]
#print(overninety_friday)


speedover = travel_df_sum['MaxSpeed'] > 135
fuelless = travel_df_sum['FuelEconomy'] < 8
fuelandspeed = travel_df_sum[speedover | fuelless]
#print(fuelandspeed)

# print(travel_df_sum.groupby(['DayOfWeek']).max())
# print(travel_df_sum.groupby(['DayOfWeek'])['FuelEconomy'].describe())



