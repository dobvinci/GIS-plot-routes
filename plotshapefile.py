#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 19:52:51 2019

@author: dobvinci
"""
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from descartes import PolygonPatch
import fiona
from shapely.geometry import Polygon, MultiPolygon, shape
import pandas as pd
import seaborn as sns
bts=pd.read_csv("Shapefile/bts for gis practicals.csv")
sns.set()
#Open the shapefile
mp = MultiPolygon(
    [shape(pol['geometry']) for pol in fiona.open('Shapefile/ke_county.shp') ])
#plot the shape
cm = plt.get_cmap('RdBu')
num_colours = len(mp)
#set the mapsize
fig = plt.figure(figsize=(10, 8), dpi=80)
ax = fig.add_subplot(111)
minx, miny, maxx, maxy = mp.bounds
w, h = maxx - minx, maxy - miny
ax.set_xlim(minx - 0.2 * w, maxx + 0.2 * w)
ax.set_ylim(miny - 0.2 * h, maxy + 0.2 * h)
ax.set_aspect(1)
patches = []
for idx, p in enumerate(mp):
    colour = cm(1. * idx / num_colours)
    patches.append(PolygonPatch(p, fc=colour, ec='#555555', alpha=1., zorder=1))
ax.add_collection(PatchCollection(patches, match_original=True))
ax.set_xticks([])
ax.set_yticks([])
sns.scatterplot(x=bts['Longitude'],y=bts['Latitude'],hue=bts['Technology'],data=bts)
plt.title("Kenya Counties and BTS")
plt.savefig('kenya_from_shp.png', alpha=True, dpi=300)
plt.show()