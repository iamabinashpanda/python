# Write a program to find the distance between two locations when their latitude and longitudes are given.

import math

d = 6371.009
lat1, long1 = math.radians(50.0359), math.radians(005.4253)
lat2, long2 = math.radians(58.3838), math.radians(003.0412)
lat_diff = lat2 - lat1

long_diff = long2 - long1
lat_diff = lat2 - lat1

D = d*2*math.asin(math.sqrt(((math.sin(lat_diff)/2)**2)+(((math.sin(long_diff)/2)**2)*math.cos(lat1)*math.cos(lat2))))
print(round(D,2))