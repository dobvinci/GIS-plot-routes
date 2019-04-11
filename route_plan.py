#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 08:48:47 2019

@author: dobvinci
"""
import gpxpy
import gpxpy.gpx
import folium
import math
#import journey GPX file as downloaded from http://map.project-osrm.org/
gpx_file = open('route_cost.gpx', 'r')
'''
My journey is planned with sleep over stops in two towns i.e Garissa and Wajir
'''
#my coordinates
hq=[-1.259201,36.786102] #Start point- Safaricom HQ
garissa=[-0.45880086 ,39.63615315] #Garissa BTS
wajir=[1.751611111,40.04830556]#Wajir BTS
mandera=[3.932805556,41.85686111]#Mandera BTS
#Function to calculated distance btw two points given x,y coordinates
def haversine(coord1, coord2):
    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    phi1, phi2 = math.radians(lat1), math.radians(lat2) 
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    #To return distance is km we divide results by 1000m and return floor to avoid floating points
    return (2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a)))//1000
#distances 
to_garissa=haversine(hq,garissa)
to_wajir=haversine(garissa,wajir)
to_mandera=haversine(wajir,mandera)


distance=(to_garissa+to_wajir+to_mandera)*2


#journey will take 4 nights 
nights=4
days=5 
total =0
mileage=0
perdiems=0
acc_cost=0
#function to calculate accomodation cost
def getAccommodationCosts(nights):
    accommodation=7000
    return accommodation*nights

#function to calculate mileage
def getMileageCosts(distance):
    #Total cost per km
    per_km=30 #cost per km
    return distance*per_km   
#function to calculate perdiem    
def getPerDiem(days):
     perdiem=8000
     return perdiem*days #Total perdiem

acc_cost=getAccommodationCosts(nights)# get accommodation costs
mileage=getMileageCosts(distance)# get mileage allowance
perdiems=getPerDiem(days)#get per diems
total=acc_cost+mileage+perdiems #calculate total journey cost
#print our total cost
print(" Total distance: {} KM \n Nights:{} \n Days: {} \n Accomodation Cost KSH: {}\n Per Diem KSH: {} \n Total Costs KSH: {}".format(distance,nights,days,acc_cost,perdiems,total))

gpx = gpxpy.parse(gpx_file) #parse our GPX file to Extract coordinates
points = [] #list for our coordinates
for track in gpx.tracks:
    for segment in track.segments:        
        for point in segment.points:
            points.append(tuple([point.latitude, point.longitude]))#save our corrdinates in pints list
#print(points)
start = points[0] #start coordinates
end=points[-1]#end corrdinates

#get our map midpoint for displaying on folium map
ave_lat = sum(p[0] for p in points)/len(points)
ave_lon = sum(p[1] for p in points)/len(points)
 
# Load map centred on above coordniates
my_map = folium.Map(location=[ave_lat, ave_lon],tiles='Stamen Terrain',attr='&copy;@vnjagi', zoom_start=7)

#our journey stop points coordinates
stops=[{"stop":"Garissa","cood":(-0.45880086 ,39.63615315)},{"stop":"Wajir","cood":(1.751611111,40.04830556)},{"stop":"Mandera","cood":(3.932805556,41.85686111)}]
#add a markers on stops
for each in stops:  
    folium.Marker(each["cood"],each["stop"],).add_to(my_map)

#set start and end points and colorise them
folium.Marker(start,'Safaricom HQ',icon=folium.Icon(color='green')).add_to(my_map)
folium.Marker(end,'Mandera BTS',icon=folium.Icon(color='red')).add_to(my_map)

#add poly line to map
folium.PolyLine(points, color='#3878C1',weight=8,opacity=0.7).add_to(my_map)
 
# Save map
my_map.save("mytravelmap.html")