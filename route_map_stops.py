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
gpx_file = open('route_stops.gpx', 'r')
gpx = gpxpy.parse(gpx_file)
len(gpx.tracks)
len(gpx.tracks[0].segments)
len(gpx.tracks[0].segments[0].points)
data = gpx.tracks[0].segments[0].points
## Start Position
start = data[0]

## End Position
finish = data[-1]
x=[36.78607,39.63615315,41.85686111]
y=[-1.25946,-0.45880086,3.932805556]
print(start,finish)
df = pd.DataFrame(columns=['lon', 'lat'])

for point in data:
    df = df.append({'lon': point.longitude, 'lat' : point.latitude}, ignore_index=True)

fig = plt.figure(facecolor = '0.05')
ax = plt.Axes(fig, [0., 0., 1., 1.], )
ax.set_aspect('equal')
ax.set_axis_off()
fig.add_axes(ax)
plt.plot(df['lon'],df['lat'])
plt.scatter(x,y)
plt.ylabel("longitude")
plt.xlabel("Latitude")
plt.title("Route from Safaricom HQ to furthest BTS  (With stops)")
filename = 'route_with_stops.png'
plt.savefig(filename, facecolor = fig.get_facecolor(), bbox_inches='tight', pad_inches=0, dpi=300)
