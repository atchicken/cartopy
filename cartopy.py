import cartopy.crs as ccrs
import cartopy.feature as cfea
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(10,10))
ax=plt.axes(projection=ccrs.PlateCarree())
#ax.coastlines(resolution='110m')
ax.gridlines(draw_labels=True)
ax.set_extent((120.0, 160.0, 15.0, 65.0),ccrs.PlateCarree())
ax.add_feature(cfea.OCEAN,color='#00FFFF')
ax.add_feature(cfea.LAND,color='#32CD32')
#plt.title('Map', fontsize='15')
plt.savefig("PlateCarree.png")
plt.show()
