import pandas as pd
import json
from haversine import haversine

# load schools
with open("schoolList_2020_04_hig.json", "r") as f:
    school_json = json.load(f)

schools = pd.DataFrame(school_json["list"])
schools = schools[['SCHUL_RDNMA', 'SCHUL_NM', 'LTTUD', 'LGTUD']]
schools["LTTUD"] = pd.to_numeric(schools["LTTUD"], downcast="float")
schools["LGTUD"] = pd.to_numeric(schools["LGTUD"], downcast="float")

# load 119 centers
centers = pd.read_csv("119centers_with_ll.csv")
centers["latitude"] = pd.to_numeric(centers["latitude"], downcast="float")
centers["longtitude"] = pd.to_numeric(centers["longtitude"], downcast="float")
centers = centers.loc[centers["latitude"] != 0]

"""
latitude1 = 35.438485
longtitude1 = 127.968246

latitude2 = 34.156297
longtitude2 = 125.831907

# filter only 전남
schools = schools.loc[(schools["LTTUD"] < latitude1) & (schools["LTTUD"] > latitude2) &
        (schools["LGTUD"] < longtitude1) & (schools["LGTUD"] > longtitude2)]

centers = centers.loc[(centers["latitude"] < latitude1) & (centers["latitude"] > latitude2) &
        (centers["longtitude"] < longtitude1) & (centers["longtitude"] > longtitude2)]
"""

def line_distance(school, center):
    school_location = (school["LGTUD"], school["LTTUD"])
    center_location = (center["longtitude"], center["latitude"])
    return haversine(school_location, center_location)


least_diss = [None] * len(schools)
least_centers = [None] * len(schools)
i = 0
for _, school in schools.iterrows():
    print(school["SCHUL_NM"])
    print(f"{i+1}/{len(schools)}")
    least_dis = 100000
    least_center = ""
    for j, center in centers.iterrows():
        dis = line_distance(school, center)
        if dis < least_dis:
            least_dis = dis
            least_center = center
        
    least_diss[i] = least_dis
    least_centers[i] = least_center['119안전센터명']

    i += 1
    
schools["least_dis"] = least_diss
schools["least_center"] = least_centers

schools.to_csv("schools_w_least.csv", index=False)

