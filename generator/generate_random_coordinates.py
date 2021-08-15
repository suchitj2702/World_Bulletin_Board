from __future__ import division
import numpy as np
from math import radians, cos, sin, asin, sqrt
import csv

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def create_random_point(latitude, longitude, distance):
    r = distance/111300
    u = np.random.uniform(0,1)
    v = np.random.uniform(0,1)
    w = r * np.sqrt(u)
    t = 2 * np.pi * v
    x = w * np.cos(t)
    x1 = x/np.cos(longitude)
    y = w*np.sin(t)
    return latitude + x1, longitude + y

def generate_random_points(latitude, longitude, radius, number_of_points):
    radius = radius*1000
    with open('dummy_lats_longs_5000km_20.csv', mode='w') as csv_file:
        dummy_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        dummy_writer.writerow(["latitude", "longitude", "distance_from_central_point"])
        dummy_writer.writerow([latitude, longitude, 0])
        for i in range(number_of_points):
            new_latitude, new_longitude = create_random_point(latitude, longitude, radius)
            dist = haversine(new_latitude, new_longitude, latitude, longitude)
            dummy_writer.writerow([new_latitude, new_longitude, dist])

            print(new_latitude, new_longitude, dist)

def generate_random_points_from_other_points(radius, number_of_points_per_point):
    radius = radius*1000
    count = 0
    with open('dummy_lats_longs_all.csv', mode='w') as csv_writing_file:
        dummy_writer = csv.writer(csv_writing_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        dummy_writer.writerow(["latitude", "longitude", "idx"])
        with open('dummy_lats_longs_all_generator.csv', mode='w') as csv_writing_file_generator:
            dummy_writer_generator = csv.writer(csv_writing_file_generator, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            with open('dummy_lats_longs_5000km_20.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                        continue
                    else:
                        for i in range(number_of_points_per_point):
                            new_latitude, new_longitude = create_random_point(float(row[0]), float(row[1]), radius)
                            dummy_writer.writerow([new_latitude, new_longitude, count])
                            dummy_writer_generator.writerow([new_latitude, new_longitude, count])
                            count = count + 1
                    line_count += 1

if __name__ == "__main__":
    #generate_random_points(33.4142485223105, -111.91875457763673, 5000, 20)
    generate_random_points_from_other_points(5, 50)

