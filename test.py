import pickle
import numpy as np
import gmplot 
gmap=gmplot.GoogleMapPlotter(47.6097,-122.3331,13)


locs=pickle.load(open('./blockfacelocs.p','rb')) # load location data
clusterlocs=np.asarray(locs.values())
lats = []
lons = []
for loc in clusterlocs:
    lats.append(loc[1])
    lats.append(loc[3])
    lons.append(loc[0])
    lons.append(loc[2])

gmap.heatmap(lats, lons)
gmap.draw("map.html")
