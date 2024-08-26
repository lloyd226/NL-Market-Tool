import math 

def calculate_distance(in_latitude, in_longitude, latitude, longitude):
    first = (latitude - in_latitude)*(math.pi/180)
    second = (longitude - in_longitude)*(math.pi/180)
    third = math.pow(math.sin(first/2),2) + math.cos(in_latitude*math.pi/180) * math.cos(latitude*math.pi/180)*math.pow(math.sin(second/2),2)
    fourth = 2*math.atan2(math.sqrt(third),math.sqrt(1-third))
    return fourth*6371