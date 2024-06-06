from netCDF4 import Dataset 
import numpy as np
import pandas as pd

data = Dataset(r'C:/Users/anind/Downloads/netcdf/MERRA2_100.tavgU_2d_aer_Nx.198002.nc4', 'r')

#display data variable names
print(data.variables.keys())

#Access variables
#lon = data.variables['lon']
#print(lon)

#lon_bnds = data.variables['lon_bnds']
#print(lon_bnds)

#lat = data.variables['lat']
#print(lat)

#lat_bnds = data.variables['lat_bnds']
#print(lat_bnds)

#time = data.variables['time'].units
#print(time)

#time_bnds = data.variables['time_bnds']
#print(time_bnds)

#lev = data.variables['lev']
#print(lev)

#lev_bnds = data.variables['lev_bnds']
#print(lev_bnds)
so2 = data.variables['SO2SMASS']
print(so2)

#Access data from variables
#time_data = data.variables['time'][:]
#print(time_data)

#lon_data = data.variables['lon'][:]
#print(lon_data)

#lat_data = data.variables['lat'][:]
#print(lat_data)

#so2_data = data.variables['so2'][:]
#print(co_data)

#lev_data = data.variables['lev'][:]
#print(lev_data)

#df = pd.DataFrame[time_data][so2_data][:]
#print(df)