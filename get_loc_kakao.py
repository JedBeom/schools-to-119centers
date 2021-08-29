import requests
import pandas as pd

def get_latitude_longtitude(query: str):
    param = {"query": query}

    res = requests.get("https://dapi.kakao.com/v2/local/search/address.json",
            # token을 수정해주세요.
            headers={"Authorization": "KakaoAK token"},
            params=param)

    documents = res.json()["documents"]
    if len(documents) <= 0:
        print("documents is 0")
        return (0, 0)

    road_address = documents[0]["road_address"]
    if road_address is None:
        print("road_address is None")
        return (0, 0)

    longtitude = road_address["x"]
    latitude = road_address["y"]

    return (latitude, longtitude)

centers = pd.read_csv("119centers.csv", header=0)
centers = centers.drop('전화번호', axis=1)

latitudes = [None] * len(centers)
longtitudes = [None] * len(centers)

for i, row in centers.iterrows():
    print(f"{i+1}/{len(centers)}")
    latitudes[i], longtitudes[i] = get_latitude_longtitude(row["주소"])

centers["latitude"] = latitudes
centers["longtitude"] = longtitudes

centers.to_csv("119centers_with_ll.csv", index=False)
