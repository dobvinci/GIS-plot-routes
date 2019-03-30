#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 21:33:52 2019

@author: dobvinci
"""


import gpxpy
import matplotlib.pyplot as plt
import pandas as pd
gpx_file = open('route1.gpx', 'r')
gpx = gpxpy.parse(gpx_file)
len(gpx.tracks)
len(gpx.tracks[0].segments)
len(gpx.tracks[0].segments[0].points)
data = gpx.tracks[0].segments[0].points
## Start Position
start = data[0]
## End Position
finish = data[-1]
df = pd.DataFrame(columns=['lon', 'lat'])

for point in data:
    df = df.append({'lon': point.longitude, 'lat' : point.latitude}, ignore_index=True)
plt.plot(df['lat'],df['lon'])
plt.ylabel("longitude")
plt.xlabel("Latitude")
plt.title("Route from Safaricom HQ to furthest BTS  (With stops)")