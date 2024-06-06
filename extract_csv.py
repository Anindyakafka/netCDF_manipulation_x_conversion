from netCDF4 import Dataset
import numpy as np
import pandas as pd

# Reading a netCDF file
data = Dataset(r'C:/Users/anind/Downloads/netcdf/TROPESS_reanalysis_6hr_so2_2005.nc', 'r')

# Storing netCDF latitude and longitude data keys as variables
lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
#print(lat,lon)

#storing the latitude and longitude of India into variables
lat_india = 20.5937
lon_india = 78.9629


#squared latitude and longitude
sq_lat = (lat - lat_india)**2
sq_lon = (lon - lon_india)**2
# indentifying the index of the minimum value of latitude and longitude
min_index_lat = lat.argmin()
min_index_lon = lon.argmin()
print(min_index_lat, min_index_lon)




so2 = data.variables['so2']
#print(so2[1, 27, 98, 70])

# Creating an empty pandas dataframe
starting_date = data.variables['time'].units[14:18]
print(starting_date)
#ending_date = data.variables['time'].units[13:15] + '-12-31'
#date_range = pd.date_range(start = starting_date, end = ending_date)
#df = pd.DataFrame(0, columns = ['sulpher'], index = date_range)
#print(df)
#t = data.variables['time'].units
#print(t)

dt = np.arange(0, data.variables['time'].size)
#print(dt)
#r = df.iloc[0]
#print(r)
#for time_index in dt:
    #df.iloc[time_index] = so2[time_index, 25, 0, 0]
#print(df)
#i = co[0, 98, 70]
#print(i)

#df.to_csv("C:/Users/anind/Downloads/netcdf/cdf.csv")




