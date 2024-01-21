import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import netCDF4 as nc
import numpy as np

# Open the NetCDF file
ds = nc.Dataset('bathy_io.nc') 
ds.variables.keys()

# Read the data using the correct variable names
lon = ds.variables['LON13801_16801'][:]
lat = ds.variables['LAT5161_7081'][:]
bath = ds.variables['B_BATHY'][:]  

# Close the NetCDF file
ds.close()

# Since 'bath' is a 3D array, we take the 2D slice
bath_2d = bath[0, :, :]

# Generate 2D coordinate grids for lon and lat
lon2d, lat2d = np.meshgrid(lon, lat, indexing='ij')

lon2d, lat2d = lon2d.T, lat2d.T

# Create a figure with a Mercator projection
fig = plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.Mercator())

# Set the extent of the plot
ax.set_extent([85,95,0,10], crs=ccrs.PlateCarree())

# Plot the bathymetry data
pcm = ax.pcolormesh(lon2d, lat2d, bath_2d, transform=ccrs.PlateCarree(), shading='auto')

# Add colorbar
cbar = plt.colorbar(pcm, orientation='vertical')
cbar.ax.set_ylabel(r'depth(m)') # LaTeX formatted label

# Add contour lines for bathymetry
contour_lines = ax.contour(lon2d, lat2d, bath_2d, levels=[-1000], colors='k', transform=ccrs.PlateCarree())
plt.clabel(contour_lines, inline=True, fontsize=10, fmt='%1.0f')

# Set the color limits for the bathymetry data
pcm.set_clim(-5000,0)

# Add coastlines for reference
ax.coastlines()

# Show the plot
plt.show()



