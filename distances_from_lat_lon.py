import pandas as pd
import numpy as np
import math as math

def distance(lat1, lng1, lat2, lng2):
    #return distance as meter if you want km distance, remove "* 1000"
    radius = 6371 * 1000 

    dLat = (lat2-lat1) * math.pi / 180
    dLng = (lng2-lng1) * math.pi / 180

    lat1 = lat1 * math.pi / 180
    lat2 = lat2 * math.pi / 180

    val = sin(dLat/2) * sin(dLat/2) + sin(dLng/2) * sin(dLng/2) * cos(lat1) * cos(lat2)    
    ang = 2 * atan2(sqrt(val), sqrt(1-val))
    return radius * ang

data = pd.read_csv('analyze_me.csv')
df = pd.DataFrame(data)
df.describe().transpose()

for deliveries in df:
	deliveries['distance'] = distance(pickup_lat, pickup_lon, dropoff_lat, dropoff_lon)
