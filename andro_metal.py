# coding=utf-8
"""
Iron Digger
"""
import math
from pandas import read_csv
import matplotlib
matplotlib.use('Agg')
from matplotlib.pyplot import scatter, show
from gmplot import gmplot

GMAP = gmplot.GoogleMapPlotter(12.925628, 77.68656, 13)
FILE = 'data/3.csv'
TOTAL_MAGNETIC_FIELD = []
DF1 = read_csv(FILE)
LONGITUDE = []
LATITUDE = []
MAGNETIC_FIELD = DF1[['MAGNETIC FIELD X (μT)', 'MAGNETIC FIELD Y (μT)',
                      'MAGNETIC FIELD Z (μT)', 'LOCATION Latitude : ',
                      'LOCATION Longitude : ']]
for index, row in MAGNETIC_FIELD.iterrows():
    x = math.sqrt((MAGNETIC_FIELD.loc[index, "MAGNETIC FIELD X (μT)"]) ** 2 +
                  (MAGNETIC_FIELD.loc[index, "MAGNETIC FIELD Y (μT)"]) ** 2 +
                  (MAGNETIC_FIELD.loc[index, "MAGNETIC FIELD Z (μT)"]) ** 2)
    if x >= 200:
        scatter(index, x, color='red')
        for i in range(5):
            LATITUDE.append(MAGNETIC_FIELD.loc[index, 'LOCATION Latitude : '])
            LONGITUDE.append(MAGNETIC_FIELD.loc[index, 'LOCATION Longitude : '])
        # gmap.scatter(latitude,longitude, 'red', size=15, marker=False)
    elif 100 <= x < 200:
        for i in range(2):
            LATITUDE.append(MAGNETIC_FIELD.loc[index, 'LOCATION Latitude : '])
            LONGITUDE.append(MAGNETIC_FIELD.loc[index, 'LOCATION Longitude : '])
        scatter(index, x, color='orange')
    elif 50 <= x < 100:
        for i in range(1):
            LATITUDE.append(MAGNETIC_FIELD.loc[index, 'LOCATION Latitude : '])
            LONGITUDE.append(MAGNETIC_FIELD.loc[index, 'LOCATION Longitude : '])
        scatter(index, x, color='darksalmon')
    TOTAL_MAGNETIC_FIELD.append(x)
MAGNETIC_FIELD['MAGNETIC FIELD TOTAL (μT)'] = TOTAL_MAGNETIC_FIELD
MAGNETIC_FIELD.hist(column='MAGNETIC FIELD TOTAL (μT)', bins=5000)
GMAP.heatmap(LATITUDE, LONGITUDE)
GMAP.draw("my_map.html")
show()
