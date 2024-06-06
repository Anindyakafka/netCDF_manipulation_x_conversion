from netCDF4 import Dataset
import numpy as np
import pandas as pd

# Reading a netCDF file
data = Dataset(r'C:/Users/anind/Downloads/netcdf/TROPESS_reanalysis_mon_co_2021.nc', 'r')

# Storing netCDF latitude and longitude data keys as variables
lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
#print(lat,lon)

#storing the latitude and longitude of India into variables
lat_india = 20.5937
lon_india = 78.9629


#squared latitude and longitude
sq_lat = (lat)**2
sq_lon = (lon)**2
# indentifying the index of the minimum value of latitude and longitude
min_index_lat = sq_lat.argmin()
min_index_lon = sq_lon.argmin()
print(min_index_lat, min_index_lon)




co = data.variables['co']

# Creating an empty pandas dataframe
starting_date = data.variables['time'].units[11:24]
ending_date = data.variables['time'].units[11:15] + '-12-31'
date_range = pd.date_range(start = starting_date, end = ending_date)
df = pd.DataFrame(0, columns = ['carbon'], index = date_range)
print(df)
t = data.variables['time'].size
#print(t)

dt = np.arange(0, t)

time_data = data.variables['time'][:].data
co_data = co[:].data
level = 0
lat_index = min_index_lat
lon_index = min_index_lon

# Extract the data for the selected level, latitude, and longitude
co_data = co[:, level, lat_index, lon_index]
# Reshape the co_data array to have a shape of (365, 12)
co_data_reshaped = co_data.reshape((365, 12))

# Create a DataFrame with the reshaped data
df = pd.DataFrame(data=co_data_reshaped, index=pd.date_range(start=starting_date, periods=365), columns=['carbon'])

# Set the index to be the date range
df.index = pd.date_range(start=starting_date, periods=365)

# Print the DataFrame
print(df)
#df.to_csv("C:/Users/anind/Downloads/netcdf1.csv")



