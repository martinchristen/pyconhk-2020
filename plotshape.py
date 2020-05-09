import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.feature import ShapelyFeature
from shapely.geometry import shape


def plot(s):
    proj = ccrs.PlateCarree()
    ax = plt.axes(projection=proj)
    ax.set_extent((s.bounds[0], s.bounds[2], s.bounds[1], s.bounds[3]), crs=ccrs.PlateCarree())
    shape_feature = ShapelyFeature([s], ccrs.PlateCarree(), facecolor='#AAFFAA', edgecolor='k')
    ax.add_feature(shape_feature);
    
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=2, color='gray', alpha=0.5, linestyle='--')
    gl.xlabels_top = False
    gl.ylabels_left = False
    gl.xlabel_style = {'size': 10, 'color': 'black'}
    gl.ylabel_style = {'size': 10, 'color': 'black'}
    
    return gl
    
    
    
    
    
def plot_merc(s):
    proj = ccrs.Mercator()
    ax = plt.axes(projection=proj)
    ax.set_extent((s.bounds[0], s.bounds[2], s.bounds[1], s.bounds[3]), crs=ccrs.PlateCarree())
    shape_feature = ShapelyFeature([s], ccrs.PlateCarree(), facecolor='#AAFFAA', edgecolor='k')
    ax.add_feature(shape_feature);

    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=2, color='gray', alpha=0.5, linestyle='--')
    gl.xlabels_top = False
    gl.ylabels_left = False
    gl.xlabel_style = {'size': 10, 'color': 'black'}
    gl.ylabel_style = {'size': 10, 'color': 'black'}
    
    return gl