from netCDF4 import Dataset
import xarray as xr
import pandas as pd
file_path = "C:/Users/anind/Downloads/netcdfnew/V6GL02.CNNPM25.Global.200501-200512.nc"

ds = xr.open_dataset(file_path)

# Print the dataset information
print(ds)

# Extract temperature data
temperature_data = ds['PM25']

#print(temperature_data.time)
# Convert to pandas DataFrame
temperature_df = temperature_data.to_dataframe()

# Reset index to flatten multi-index structure
temperature_df.reset_index(inplace=True)

# Save DataFrame to CSV
output_csv = "C:/Users/anind/Downloads/netcdfnew/pm25/pm25_2005.csv"
temperature_df.to_csv(output_csv, index=False)


