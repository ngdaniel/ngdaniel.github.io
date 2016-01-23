import pickle
import gmplot 
import xlrd
import pprint
import csv
gmap=gmplot.GoogleMapPlotter(47.6097,-122.3331,13)
cross_reference_xls = xlrd.open_workbook('crossreferencesheet2.xlsx').sheet_by_index(0)
keys = cross_reference_xls.row(0)
for x in xrange(len(keys)):
    keys[x] = str(keys[x])[7:len(str(keys[x]))-1]

cross_reference = {}
for x in xrange(cross_reference_xls.nrows):
    print cross_reference_xls.row(x) 

locs = pickle.load(open('blockfacelocs.p','rb')) # load location data
lats = []
lons = []
for id in locs.keys():
    locs[id] = [(locs[id][1] + locs[id][3])/2, (locs[id][0] + locs[id][2])/2]
    lats.append(locs[id][0])
    lons.append(locs[id][1])

pickle.dump(locs, open('avgblockfacelocs.pickle', 'wb'))
gmap.heatmap(lats, lons)
gmap.draw("map.html")
