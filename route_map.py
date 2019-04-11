#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 21:33:52 2019

@author: dobvinci
"""


import gpxpy
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()
gpx_file = open('route_cost.gpx', 'r')
gpx = gpxpy.parse(gpx_file)
print("Tracks {}".format(len(gpx.tracks)))
print("Segments {}".format(len(gpx.tracks[0].segments)))
print("Points {}".format(len(gpx.tracks[0].segments[0].points)))
data = gpx.tracks[0].segments[0].points
## Start Position
start = data[0]
print("Starting Point {}".format(start))
## End Position
finish = data[-1]

print("End Point {}".format(finish))
print("Duration {}".format(gpx.get_duration()))

distance=gpx.length_2d()/1000
print("2D Distance {} KM".format(distance))
df = pd.DataFrame(columns=['lon', 'lat'])
#print("3D Distance {} KM".format(gpx.length_3d()/1000))
df = pd.DataFrame(columns=['lon', 'lat'])
for point in data:
    df = df.append({'lon': point.longitude, 'lat' : point.latitude}, ignore_index=True)

data_path = 'lpq'
fig = plt.figure(facecolor = '0.05')
ax = plt.Axes(fig, [0., 0., 1., 1.], )
ax.set_aspect('equal')
ax.set_axis_off()
fig.add_axes(ax)
#fig.add_axes(ax)
sns.set_style("dark")
sns.despine(left=True,right=True)
x=[36.786102,39.63615315,40.04830556,41.85686111]
y=[-1.259201,-0.45880086,1.751611111,3.932805556]

plt.scatter(x,y, s = 100)
#plt.plot(df['lon'],df['lat'], color = 'deepskyblue', lw = 0.2, alpha = 0.8)
plt.plot(df['lon'],df['lat'], color = 'deepskyblue')
plt.ylabel("longitude")
plt.xlabel("Latitude")

plt.title("Route plan from Safaricom HQ Distance {} KM".format(distance))

filename = data_path + '.png'
plt.savefig(filename, facecolor = fig.get_facecolor(), bbox_inches='tight', pad_inches=0, dpi=300)
